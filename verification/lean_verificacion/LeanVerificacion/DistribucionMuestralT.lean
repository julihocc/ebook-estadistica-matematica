import Mathlib.Tactic

/-!
# Distribución muestral t — teoría

Formaliza `latex/distribucion_muestral_t.tex`. La definición de $t_\nu$
como cociente $Z/\sqrt{\chi^2_\nu/\nu}$, su densidad, y `eq:5.4.1`
(intervalo de confianza) son Tier D (necesitan la maquinaria de
`distribucion_muestral_chi_cuadrada`, ya Tier D, más el cociente de
variables aleatorias independientes). Los cuantiles de $t_\nu$ en sí son
Tier C (sin forma cerrada elemental). Se formaliza el ejemplo numérico.
-/

namespace DistribucionMuestralT

/-- `exmp:5.4.1` — $\bar X=48.5,S=3.2,n=9$: $\mathrm{SE}=S/\sqrt9=3.2/3$,
y el margen $t_{8,0.025}\cdot\mathrm{SE}\approx2.306\cdot(3.2/3)\approx2.46$
da el IC $[46.04,50.96]$; comparado con el margen (más angosto e
incorrecto para $\sigma$ desconocida) usando $z_{0.025}=1.96$, que da
$\approx2.09$ y $[46.41,50.59]$. Los cuantiles $t_{8,0.025}\approx2.306$ y
$z_{0.025}=1.96$ en sí son Tier C, confirmados en
`verification/scipy/distribucion_muestral_t/numeric_checks.py`. -/
theorem exmp_5_4_1 :
    (3.2 : ℝ) / 3 = 32 / 30 ∧ |(2.306 : ℝ) * (3.2 / 3) - 2.46| < 5e-3 ∧
      (48.5 : ℝ) + 2.46 = 50.96 ∧ (48.5 : ℝ) - 2.46 = 46.04 ∧
      |(1.96 : ℝ) * (3.2 / 3) - 2.09| < 5e-3 := by
  norm_num

end DistribucionMuestralT
