import Mathlib.Tactic

/-!
# Distribución muestral χ² — teoría

Formaliza `latex/distribucion_muestral_chi_cuadrada.tex`. $E(\chi^2_\nu)=\nu$,
$\Var(\chi^2_\nu)=2\nu$ son consecuencias de los momentos generales de
Gamma (Tier D en `distribuciones_tipo_gamma`, no formalizados ahí como
teorema general — la sustitución concreta se verifica en
`DistribucionMuestralChiCuadradaProblemas.prob_b08d077`). El Teorema de
Fisher (`eq:5.3.2`, independencia de $\bar X$ y $S^2$ + $(n-1)S^2/\sigma^2
\sim\chi^2_{n-1}$) es Tier D — necesita una transformación ortogonal del
vector muestral (caso particular del teorema de Cochran), fuera de
alcance. Se formaliza el ejemplo numérico.
-/

namespace DistribucionMuestralChiCuadrada

/-- `exmp:5.3.1` — $\sigma^2=4,n=10,S^2=7.2$: el estadístico
$(n-1)S^2/\sigma^2=9\cdot7.2/4=16.2$, y $16.2<16.92\approx\chi^2_{9,0.95}$
(no se rechaza). El valor crítico $16.92$ en sí (Tier C, cuantil de
$\chi^2_9$) se confirma en
`verification/scipy/distribucion_muestral_chi_cuadrada/numeric_checks.py`. -/
theorem exmp_5_3_1 : (9 : ℝ) * 7.2 / 4 = 16.2 ∧ (16.2 : ℝ) < 16.92 ∧ (16.2 : ℝ) > 9 := by
  norm_num

end DistribucionMuestralChiCuadrada
