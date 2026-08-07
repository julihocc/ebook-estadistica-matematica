import Mathlib.Tactic

/-!
# Distribución normal — problemas

Formaliza `latex/distribucion_normal(p).tex`. `prob:6f58870` (Recordar),
`prob:74e7285` (Comprender) y `prob:96d8f57` (Evaluar) son puramente
conceptuales — sin cálculo numérico que verificar, no formalizados.
`prob:dd1e027` (Analizar) reutiliza `mgf_exponente` de
`DistribucionNormal.lean`, no se repite aquí. Las evaluaciones
decimales que necesitan la CDF normal estándar $\Phi$ (irracional) son
Tier C, ver `verification/scipy/distribucion_normal/`.
-/

namespace DistribucionNormalProblemas

/-- `prob:48f2103` (Aplicar) — $X\sim N(170,100)$: estandarización exacta
$Z=(185-170)/10=1.5$ y $Z=(160-170)/10=-1$, $Z=(180-170)/10=1$ (los
valores de $\Phi$ mismos son Tier C). -/
theorem prob_48f2103_estandarizacion :
    ((185 : ℝ) - 170) / 10 = 1.5 ∧ ((160 : ℝ) - 170) / 10 = -1 ∧ ((180 : ℝ) - 170) / 10 = 1 := by
  norm_num

/-- `prob:1c4fda2` (Crear) — $X\sim N(0.150,0.0004)$: $Z=(0.100-0.150)/0.02=-2.5$
exacto ($\Phi(-2.5)\approx0.0062$ es Tier C). -/
theorem prob_1c4fda2_estandarizacion : ((0.100 : ℝ) - 0.150) / 0.02 = -2.5 := by norm_num

end DistribucionNormalProblemas
