import Mathlib.Tactic

/-!
# Variables discretas y ciencia de datos — teoría

Formaliza `latex/variables_discretas_ciencia_datos.tex`. El capítulo es en
su mayoría prosa aplicada (una lista de usos de cada distribución en
ciencia de datos, sin afirmaciones matemáticas propias) más un único
ejemplo numérico (`exmp:2.10.18`) sobre detección de sobredispersión
comparando media y varianza muestral. No hay `teorema`/`definicion`
formales en este archivo — solo el `ejemplo`/`solucion` de abajo.
-/

namespace VariablesDiscretasCienciaDatos

/-- `exmp:2.10.18` — con $\bar x=4.2$ y $s^2=8.7$, la solución afirma
$s^2 \gg \bar x$ (sobredispersión), lo cual justifica preferir Binomial
Negativa sobre Poisson. Verificación Tier A: la desigualdad exacta que
sustenta la conclusión. -/
theorem exmp_2_10_18 : (8.7 : ℚ) > 4.2 := by norm_num

end VariablesDiscretasCienciaDatos
