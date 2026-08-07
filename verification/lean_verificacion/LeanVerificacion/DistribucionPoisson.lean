import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Normed.Algebra.Exponential
import Mathlib.Analysis.SpecialFunctions.Exponential

/-!
# Distribución Poisson — verificación

Formaliza la parte cuantitativa de `latex/distribucion_poisson.tex` (la
sección sobre distribución normal, relación binomial-normal, percentiles y
los ejemplos de "Problemas Resueltos" no dan valores numéricos explícitos en
el propio texto — solo referencian scripts de Python sin mostrar el
resultado inline — así que no hay una afirmación concreta del libro que
verificar ahí; se documenta como observación, no como Tier D). La
normalización de la PMF ($\sum f(n)=1$) se prueba en general — Tier B — vía
la serie de la exponencial de Mathlib (`NormedSpace.expSeries_div_hasSum_exp`),
con el mismo estilo que usa internamente
`Mathlib.Probability.Distributions.Poisson.Basic.hasSum_one_poissonMeasure`
(que solo cubre `r:ℝ≥0`; aquí se prueba para `lam:ℝ` general). $\mu=\sigma^2=
\lambda$ quedan **Tier D**: requerirían además un lema de desplazamiento de
`tsum` (`∑f(n) = f(0) + ∑f(n+1)`) combinado con la serie exponencial —
identificado en Mathlib como `Summable.tsum_eq_zero_add`, pero conectarlo
con la sumabilidad de $n\cdot f(n)$ no se completó en este pase por tiempo.
-/

namespace DistribucionPoisson

/-- `eq:2.10.7` — normalización de la PMF de Poisson: $\sum_{n=0}^\infty
e^{-\lambda}\lambda^n/n!=1$, para $\lambda$ real arbitrario (no solo
$\lambda\ge0$, aunque el libro solo usa $\lambda>0$) — vía la serie de la
exponencial de Mathlib, mismo estilo que
`ProbabilityTheory.hasSum_one_poissonMeasure`. -/
theorem suma_normalizada_poisson (lam : ℝ) :
    ∑' n : ℕ, Real.exp (-lam) * lam ^ n / (Nat.factorial n : ℝ) = 1 := by
  have h := (NormedSpace.expSeries_div_hasSum_exp lam).mul_left (Real.exp (-lam))
  have heq : (fun n : ℕ => Real.exp (-lam) * (lam ^ n / (Nat.factorial n : ℝ))) =
      fun n : ℕ => Real.exp (-lam) * lam ^ n / (Nat.factorial n : ℝ) := by
    funext n; ring
  rw [heq] at h
  rw [h.tsum_eq, ← Real.exp_eq_exp_ℝ, ← Real.exp_add]
  simp

/-- `exmp:2.10.5` — hospital con $\lambda=5$: $P(X\le3)=e^{-5}(1+5+12.5+
20.8\overline3)$. La suma finita `1+5+25/2+125/6` se verifica exactamente
(Tier A); la evaluación decimal final (`\approx0.265`) requiere $e^{-5}$,
irracional — **Tier C**, ver
`verification/scipy/distribucion_poisson/exmp_2_10_5.py`. -/
theorem exmp_2_10_5_suma_finita :
    (1 : ℝ) + 5 + 25 / 2 + 125 / 6 = 39 + 1 / 3 := by norm_num

end DistribucionPoisson
