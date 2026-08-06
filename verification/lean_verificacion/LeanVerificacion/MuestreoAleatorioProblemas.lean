import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Muestreo aleatorio — problemas

Formaliza los problemas de `latex/muestreo_aleatorio(p).tex`. `prob:293fd20`
(no existencia de momentos de Cauchy, funciones características) requiere
teoría de integración de Lebesgue que el proyecto no ha construido — **Tier
D, no formalizado**, ver bitácora de hallazgos. `prob:0c980d4` (que
$E(S^2)=\sigma^2$) se divide en dos partes: la identidad algebraica
$\sum(X_i-\bar X)^2=\sum(X_i-\mu)^2-n(\bar X-\mu)^2$ que el libro deriva
(líneas 100-108) es pura aritmética de `Finset.sum` sobre $\mathbb{R}$ y **sí
se formaliza** (`descomposicion_varianza`); solo el paso final de aplicar el
operador de esperanza $E[\cdot]$ (líneas 109-116) requiere una capa de
variables aleatorias que el proyecto no ha construido — Tier D para esa
última parte únicamente.
-/

namespace MuestreoAleatorioProblemas

/-- Identidad algebraica detrás de `prob:0c980d4` (líneas 100-108 del libro):
para cualquier familia finita $X_i$ y cualquier constante $\mu$,
$\sum_i(X_i-\bar X)^2 = \sum_i(X_i-\mu)^2 - n(\bar X-\mu)^2$, donde
$\bar X=(\sum_i X_i)/n$. Es exactamente el paso algebraico que el libro
demuestra antes de aplicar el operador de esperanza; ese último paso
($E[(X_i-\mu)^2]=\sigma^2$, $E[(\bar X-\mu)^2]=\sigma^2/n$) no se formaliza
aquí (Tier D — requiere una capa de variables aleatorias/esperanza que el
proyecto no ha construido). -/
theorem descomposicion_varianza {ι : Type*} (s : Finset ι) (X : ι → ℝ) (μ : ℝ)
    (hne : s.Nonempty) :
    let n : ℝ := s.card
    let Xbar := (∑ i ∈ s, X i) / n
    ∑ i ∈ s, (X i - Xbar) ^ 2 = ∑ i ∈ s, (X i - μ) ^ 2 - n * (Xbar - μ) ^ 2 := by
  intro n Xbar
  have hn0 : n ≠ 0 := Nat.cast_ne_zero.mpr (Finset.card_ne_zero.mpr hne)
  have hsum_eq : (∑ i ∈ s, X i) = n * Xbar := by
    change (∑ i ∈ s, X i) = n * ((∑ i ∈ s, X i) / n)
    field_simp
  have hdev_sum : ∑ i ∈ s, (X i - μ) = n * (Xbar - μ) := by
    have hsplit : ∑ i ∈ s, (X i - μ) = (∑ i ∈ s, X i) - s.card • μ := by
      rw [Finset.sum_sub_distrib, Finset.sum_const]
    rw [hsplit, hsum_eq, nsmul_eq_mul]
    ring
  have expand : ∑ i ∈ s, (X i - Xbar) ^ 2 =
      ∑ i ∈ s, ((X i - μ) ^ 2 - 2 * (Xbar - μ) * (X i - μ) + (Xbar - μ) ^ 2) := by
    refine Finset.sum_congr rfl fun i _ => ?_
    ring
  rw [expand, Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum,
    hdev_sum, Finset.sum_const, nsmul_eq_mul]
  ring

/-- `prob:0c980d4` (Analizar), parte algebraica — es exactamente
`descomposicion_varianza`; el paso final ($E[\cdot]$) queda Tier D. -/
theorem prob_0c980d4 {ι : Type*} (s : Finset ι) (X : ι → ℝ) (μ : ℝ) (hne : s.Nonempty) :
    let n : ℝ := s.card
    let Xbar := (∑ i ∈ s, X i) / n
    ∑ i ∈ s, (X i - Xbar) ^ 2 = ∑ i ∈ s, (X i - μ) ^ 2 - n * (Xbar - μ) ^ 2 :=
  descomposicion_varianza s X μ hne

/-- `prob:c0cebb4` (Recordar) — error estándar $\sigma_{\bar X}=\sigma/\sqrt n$
con $\sigma=12$, para $n=9,36,144,576$: $4.00, 2.00, 1.00, 0.50$. Se usa
`Real.sqrt n` literalmente (no el resultado ya calculado a mano $3,6,12,24$),
para que un $n$ incorrecto en el libro no pudiera colarse. -/
theorem prob_c0cebb4 :
    let sigma : ℝ := 12
    sigma / Real.sqrt 9 = 4 ∧ sigma / Real.sqrt 36 = 2 ∧
      sigma / Real.sqrt 144 = 1 ∧ sigma / Real.sqrt 576 = 0.5 := by
  have h9 : Real.sqrt 9 = 3 := by
    rw [show (9 : ℝ) = 3 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  have h36 : Real.sqrt 36 = 6 := by
    rw [show (36 : ℝ) = 6 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  have h144 : Real.sqrt 144 = 12 := by
    rw [show (144 : ℝ) = 12 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  have h576 : Real.sqrt 576 = 24 := by
    rw [show (576 : ℝ) = 24 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  simp only [h9, h36, h144, h576]
  norm_num

/-- `prob:116017b` (Comprender) — población finita $N=6$, muestra $n=3$: con
reemplazo $6^3=216$; sin reemplazo (no ordenado) $\binom{6}{3}=20$. La parte 3
(argumento asintótico $N\to\infty$) es prosa/límite cualitativo, no se
formaliza (Tier D). -/
theorem prob_116017b : (6 : ℕ) ^ 3 = 216 ∧ Nat.choose 6 3 = 20 := by decide

/-- `prob:2da8cc3` (Aplicar) — tamaño de muestra mínimo: $n = (z_{\alpha/2}
\sigma/E)^2 = (1.96\times8/1.5)^2 \approx 109.27$, y el entero mínimo que
satisface $n \ge 109.27$ es $110$. El valor exacto de $(1.96\times8/1.5)^2$ se
liga con `let` y se reutiliza para la comparación de redondeo. -/
theorem prob_2da8cc3 :
    let z : ℝ := 1.96
    let sigma : ℝ := 8
    let E : ℝ := 1.5
    let nExacto := (z * sigma / E) ^ 2
    |nExacto - 109.27| < 1e-2 ∧ (109 : ℝ) < nExacto ∧ nExacto ≤ 110 := by
  norm_num

/-- `prob:b7567ec` (Crear) — tornillos: $\mu=10$, $\sigma=0.5$, $n=64$,
$\sigma_{\bar X}=\sigma/\sqrt{64}=0.5/8=0.0625$, $z_1=-1.6$, $z_2=1.6$
(exactos). Se usa `Real.sqrt 64` literalmente (no el $8$ ya calculado a
mano). La evaluación final $2\Phi(1.6)-1\approx0.8904$ requiere la CDF normal
— Tier C, ver `verification/scipy/muestreo_aleatorio/tornillos.py`. El error
estándar se liga con `let` y se reutiliza para ambos puntajes $Z$. -/
theorem prob_b7567ec_parte_lean :
    let mu : ℝ := 10
    let sigma : ℝ := 0.5
    let seXbar := sigma / Real.sqrt 64
    seXbar = 0.0625 ∧ (9.9 - mu) / seXbar = -1.6 ∧ (10.1 - mu) / seXbar = 1.6 := by
  have h64 : Real.sqrt 64 = 8 := by
    rw [show (64 : ℝ) = 8 ^ 2 by norm_num]; exact Real.sqrt_sq (by norm_num)
  simp only [h64]
  norm_num

end MuestreoAleatorioProblemas
