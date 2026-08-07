import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Distribuciones de probabilidad de funciones de variable aleatoria — teoría

Formaliza `latex/distribuciones_funciones_variable_aleatoria.tex`.
`eq:3.2.5` (suma sobre preimágenes) y `eq:3.2.6` (integración sobre
superficie de nivel en varias variables) son definicionales/generales sin
un enunciado cerrado único que probar aisladamente — su contenido
concreto se verifica vía las instancias (`exmp:3.2.5` aquí,
`prob:4cdd21e`/`prob:43a7344`/`prob:db5d952` en problemas).
-/

namespace DistribucionesFuncionesVariableAleatoria

open intervalIntegral

/-- `exmp:3.2.5` — $X_1,X_2\sim\mathrm{Exp}(1)$ independientes, $Y=X_1+X_2$:
la integral sobre la recta de nivel es constante en $x_1$, dando
$f_Y(y)=y\,e^{-y}$ (Erlang/Gamma$(2,1)$), para cualquier $y$. -/
theorem exmp_3_2_5 (y : ℝ) : (∫ x1 in (0 : ℝ)..y, Real.exp (-(x1 + (y - x1)))) = y * Real.exp (-y) := by
  have heq : (fun x1 : ℝ => Real.exp (-(x1 + (y - x1)))) = fun _ => Real.exp (-y) := by
    funext x1; ring_nf
  rw [heq, intervalIntegral.integral_const, smul_eq_mul]
  ring

end DistribucionesFuncionesVariableAleatoria
