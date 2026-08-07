import Mathlib.Tactic

/-!
# Distribución muestral F — teoría

Formaliza `latex/distribucion_muestral_f.tex`. La definición, densidad,
momentos ($E(F)$, $\Var(F)$), y los teoremas de ANOVA/IC para
$\sigma_1^2/\sigma_2^2$ son Tier D (dependen de la maquinaria ya Tier D
de `distribucion_muestral_chi_cuadrada`/`distribucion_muestral_t`, más
razones de variables aleatorias independientes). Se formalizan la
identidad algebraica de reciprocidad ($1/F_{d_1,d_2}\sim F_{d_2,d_1}$) y
el ejemplo numérico de ANOVA, donde se encontraron dos errores
aritméticos confirmados.
-/

namespace DistribucionMuestralF

/-- Propiedad de reciprocidad: si $F=(\chi^2_{d_1}/d_1)/(\chi^2_{d_2}/d_2)$,
entonces $1/F=(\chi^2_{d_2}/d_2)/(\chi^2_{d_1}/d_1)$ — identidad algebraica
pura, general para cualquier $a,b,d_1,d_2\ne0$. -/
theorem reciprocidad_F (a b d1 d2 : ℝ) (ha : a ≠ 0) (hb : b ≠ 0) (hd1 : d1 ≠ 0) (hd2 : d2 ≠ 0) :
    1 / ((a / d1) / (b / d2)) = (b / d2) / (a / d1) := by
  field_simp

/-- **`exmp:3.2.6` — hallazgo confirmado, dos errores aritméticos.**
(1) El libro afirma $\mathrm{SC}_{\text{trat}}=5(86.6-86.4)^2+5(81.0-86.4)^2+5(91.6-86.4)^2=290.0$,
pero el valor exacto es $281.2$. (2) El libro afirma que la suma de
cuadrados intra-grupo del Método C es $23.2$, pero el valor exacto
(con los mismos datos $\{92,95,88,90,93\}$ y media $91.6$ que el libro
usa correctamente) es $29.2$. Ambos errores se propagan:
$\mathrm{SC}_{\text{error}}=119.2+40.0+29.2=188.4$ (no $182.4$), y el
estadístico $F=(281.2/2)/(188.4/12)\approx8.955$ (no $9.54$). La
conclusión cualitativa del libro (rechazar $H_0$) sobrevive por
casualidad — ambos valores de $F$ superan el crítico $3.89$ — pero los
valores intermedios están mal. Verificado con `fractions.Fraction` en
Python antes de escribir esta prueba. Presente idéntico en
`en_distribucion_muestral_f.tex` (mismos $290.0$, $23.2$, $182.4$,
$9.54$) — confirma fuente compartida. -/
theorem exmp_3_2_6_hallazgo :
    (5 : ℝ) * (86.6 - 86.4) ^ 2 + 5 * (81.0 - 86.4) ^ 2 + 5 * (91.6 - 86.4) ^ 2 = 281.2 ∧
      ¬ (5 : ℝ) * (86.6 - 86.4) ^ 2 + 5 * (81.0 - 86.4) ^ 2 + 5 * (91.6 - 86.4) ^ 2 = 290.0 ∧
      ((92 : ℝ) - 91.6) ^ 2 + (95 - 91.6) ^ 2 + (88 - 91.6) ^ 2 + (90 - 91.6) ^ 2 + (93 - 91.6) ^ 2 = 29.2 ∧
      ¬ ((92 : ℝ) - 91.6) ^ 2 + (95 - 91.6) ^ 2 + (88 - 91.6) ^ 2 + (90 - 91.6) ^ 2 + (93 - 91.6) ^ 2 = 23.2 := by
  norm_num

/-- La cascada corregida: $\mathrm{SC}_{\text{error}}=119.2+40.0+29.2=188.4$
(el libro dice $182.4$), y el estadístico $F$ correcto es
$(281.2/2)/(188.4/12)$; se verifica que sigue superando el valor crítico
$3.89$ (la conclusión cualitativa del libro es correcta pese a los
errores aritméticos). -/
theorem exmp_3_2_6_f_corregido :
    (119.2 : ℝ) + 40.0 + 29.2 = 188.4 ∧ (281.2 / 2 : ℝ) / (188.4 / 12) > 3.89 := by
  norm_num

end DistribucionMuestralF
