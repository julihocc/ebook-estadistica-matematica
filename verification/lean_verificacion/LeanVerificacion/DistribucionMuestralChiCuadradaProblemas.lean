import Mathlib.Tactic

/-!
# Distribución muestral χ² — problemas

Formaliza `latex/distribucion_muestral_chi_cuadrada(p).tex`.
`prob:0d114e5` (Recordar), `prob:66b286b` (Comprender) y `prob:db05590`
(Evaluar) son conceptuales, sin cálculo numérico.
-/

namespace DistribucionMuestralChiCuadradaProblemas

/-- `prob:94c69e2` (Aplicar) — $\sigma_0^2=10,n=16,S^2=18.2$: el
estadístico es $15\cdot18.2/10=27.3>24.996\approx\chi^2_{15,0.95}$
(se rechaza $H_0$). El valor crítico en sí es Tier C, ver
`verification/scipy/distribucion_muestral_chi_cuadrada/numeric_checks.py`. -/
theorem prob_94c69e2 : (15 : ℝ) * 18.2 / 10 = 27.3 ∧ (27.3 : ℝ) > 24.996 := by norm_num

/-- `prob:b08d077` (Analizar) — sustituyendo $\alpha=\nu/2,\beta=2$ en las
fórmulas generales de la Gamma, $E(\chi^2_\nu)=\alpha\beta=\nu$ y
$\Var(\chi^2_\nu)=\alpha\beta^2=2\nu$, general para cualquier $\nu$. -/
theorem prob_b08d077 (nu : ℝ) : nu / 2 * 2 = nu ∧ nu / 2 * 2 ^ 2 = 2 * nu := by
  constructor <;> ring

/-- `prob:501e850` (Crear) — $\sigma_0^2=0.04,n=21,S^2=0.065$: el
estadístico es $20\cdot0.065/0.04=32.5>31.410\approx\chi^2_{20,0.95}$
(se rechaza $H_0$). Valor crítico Tier C, mismo script. -/
theorem prob_501e850 : (20 : ℝ) * 0.065 / 0.04 = 32.5 ∧ (32.5 : ℝ) > 31.410 := by norm_num

end DistribucionMuestralChiCuadradaProblemas
