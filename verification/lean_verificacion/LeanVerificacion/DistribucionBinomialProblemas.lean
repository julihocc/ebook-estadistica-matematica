import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Vandermonde
import Mathlib.Algebra.BigOperators.NatAntidiagonal
import LeanVerificacion.DistribucionBinomial

/-!
# Distribución binomial — problemas

Formaliza `latex/distribucion_binomial(p).tex`. `prob:71ce5a0` (recordar
fórmulas de memoria) y `prob:1149be6` (justificación en prosa de por qué el
conteo da $\binom nk$) no se formalizan más allá de lo ya cubierto en
`DistribucionBinomial.lean` — son recordatorio/argumento verbal, no cálculo
nuevo. `prob:19f50da` es mayormente prosa evaluativa (validez de la
aproximación Normal, corrección de continuidad); solo se formaliza la
comprobación numérica concreta de la regla operativa $np\ge5$, $n(1-p)\ge5$
que sí aparece como cálculo explícito en el texto.
-/

namespace DistribucionBinomialProblemas

/-- `prob:c3d2032` (Aplicar) — $X\sim\mathrm{Bin}(12,0.15)$ ($p=3/20$ exacto):
$P(X\le2)\approx0.7358$; $P(X\ge4\mid X\ge1)\approx0.1075$. Los cinco valores
intermedios que el libro cita explícitamente ($P(X=0),P(X=1),P(X=2),P(X=3)$,
$P(X\le3)$) se verifican por separado, no solo el resultado final. -/
theorem prob_c3d2032 :
    let p : ℚ := 3 / 20
    let q : ℚ := 17 / 20
    let P0 : ℚ := (Nat.choose 12 0 : ℚ) * p ^ 0 * q ^ 12
    let P1 : ℚ := (Nat.choose 12 1 : ℚ) * p ^ 1 * q ^ 11
    let P2 : ℚ := (Nat.choose 12 2 : ℚ) * p ^ 2 * q ^ 10
    let P3 : ℚ := (Nat.choose 12 3 : ℚ) * p ^ 3 * q ^ 9
    let Ple2 := P0 + P1 + P2
    let Ple3 := Ple2 + P3
    |(P0 : ℝ) - 0.14224| < 1e-5 ∧ |(P1 : ℝ) - 0.30121| < 1e-5 ∧
      |(P2 : ℝ) - 0.29236| < 1e-5 ∧ |(Ple2 : ℝ) - 0.7358| < 1e-4 ∧
      |(P3 : ℝ) - 0.17197| < 1e-5 ∧ |(Ple3 : ℝ) - 0.90778| < 1e-4 ∧
      |(((1 - Ple3) / (1 - P0) : ℚ) : ℝ) - 0.1075| < 1e-4 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num [Nat.choose]

/-- Identidad de Vandermonde en la forma exacta del libro:
$\sum_{j=0}^m\binom{n_1}j\binom{n_2}{m-j}=\binom{n_1+n_2}m$ — reindexado de
`Nat.add_choose_eq` (que suma sobre `antidiagonal`) a una suma sobre
`Finset.range`, vía `Finset.Nat.sum_antidiagonal_eq_sum_range_succ`. -/
theorem vandermonde_binomial (n1 n2 m : ℕ) :
    ∑ j ∈ Finset.range (m + 1), n1.choose j * n2.choose (m - j) = (n1 + n2).choose m := by
  rw [Nat.add_choose_eq,
    Finset.Nat.sum_antidiagonal_eq_sum_range_succ (fun i j => n1.choose i * n2.choose j) m]

/-- `prob:bae56b2` (Analizar), núcleo combinatorio — la identidad de
Vandermonde citada por el libro es exactamente `vandermonde_binomial` arriba
(no una nueva verificación independiente). La aditividad de $E[\cdot]$ y
$\mathrm{Var}(\cdot)$ bajo $Z=X+Y$ es consecuencia algebraica directa de
`esperanza_binomial`/`varianza_binomial` de `DistribucionBinomial.lean`
aplicados a $n_1+n_2$: $(n_1+n_2)p=n_1p+n_2p$ y $(n_1+n_2)pq=n_1pq+n_2pq$.
**No formalizado aquí** (Tier B, factible con más trabajo de aritmética de
exponentes con resta de `ℕ`, no crítico dado que el núcleo combinatorio ya
está verificado): la derivación completa de que la *convolución* de las dos
PMFs binomiales, término a término, coincide con la PMF de
$\mathrm{Bin}(n_1+n_2,p)$ — requiere además manejar los exponentes
$p^jq^{n_1-j}\cdot p^{m-j}q^{n_2-(m-j)}=p^mq^{n_1+n_2-m}$, válidos solo para
los términos no nulos de la suma ($j\le n_1$, $m-j\le n_2$). -/
theorem prob_bae56b2_aditividad (n1 n2 : ℕ) (p q : ℝ) :
    (n1 + n2 : ℝ) * p = (n1 : ℝ) * p + (n2 : ℝ) * p ∧
      (n1 + n2 : ℝ) * p * q = (n1 : ℝ) * p * q + (n2 : ℝ) * p * q := by
  constructor <;> ring

/-- `prob:19f50da` (Evaluar), única parte cuantitativa — la regla operativa
$np\ge5$, $n(1-p)\ge5$ sí se satisface para $n=500$, $p=0.04$
($np=20$, $n(1-p)=480$). El resto del problema (validez de la corrección de
continuidad de Yates) es evaluación cualitativa en prosa, no formalizable. -/
theorem prob_19f50da :
    (500 : ℝ) * 0.04 ≥ 5 ∧ (500 : ℝ) * (1 - 0.04) ≥ 5 := by
  norm_num

/-- `prob:3c14103` (Crear) — ejemplo del libro (germinación de semillas):
$X\sim\mathrm{Bin}(15,0.7)$, $\mathbb E[X]=15(0.7)=10.5$,
$\mathrm{Var}(X)=15(0.7)(0.3)=3.15$. -/
theorem prob_3c14103 :
    (15 : ℝ) * 0.7 = 10.5 ∧ (15 : ℝ) * 0.7 * (1 - 0.7) = 3.15 := by
  norm_num

end DistribucionBinomialProblemas
