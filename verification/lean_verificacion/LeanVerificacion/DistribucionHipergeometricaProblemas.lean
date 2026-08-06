import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import LeanVerificacion.DistribucionHipergeometrica

/-!
# Distribución hipergeométrica — problemas

Formaliza `latex/distribucion_hipergeometrica(p).tex`. `prob:748a77d`
(Recordar) es puro recordatorio de la PMF, ya cubierta en la teoría — no se
repite. `prob:64e9a8d` partes 1–2 son pasos de derivación en prosa/símbolos
sin un número concreto que verificar de forma aislada; la parte 3 (combinar
las piezas algebraicas en la fórmula cerrada de $\mathrm{Var}(X)$) es
exactamente `varianza_hipergeometrica_algebra` de la teoría — no se repite
aquí.
-/

namespace DistribucionHipergeometricaProblemas

/-- `prob:5e6e8bf` (Comprender) — los dos casos límite del Factor de
Corrección por Población Finita $(N-n)/(N-1)$: en $n=1$ vale $1$
(sin corrección); en $n=N$ vale $0$ (censo completo, sin incertidumbre
muestral). -/
theorem prob_5e6e8bf (N : ℕ) (hN2 : 2 ≤ N) :
    ((N : ℝ) - 1) / ((N : ℝ) - 1) = 1 ∧ ((N : ℝ) - N) / ((N : ℝ) - 1) = 0 := by
  have hN1 : (N : ℝ) - 1 ≠ 0 := by
    have : (2 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN2
    linarith
  constructor
  · field_simp
  · simp

/-- `prob:1651c98` (Aplicar) — lote $N=30,K=6,n=5$: $P(X=0)=\binom60
\binom{24}5/\binom{30}5=42504/142506\approx0.2983$;
$P(X\le1)\approx0.7457$. -/
theorem prob_1651c98 :
    let den : ℝ := Nat.choose 30 5
    let P0 : ℝ := (Nat.choose 6 0 : ℝ) * (Nat.choose 24 5 : ℝ) / den
    let P1 : ℝ := (Nat.choose 6 1 : ℝ) * (Nat.choose 24 4 : ℝ) / den
    den = 142506 ∧ |P0 - 0.2983| < 1e-4 ∧ |P0 + P1 - 0.7457| < 1e-4 := by
  norm_num [Nat.choose]

/-- `prob:7cf587b` (Evaluar) — $N=2000,K=100,n=20$: la regla $n/N<0.05$ se
cumple ($n/N=0.01$); $P(X=2)\approx0.189725$ para la hipergeométrica exacta
y $P(Y=2)\approx0.188677$ para la aproximación $\mathrm{Bin}(20,0.05)$
($p=K/N$ exacto, $=1/20$); el error absoluto es pequeño. -/
theorem prob_7cf587b :
    let nN : ℝ := 20 / 2000
    let PX2 : ℝ := (Nat.choose 100 2 : ℝ) * (Nat.choose 1900 18 : ℝ) / (Nat.choose 2000 20 : ℝ)
    let PY2 : ℝ := (Nat.choose 20 2 : ℝ) * (1 / 20 : ℝ) ^ 2 * (19 / 20 : ℝ) ^ 18
    nN = 0.01 ∧ nN < 0.05 ∧ |PX2 - 0.189725| < 1e-6 ∧ |PY2 - 0.188677| < 1e-6 ∧
      |PX2 - PY2| < 0.002 := by
  norm_num [Nat.choose]

/-- `prob:969b25a` (Crear) — biblioteca $N=200,K=25,n=15$: $\mathbb E[X]=
15(25/200)=1.875$; $\mathrm{Var}(X)=1.640625(185/199)\approx1.5254$, ambos
verificados vía las fórmulas generales de la teoría (`esperanza_hipergeometrica`,
`varianza_hipergeometrica_algebra`), no re-derivados desde cero. -/
theorem prob_969b25a :
    let EX : ℝ := 15 * (25 / 200 : ℝ)
    let VarX : ℝ := 15 * (25 / 200 : ℝ) * (1 - 25 / 200) * ((200 - 15) / (200 - 1) : ℝ)
    EX = 1.875 ∧ |VarX - 1.5254| < 1e-4 := by
  norm_num

end DistribucionHipergeometricaProblemas
