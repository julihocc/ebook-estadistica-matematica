import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Distribución uniforme continua — teoría

Formaliza `latex/distribucion_uniforme_continua.tex`. Capítulo corto:
PDF/CDF de $U(a,b)$ y sus dos momentos, con un ejemplo numérico
(`exmp:2.8.1`). Todo Tier A/B — sin `MeasureTheory.integral` sobre un
espacio de probabilidad, solo `intervalIntegral` con la densidad
constante $1/(b-a)$.
-/

namespace DistribucionUniformeContinua

open intervalIntegral

/-- `eq:2.8.2` — CDF de $U(a,b)$: $F(x)=(x-a)/(b-a)$ para $a\le x\le b$,
general para cualquier $a<b$. -/
theorem cdf_uniforme {a b : ℝ} (hab : a < b) (x : ℝ) :
    (∫ t in a..x, (1 : ℝ) / (b - a)) = (x - a) / (b - a) := by
  rw [intervalIntegral.integral_const, smul_eq_mul]
  ring

/-- Propiedades de $U(a,b)$: $\mu_X=(a+b)/2$, general para $a<b$. -/
theorem media_uniforme {a b : ℝ} (hab : a < b) :
    (∫ x in a..b, x * (1 / (b - a))) = (a + b) / 2 := by
  have hba : b - a ≠ 0 := sub_ne_zero.mpr hab.ne'
  have heq : (fun x : ℝ => x * (1 / (b - a))) = fun x => (1 / (b - a) : ℝ) * x := by
    funext x; ring
  rw [heq, intervalIntegral.integral_const_mul (1 / (b - a) : ℝ) (fun x : ℝ => x), integral_id]
  field_simp
  ring

/-- Propiedades de $U(a,b)$: $\sigma_X^2=(b-a)^2/12$, general para $a<b$.
Se factoriza la constante $1/(b-a)$ primero, dejando una integral
polinomial pura (sin denominador $b-a$ adentro), que se calcula con
`integral_pow`/`integral_id`/`integral_const` estándar. -/
theorem varianza_uniforme {a b : ℝ} (hab : a < b) :
    (∫ x in a..b, (x - (a + b) / 2) ^ 2 * (1 / (b - a))) = (b - a) ^ 2 / 12 := by
  have hba : b - a ≠ 0 := sub_ne_zero.mpr hab.ne'
  set mu := (a + b) / 2 with hmu
  have heq1 : (fun x : ℝ => (x - mu) ^ 2 * (1 / (b - a))) = fun x => (1 / (b - a) : ℝ) * (x - mu) ^ 2 := by
    funext x; ring
  rw [heq1, intervalIntegral.integral_const_mul (1 / (b - a) : ℝ) (fun x => (x - mu) ^ 2)]
  have heq2 : (fun x : ℝ => (x - mu) ^ 2) = fun x => x ^ 2 - 2 * mu * x + mu ^ 2 := by
    funext x; ring
  rw [heq2]
  have hc1 : Continuous fun x : ℝ => x ^ 2 - 2 * mu * x := (continuous_pow 2).sub (continuous_id'.const_mul (2 * mu))
  have hc2 : Continuous fun _ : ℝ => mu ^ 2 := continuous_const
  rw [intervalIntegral.integral_add (hc1.intervalIntegrable a b) (hc2.intervalIntegrable a b),
    intervalIntegral.integral_sub ((continuous_pow 2).intervalIntegrable a b)
      ((continuous_id'.const_mul (2 * mu) : Continuous fun x : ℝ => 2 * mu * x).intervalIntegrable a b),
    intervalIntegral.integral_const_mul (2 * mu : ℝ) (fun x : ℝ => x), integral_pow, integral_id,
    intervalIntegral.integral_const]
  field_simp
  ring

/-- `exmp:2.8.1` — tiempo de espera $X\sim U(0,15)$: $P(X<5)=1/3$. -/
theorem exmp_2_8_1_probabilidad : (∫ x in (0 : ℝ)..5, (1 : ℝ) / 15) = 1 / 3 := by
  simp [intervalIntegral.integral_const]
  norm_num

/-- `exmp:2.8.1` — $E(X)=(0+15)/2=7.5$. -/
theorem exmp_2_8_1_esperanza : ((0 : ℝ) + 15) / 2 = 7.5 := by norm_num

end DistribucionUniformeContinua
