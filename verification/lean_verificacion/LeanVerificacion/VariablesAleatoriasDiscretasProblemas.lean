import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Variables aleatorias discretas — problemas

Formaliza los 6 problemas de `latex/variables_aleatorias_discretas(p).tex`.
Todos son Tier A (aritmética exacta de racionales sobre PMFs explícitas) o
Tier B (identidades generales: la suma telescópica de `prob:cb2247c`, y la
cota de raíz cuadrada exacta usada en `prob:d332420` para confirmar
$\sigma_R\approx56.71$ y concluir $U<0$ sin recurrir a `scipy`, ya que solo
se necesita una cota, no el valor exacto de $\sqrt{3216}$). Ningún problema
de este archivo requiere la capa de esperanza sobre `MeasureTheory` — todas
las variables aleatorias tienen soporte finito explícito, así que la
esperanza/varianza son sumas finitas ponderadas (ver `konig_huygens` en
`VariablesAleatoriasDiscretas.lean`).
-/

namespace VariablesAleatoriasDiscretasProblemas

/-- `prob:2c27c8e` (Recordar) — $f(x)=cx^2$ en $\{1,2,3,4\}$: normalización
$c=1/30$; $P(X\ge3)=5/6$; $P(X\text{ par}\mid X\ge2)=20/29$. -/
theorem prob_2c27c8e :
    let f : ℕ → ℚ := fun x => (x : ℚ) ^ 2 / 30
    f 1 + f 2 + f 3 + f 4 = 1 ∧
      f 3 + f 4 = 5 / 6 ∧
      (f 2 + f 4) / (f 2 + f 3 + f 4) = 20 / 29 := by
  norm_num

/-- `prob:9efeaae` (Comprender) — PMF $(0.40,0.30,0.20,0.10)$ en $\{0,1,2,3\}$;
$F(1)=0.70$; $P(\text{rechazo})=P(X\ge2)=1-F(1)=0.30$. -/
theorem prob_9efeaae :
    let f0 : ℚ := 0.40
    let f1 : ℚ := 0.30
    let f2 : ℚ := 0.20
    let f3 : ℚ := 0.10
    let F1 := f0 + f1
    f0 + f1 + f2 + f3 = 1 ∧ F1 = 0.70 ∧ 1 - F1 = 0.30 := by
  norm_num

/-- `prob:c324c4f` (Aplicar) — PMF $(0.35,0.30,0.20,0.10,0.05)$ en
$\{0,\dots,4\}$: $\mu=1.20$, $E[X^2]=2.80$, $\mathrm{Var}(X)=1.36$ vía
König-Huygens. -/
theorem prob_c324c4f :
    let f0 : ℚ := 0.35
    let f1 : ℚ := 0.30
    let f2 : ℚ := 0.20
    let f3 : ℚ := 0.10
    let f4 : ℚ := 0.05
    let mu := 0 * f0 + 1 * f1 + 2 * f2 + 3 * f3 + 4 * f4
    let EX2 := (0 : ℚ) ^ 2 * f0 + 1 ^ 2 * f1 + 2 ^ 2 * f2 + 3 ^ 2 * f3 + 4 ^ 2 * f4
    mu = 1.20 ∧ EX2 = 2.80 ∧ EX2 - mu ^ 2 = 1.36 := by
  norm_num

/-- Identidad telescópica general detrás de `prob:cb2247c`: para todo
$N\in\mathbb N$, $\sum_{i=0}^{N-1}\frac{1}{(i+1)(i+2)}=\frac{N}{N+1}$
(reindexado de $\sum_{x=1}^N\frac{1}{x(x+1)}$ con $x=i+1$), probado por
inducción sobre `Finset.range`, no citado de memoria. -/
theorem telescoping_parcial (N : ℕ) :
    ∑ i ∈ Finset.range N, (1 : ℚ) / ((i + 1) * (i + 2)) = N / (N + 1) := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih]
    have h1 : (n : ℚ) + 1 ≠ 0 := by positivity
    have h2 : (n : ℚ) + 2 ≠ 0 := by positivity
    push_cast
    field_simp
    ring

/-- `prob:cb2247c` (Analizar) — la constante de normalización $c_N=(N+1)/N$
satisface $c_N\cdot\sum_{x=1}^N\frac{1}{x(x+1)}=1$ para todo $N\ge1$,
reutilizando `telescoping_parcial`. -/
theorem prob_cb2247c (N : ℕ) (hN : 1 ≤ N) :
    let cN : ℚ := (N + 1) / N
    cN * ∑ i ∈ Finset.range N, (1 : ℚ) / ((i + 1) * (i + 2)) = 1 := by
  intro cN
  rw [telescoping_parcial N]
  have hN' : (N : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have hN1 : (N : ℚ) + 1 ≠ 0 := by positivity
  simp only [cN]
  field_simp

/-- `prob:d332420` (Evaluar), parte cuantitativa exacta — $E[R]=42$,
$\mathrm{Var}(R)=3216$ (M USD), vía König-Huygens sobre los tres escenarios
dados. -/
theorem prob_d332420 :
    let p1 : ℚ := 0.25
    let r1 : ℚ := 120
    let p2 : ℚ := 0.55
    let r2 : ℚ := 40
    let p3 : ℚ := 0.20
    let r3 : ℚ := -50
    let ER := p1 * r1 + p2 * r2 + p3 * r3
    let ER2 := p1 * r1 ^ 2 + p2 * r2 ^ 2 + p3 * r3 ^ 2
    ER = 42 ∧ ER2 - ER ^ 2 = 3216 := by
  norm_num

/-- `prob:d332420`, parte del riesgo — $\sigma_R=\sqrt{3216}$ no es racional,
así que en vez de aproximarlo numéricamente con `scipy` (como en capítulos
previos) se prueba una cota exacta $56.70<\sigma_R<56.71$ (consistente con el
$\approx56.71$ del libro) directamente en Lean vía `Real.lt_sqrt`/
`Real.sqrt_lt'`, suficiente para concluir formalmente $U=E[R]-1.25\sigma_R<0$
— la misma conclusión de rechazo del libro. -/
theorem prob_d332420_riesgo :
    (56.70 : ℝ) < Real.sqrt 3216 ∧ Real.sqrt 3216 < 56.71 ∧
      (42 : ℝ) - 1.25 * Real.sqrt 3216 < 0 := by
  have hlo : (56.70 : ℝ) < Real.sqrt 3216 := by
    rw [Real.lt_sqrt (by norm_num)]
    norm_num
  have hhi : Real.sqrt (3216 : ℝ) < 56.71 := by
    rw [Real.sqrt_lt' (by norm_num)]
    norm_num
  exact ⟨hlo, hhi, by nlinarith⟩

/-- `prob:e538b1b` (Crear) — ejemplo del libro (tickets de soporte técnico):
PMF $(0.10,0.25,0.30,0.25,0.10)$ en $\{0,\dots,4\}$; CDF acumulada
$(0.10,0.35,0.65,0.90,1.00)$; cuantil $q_{0.75}=3$ porque $F(2)=0.65<0.75$ y
$F(3)=0.90\ge0.75$ (la condición que define el cuantil, no solo el resultado
citado). -/
theorem prob_e538b1b :
    let f0 : ℚ := 0.10
    let f1 : ℚ := 0.25
    let f2 : ℚ := 0.30
    let f3 : ℚ := 0.25
    let f4 : ℚ := 0.10
    let F0 := f0
    let F1 := F0 + f1
    let F2 := F1 + f2
    let F3 := F2 + f3
    let F4 := F3 + f4
    f0 + f1 + f2 + f3 + f4 = 1 ∧
      F0 = 0.10 ∧ F1 = 0.35 ∧ F2 = 0.65 ∧ F3 = 0.90 ∧ F4 = 1.00 ∧
      F2 < 0.75 ∧ (0.75 : ℚ) ≤ F3 := by
  norm_num

end VariablesAleatoriasDiscretasProblemas
