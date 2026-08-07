import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Distribuciones de probabilidad de funciones de variable aleatoria — problemas

Formaliza `latex/distribuciones_funciones_variable_aleatoria(p).tex`.
`prob:0b1575d` (Recordar), `prob:a8b056e` (Comprender) y `prob:df21aa1`
(Evaluar) son conceptuales, sin cálculo numérico, no formalizados.
-/

namespace DistribucionesFuncionesVariableAleatoriaProblemas

open intervalIntegral Real

/-- `prob:4cdd21e` (Aplicar) — $X_1,X_2\sim U(0,1)$: la convolución en
$y\in(0,1)$ es $\int_0^y 1\,dx_1=y$ (densidad triangular). -/
theorem prob_4cdd21e (y : ℝ) : (∫ _x1 in (0 : ℝ)..y, (1 : ℝ)) = y := by
  rw [intervalIntegral.integral_const, smul_eq_mul]
  ring

/-- `prob:43a7344` (Analizar) — $X\sim N(0,1)$, $Y=|X|$: la suma de las
dos contribuciones simétricas da $\sqrt{2/\pi}\,e^{-y^2/2}$ (semi-normal). -/
theorem prob_43a7344 (y : ℝ) :
    (1 : ℝ) / Real.sqrt (2 * π) * Real.exp (-y ^ 2 / 2) +
        1 / Real.sqrt (2 * π) * Real.exp (-y ^ 2 / 2) =
      Real.sqrt (2 / π) * Real.exp (-y ^ 2 / 2) := by
  have hpi : (0 : ℝ) < π := Real.pi_pos
  have hpos : (0 : ℝ) < Real.sqrt (2 * π) := Real.sqrt_pos.mpr (by positivity)
  have key : Real.sqrt (2 / π) * Real.sqrt (2 * π) = 2 := by
    rw [← Real.sqrt_mul (by positivity : (0 : ℝ) ≤ 2 / π)]
    have heq : (2 / π) * (2 * π) = 4 := by field_simp; ring
    rw [heq, show (4 : ℝ) = 2 * 2 by norm_num, Real.sqrt_mul_self (by norm_num : (0 : ℝ) ≤ 2)]
  have hval : Real.sqrt (2 / π) = 2 / Real.sqrt (2 * π) := by
    rw [eq_div_iff hpos.ne']
    linarith [key]
  rw [hval]
  ring

/-- `prob:db5d952` (Crear) — $X_1\sim\mathrm{Exp}(2)$, $X_2\sim\mathrm{Exp}(3)$
independientes, $Y=X_1+X_2$: $f_Y(y)=6e^{-3y}(e^y-1)=6e^{-2y}-6e^{-3y}$. -/
theorem prob_db5d952 (y : ℝ) :
    (6 : ℝ) * Real.exp (-3 * y) * (∫ x1 in (0 : ℝ)..y, Real.exp x1)
      = 6 * Real.exp (-2 * y) - 6 * Real.exp (-3 * y) := by
  have hint : (∫ x1 in (0 : ℝ)..y, Real.exp x1) = Real.exp y - 1 := by
    rw [integral_exp, Real.exp_zero]
  rw [hint]
  have h2 : Real.exp (-3 * y) * Real.exp y = Real.exp (-2 * y) := by
    rw [← Real.exp_add]; ring_nf
  have hexpand : (6 : ℝ) * Real.exp (-3 * y) * (Real.exp y - 1)
      = 6 * (Real.exp (-3 * y) * Real.exp y) - 6 * Real.exp (-3 * y) := by ring
  rw [hexpand, h2]

end DistribucionesFuncionesVariableAleatoriaProblemas
