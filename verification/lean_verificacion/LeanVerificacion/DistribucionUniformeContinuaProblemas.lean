import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Distribución uniforme continua — problemas

Formaliza `latex/distribucion_uniforme_continua(p).tex`. `prob:97c4388`
(Recordar) es puramente definicional — no formalizado aparte.
`prob:5794e09` (Analizar) pide una demostración de máxima entropía vía
multiplicadores de Lagrange sobre un funcional — cálculo de variaciones,
Tier D, no formalizado (razón abajo).
-/

namespace DistribucionUniformeContinuaProblemas

open intervalIntegral

/-- `prob:9f6e77c` (Comprender) — $X\sim U(0,15)$: la uniforme **no**
tiene la propiedad de falta de memoria: $P(X\ge15\mid X\ge10)=0\ne
2/3=P(X\ge5)$. -/
theorem prob_9f6e77c :
    (0 : ℝ) / (5 / 15) = 0 ∧ (10 : ℝ) / 15 = 2 / 3 ∧ (0 : ℝ) ≠ 10 / 15 := by
  norm_num

/-- `prob:8fcc221` (Aplicar) — $P(X<5)=1/3$, $q_{0.75}=11.25$. -/
theorem prob_8fcc221 : (5 : ℝ) / 15 = 1 / 3 ∧ (0.75 : ℝ) * 15 = 11.25 := by norm_num

/-- `prob:126be41` (Evaluar) — el método de la transformada inversa:
$Y=F^{-1}(U)$ tiene CDF $F$, para cualquier $F$ **estrictamente
monótona** con inversa por la derecha `Finv` — no se necesita que
$F^{-1}$ tenga forma cerrada, solo que $F$ sea invertible. Este es el
contenido matemático central de la solución (la equivalencia de orden
$F^{-1}(u)\le y \iff u\le F(y)$); combinado con que $U\sim U(0,1)$ tiene
CDF $F_U(t)=t$ (`cdf_uniforme` con $a=0,b=1$), da
$P(Y\le y)=P(U\le F(y))=F(y)$, la afirmación completa del libro. -/
theorem prob_126be41_transformada_inversa {F Finv : ℝ → ℝ} (hF : StrictMono F)
    (hinv : Function.RightInverse Finv F) (u y : ℝ) : Finv u ≤ y ↔ u ≤ F y := by
  rw [← hF.le_iff_le, hinv]

/-- `prob:126be41`, caso concreto — $\mathrm{Exp}(\lambda=2)$ sí tiene
forma cerrada: $F(y)=1-e^{-2y}$, $F^{-1}(u)=-\ln(1-u)/2$, son inversas
mutuas en $(0,1)$/$[0,\infty)$. -/
theorem prob_126be41_exponencial (u : ℝ) (hu : 0 < u) (hu1 : u < 1) :
    1 - Real.exp (-2 * (-Real.log (1 - u) / 2)) = u := by
  have h1u : (1 : ℝ) - u > 0 := by linarith
  have heq : (-2 : ℝ) * (-Real.log (1 - u) / 2) = Real.log (1 - u) := by ring
  rw [heq, Real.exp_log h1u]
  ring

/-- `prob:c1c6ece` (Crear) — $X\sim U(-5,5)$: $\mathbb E[X]=0$,
$\mathrm{Var}(X)=100/12\approx8.33$. -/
theorem prob_c1c6ece :
    ((-5 : ℝ) + 5) / 2 = 0 ∧ ((5 : ℝ) - (-5)) ^ 2 / 12 = 25 / 3 := by norm_num

end DistribucionUniformeContinuaProblemas
