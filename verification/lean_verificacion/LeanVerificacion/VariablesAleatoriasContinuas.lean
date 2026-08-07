import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-!
# Variables aleatorias continuas — teoría

Formaliza `latex/variables_aleatorias_continuas.tex`. **Primer capítulo que
necesita cálculo integral real** (`intervalIntegral`), no solo
`Finset.sum`/`tsum` — las densidades PDF/CDF viven en `ℝ`, no en soporte
discreto. A diferencia de capítulos anteriores, este archivo de teoría no
tiene bloques `solucion` con valores numéricos concretos — todos los
`ejemplo` son enunciados de problemas sin resolver inline en el propio
archivo (las respuestas están en figuras o se resuelven en clase); solo se
formalizan las dos identidades generales explícitas del texto,
`eq:2.7.3` y `eq:2.7.6`. El resto del capítulo (definiciones de PDF/CDF
conjunta, marginal, condicional, independencia) es aparato definicional,
no afirmaciones a verificar.
-/

namespace VariablesAleatoriasContinuas

open MeasureTheory intervalIntegral

/-- `eq:2.7.3` — $P(X=a)=0$ para una v.a. continua. El libro lo deriva
directamente de `eq:2.7.2` ($P(a<X<b)=\int_a^b f$) tomando $b=a$: la
integral sobre un intervalo degenerado a un punto es cero. General, para
cualquier densidad `f`. -/
theorem punto_probabilidad_cero (f : ℝ → ℝ) (a : ℝ) :
    (∫ x in a..a, f x) = 0 :=
  intervalIntegral.integral_same

/-- `eq:2.7.6` — $dF/dx=f(x)$: la derivada de la función de distribución es
la densidad. Formalizado con límite inferior fijo `a` (no `-∞`, fuera de
alcance de `intervalIntegral` estándar sin maquinaria adicional de
integrales impropias) — captura el contenido matemático central (el
Teorema Fundamental del Cálculo) sin necesitar ese caso límite. Para
cualquier `f` continua, $F(x):=\int_a^x f(t)\,dt$ tiene $F'(x)=f(x)$ en
todo punto. -/
theorem ftc_densidad {f : ℝ → ℝ} (hf : Continuous f) (a x : ℝ) :
    HasDerivAt (fun u => ∫ t in a..u, f t) (f x) x :=
  (hf.integral_hasStrictDerivAt a x).hasDerivAt

end VariablesAleatoriasContinuas
