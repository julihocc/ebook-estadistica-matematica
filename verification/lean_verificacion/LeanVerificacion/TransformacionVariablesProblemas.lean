import Mathlib.Tactic

/-!
# Transformación de variables — problemas

Formaliza `latex/transformacion_variables(p).tex`. `prob:d3727e9`
(Recordar) y `prob:fbf2d01` (Comprender) son conceptuales, sin cálculo
numérico, no formalizados.
-/

namespace TransformacionVariablesProblemas

/-- `prob:d795060` (Aplicar) — $X\sim N(5,4)$, $Y=3X-2$:
$\mu_Y=3(5)-2=13$, $\sigma_Y^2=3^2(4)=36$. -/
theorem prob_d795060 : (3 : ℝ) * 5 - 2 = 13 ∧ (3 : ℝ) ^ 2 * 4 = 36 := by norm_num

/-- `prob:182603c` (Analizar) — $X\sim\mathrm{Exp}(\lambda)$, $Y=\sqrt
X$: $f_Y(y)=f_X(y^2)\cdot2y=2\lambda y\,e^{-\lambda y^2}$, general
(Weibull con $\beta=2,\eta=1/\sqrt\lambda$). -/
theorem prob_182603c (lam y : ℝ) :
    lam * Real.exp (-lam * y ^ 2) * (2 * y) = 2 * lam * y * Real.exp (-lam * y ^ 2) := by ring

/-- `prob:5ce800e` (Evaluar) — corrección del caso no monótono $Y=X^2$
para $X\sim U(-1,1)$: la suma de las dos raíces da $f_Y(y)=1/(2\sqrt
y)$, el doble del resultado incompleto ($1/(4\sqrt y)$) que obtendría
usar solo una raíz. -/
theorem prob_5ce800e (y : ℝ) (_hy : 0 < y) :
    (1 : ℝ) / 2 * (1 / (2 * Real.sqrt y)) + 1 / 2 * (1 / (2 * Real.sqrt y)) = 1 / (2 * Real.sqrt y) := by
  ring

/-- `prob:12a4921` (Crear) — $X\sim U(0,1)$, $Y=-\ln X$: $f_Y(y)=e^{-y}$
para $y>0$ ($Y\sim\mathrm{Exp}(1)$, la transformada inversa). -/
theorem prob_12a4921 (y : ℝ) : (1 : ℝ) * |(-Real.exp (-y))| = Real.exp (-y) := by
  rw [abs_neg, abs_of_pos (Real.exp_pos _)]
  ring

end TransformacionVariablesProblemas
