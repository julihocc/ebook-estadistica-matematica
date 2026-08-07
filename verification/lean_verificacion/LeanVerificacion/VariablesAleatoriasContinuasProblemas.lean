import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals

/-!
# Variables aleatorias continuas — problemas

Formaliza `latex/variables_aleatorias_continuas(p).tex`. **Primer capítulo
de la serie con integrales reales** (`intervalIntegral`, integrales
impropias sobre `Set.Ioi`) en vez de sumas finitas/series. `prob:19f62fd`
(Analizar), parte (a), es la definición operacional de LOTUS especializada
a $g(x)=x^2$ — tautológica, no se formaliza aparte (mismo patrón que
`prob:9dc367e` en `distribucion_poisson`).
-/

namespace VariablesAleatoriasContinuasProblemas

open MeasureTheory intervalIntegral Real

/-- `prob:14b3125` parte 1 — normalización de $f(x)=ce^{-x}$, $x\geq0$:
$\int_0^\infty e^{-x}dx=1$, luego $c=1$. -/
theorem prob_14b3125_normalizacion : (∫ x in Set.Ioi (0 : ℝ), Real.exp (-x)) = 1 := by
  rw [integral_exp_neg_Ioi_zero]

/-- `prob:14b3125` parte 2 — $P(1\le X\le3)=\int_1^3e^{-x}dx=e^{-1}-e^{-3}$,
forma exacta (evaluación decimal $\approx0.3181$: Tier C, ver
`verification/scipy/variables_aleatorias_continuas/prob_14b3125.py`). -/
theorem prob_14b3125_probabilidad :
    (∫ x in (1 : ℝ)..3, Real.exp (-x)) = Real.exp (-1) - Real.exp (-3) := by
  rw [intervalIntegral.integral_comp_neg (f := Real.exp), integral_exp]

/-- `prob:14b3125` parte 3 — CDF $F(x)=1-e^{-x}$ para $x\geq0$. -/
theorem prob_14b3125_cdf (x : ℝ) (_hx : 0 ≤ x) :
    (∫ t in (0 : ℝ)..x, Real.exp (-t)) = 1 - Real.exp (-x) := by
  rw [intervalIntegral.integral_comp_neg (f := Real.exp), integral_exp]
  simp

/-- `prob:287c45c` parte 1 — CDF $F(x)=x^2$ para $0\le x\le1$, con
$f(x)=2x$. -/
theorem prob_287c45c_cdf (x : ℝ) : (∫ t in (0 : ℝ)..x, 2 * t) = x ^ 2 := by
  rw [intervalIntegral.integral_const_mul (2 : ℝ) (fun t : ℝ => t), integral_id]
  ring

/-- `prob:287c45c` parte 3 — $P(0.3\le X\le0.7)=F(0.7)-F(0.3)=0.49-0.09=0.4$,
exacto en ℚ (vía la CDF general `prob_287c45c_cdf`). -/
theorem prob_287c45c_probabilidad :
    ((0.7 : ℝ) ^ 2 - (0.3 : ℝ) ^ 2 = 0.4) := by norm_num

/-- `prob:61a9dd8` parte 2 — el cuantil $q_{0.90}=5\ln10$ satisface
$1-e^{-0.2q_{0.90}}=0.9$ exactamente (evaluación decimal
$q_{0.90}\approx11.51$: Tier C). -/
theorem prob_61a9dd8_q90 : 1 - Real.exp (-(0.2 * (5 * Real.log 10))) = 0.9 := by
  have h : (0.2 : ℝ) * (5 * Real.log 10) = Real.log 10 := by ring
  rw [h, Real.exp_neg, Real.exp_log (by norm_num : (10 : ℝ) > 0)]
  norm_num

/-- `prob:61a9dd8` parte 3 — $t=-5\ln(0.05)$ satisface $1-e^{-0.2t}=0.95$
exactamente (evaluación decimal $t\approx14.98$: Tier C). -/
theorem prob_61a9dd8_t : 1 - Real.exp (-(0.2 * (-5 * Real.log 0.05))) = 0.95 := by
  have h : -(0.2 * (-5 * Real.log 0.05)) = Real.log 0.05 := by ring
  rw [h, Real.exp_log (by norm_num : (0.05 : ℝ) > 0)]
  norm_num

/-- `prob:8ec7e10` — estadístico KS: $\sqrt{50}\cdot0.18\approx1.273<1.358$,
no se rechaza $H_0$. Cota exacta, no aproximación decimal. -/
theorem prob_8ec7e10_ks : Real.sqrt 50 * 0.18 < 1.358 := by
  have h : Real.sqrt 50 < 1.358 / 0.18 := by
    rw [show (1.358 : ℝ) / 0.18 = 679 / 90 by norm_num, Real.sqrt_lt' (by norm_num)]
    norm_num
  nlinarith [h]

/-- `prob:19f62fd` parte (b) — $\mathrm{Var}(X)=\mathbb E[X^2]-(\mathbb
E[X])^2$ vía LOTUS, para cualquier densidad `f` con los momentos dados
como hipótesis (análogo continuo de `konig_huygens` de
`variables_aleatorias_discretas`, ahora sobre `MeasureTheory.integral` en
vez de `Finset.sum`). -/
theorem prob_19f62fd_varianza {f : ℝ → ℝ} {mu : ℝ} (hf : Integrable f)
    (hxf : Integrable fun x => x * f x) (hx2f : Integrable fun x => x ^ 2 * f x)
    (hnorm : (∫ x, f x) = 1) (hmu : (∫ x, x * f x) = mu) :
    (∫ x, (x - mu) ^ 2 * f x) = (∫ x, x ^ 2 * f x) - mu ^ 2 := by
  have hstep1 : Integrable fun x => x ^ 2 * f x - 2 * mu * (x * f x) :=
    hx2f.sub (hxf.const_mul (2 * mu))
  have hstep2 : Integrable fun x => mu ^ 2 * f x := hf.const_mul (mu ^ 2)
  have heq : (fun x => (x - mu) ^ 2 * f x)
      = fun x => x ^ 2 * f x - 2 * mu * (x * f x) + mu ^ 2 * f x := by
    funext x; ring
  rw [heq, integral_add hstep1 hstep2, integral_sub hx2f (hxf.const_mul (2 * mu)),
    MeasureTheory.integral_const_mul (2 * mu) (fun a => a * f a),
    MeasureTheory.integral_const_mul (mu ^ 2) f, hmu, hnorm]
  ring

/-- `prob:0d490fc` — normalización $\int_1^\infty x^{-2}dx=1$, luego $k=1$
para la densidad de cola pesada $f(x)=k/x^2$. -/
theorem prob_0d490fc_normalizacion :
    (∫ x in Set.Ioi (1 : ℝ), x ^ (-2 : ℝ)) = 1 := by
  rw [integral_Ioi_rpow_of_lt (by norm_num) (by norm_num)]
  norm_num

/-- `prob:0d490fc` — $P(1\le X\le2)=\int_1^2 x^{-2}dx=1/2$, exacto. -/
theorem prob_0d490fc_probabilidad :
    (∫ x in (1 : ℝ)..2, x ^ (-2 : ℤ)) = 1 / 2 := by
  rw [integral_zpow (Or.inr ⟨by norm_num, by norm_num⟩)]
  norm_num

end VariablesAleatoriasContinuasProblemas
