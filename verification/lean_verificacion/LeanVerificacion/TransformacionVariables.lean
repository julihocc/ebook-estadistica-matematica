import Mathlib.Tactic
import Mathlib.Analysis.Calculus.Deriv.Comp
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Inverse

/-!
# Transformación de variables — teoría

Formaliza `latex/transformacion_variables.tex`. `eq:3.2.1`/`eq:3.2.2`
($\mu_Y=a\mu_X+b$, $\sigma_Y^2=a^2\sigma_X^2$ para $Y=aX+b$) son
instancias directas de `EsperanzaMatematica.linealidad`/`var_escalar`
(capítulo 3), no se reproducen aquí. El Teorema de Unicidad y el
Teorema de Suma de `funcion_generadora_momentos` ya cubrieron la parte
Tier D de "depende de independencia"; aquí el resultado central
(`eq:3.2.3`, cambio de variable monótono) es literalmente la regla de la
cadena de Mathlib aplicada a $F_Y=F_X\circ g^{-1}$ — un caso donde la
"demostración pesada" del libro es, en Lean, una llamada de una línea a
`HasDerivAt.comp`.
-/

namespace TransformacionVariables

open Real

/-- `eq:3.2.1` (parte de la CDF) — para $Y=aX+b$ con $a>0$: la
equivalencia de orden que sustenta $F_Y(y)=F_X((y-b)/a)$, general. -/
theorem transformacion_afin_orden {a b : ℝ} (ha : 0 < a) (x y : ℝ) :
    a * x + b ≤ y ↔ x ≤ (y - b) / a := by
  rw [le_div_iff₀ ha]
  constructor <;> intro h <;> linarith

/-- `eq:3.2.3` — Teorema de cambio de variable (caso monótono
creciente): si $F_Y=F_X\circ g^{-1}$ y $g^{-1}$ tiene derivada
`gderiv` en $y$, con $F_X'=f_X$ en $g^{-1}(y)$, entonces
$F_Y'(y)=f_X(g^{-1}(y))\cdot g^{-1\prime}(y)$ — exactamente `eq:3.2.3`
sin el valor absoluto (que solo entra para $g$ decreciente, ver
`prob:fbf2d01`). Es la regla de la cadena aplicada directamente. -/
theorem cambio_variable_monotono {F_X f_X ginv : ℝ → ℝ} {gderiv : ℝ} (y : ℝ)
    (hFX : HasDerivAt F_X (f_X (ginv y)) (ginv y)) (hginv : HasDerivAt ginv gderiv y) :
    HasDerivAt (F_X ∘ ginv) (f_X (ginv y) * gderiv) y :=
  HasDerivAt.comp y hFX hginv

/-- `exmp:3.2.2` — $X\sim\mathrm{Exp}(1)$, $Y=e^X$: $f_Y(y)=e^{-\ln
y}\cdot(1/y)=1/y^2$ para $y>1$ (Pareto, $\alpha=1$). -/
theorem exmp_3_2_2_pareto (y : ℝ) (hy : 0 < y) :
    Real.exp (-Real.log y) * (1 / y) = 1 / y ^ 2 := by
  rw [Real.exp_neg, Real.exp_log hy]
  field_simp

/-- `exmp:3.2.4` — caso no monótono $Y=\sin X$, $X\sim U(0,2\pi)$: la
suma de las dos contribuciones simétricas
$\frac{1}{2\pi}\cdot\frac{1}{\sqrt{1-y^2}}$ da la densidad del
arcoseno $\frac{1}{\pi\sqrt{1-y^2}}$ (el hecho $d/dy\arcsin
y=1/\sqrt{1-y^2}$ en sí es estándar de Mathlib, `Real.hasDerivAt_arcsin`,
no se rederiva aquí). -/
theorem exmp_3_2_4_arcoseno (y : ℝ) (hy : Real.sqrt (1 - y ^ 2) ≠ 0) :
    2 * (1 / (2 * π) * (1 / Real.sqrt (1 - y ^ 2))) = 1 / (π * Real.sqrt (1 - y ^ 2)) := by
  have hpi : (π : ℝ) ≠ 0 := Real.pi_ne_zero
  field_simp

end TransformacionVariables
