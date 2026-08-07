import Mathlib.Tactic

/-!
# Distribuciones de tipo gamma — teoría

Formaliza `latex/distribuciones_tipo_gamma.tex`. Capítulo muy amplio
(función gamma, Gamma, Exponencial como caso particular, chi-cuadrada,
suma de gammas, Beta, Weibull) con mucho contenido puramente
definicional/enumerativo (propiedades de $\Gamma$, identificaciones de
casos particulares) y varios resultados analíticos genuinamente pesados:

**Tier D, no formalizado (razones):**
- Propiedades de la función gamma ($\Gamma(1)=1$, $\Gamma(\alpha+1)=\alpha\Gamma(\alpha)$,
  $\Gamma(n)=(n-1)!$, $\Gamma(1/2)=\sqrt\pi$) — Mathlib SÍ tiene
  `Real.Gamma`/`Real.Gamma_add_one`/`Real.Gamma_nat_eq_factorial`, pero
  dado el patrón de esta sesión (`Mathlib.Probability.Distributions.Gaussian`
  bloqueado por MAX_PATH en `distribucion_normal`), no se intentó
  encadenar el paquete completo en este pase — factible, no prioritario
  frente a los valores numéricos concretos del capítulo.
- La demostración de que $\mathrm{Gamma}(\alpha,\beta)$ tiene media
  $\alpha\beta$ y varianza $\alpha\beta^2$ (necesita la función gamma vía
  integrales impropias con cambio de variable).
- `eq:2.8.10` — el teorema de suma de gammas independientes con la misma
  escala (necesita convolución de densidades, un resultado genuinamente
  pesado).
- Media/varianza de la distribución Weibull (involucran $\Gamma(1+1/\beta)$,
  $\Gamma(1+2/\beta)$ — la función gamma evaluada en puntos no enteros).

Se formalizan las identidades algebraicas exactas y los valores numéricos
concretos de los ejemplos, que es donde vive el riesgo real de errores de
transcripción del libro.
-/

namespace DistribucionesTipoGamma

/-- `exmp:2.8.3` — $T\sim\mathrm{Gamma}(3,1/3)$ (Erlang de 3 llamadas a
tasa $\lambda=3$): $P(T>1.5)=e^{-4.5}(1+4.5+20.25/2)$, con la suma
interior exacta $=15.625$. -/
theorem exmp_2_8_3_suma : (1 : ℝ) + 4.5 + 20.25 / 2 = 15.625 := by norm_num

/-- `exmp:2.8.7` — $X\sim\mathrm{Beta}(2,8)$: $\mathbb E[X]=0.2$,
$\mathrm{Var}(X)=16/1100\approx0.0145$. -/
theorem exmp_2_8_7 :
    (2 : ℝ) / (2 + 8) = 0.2 ∧ |(16 : ℝ) / 1100 - 0.0145| < 1e-4 := by
  constructor <;> norm_num

/-- `exmp:2.8.8` — $T\sim\mathrm{Weibull}(\beta=2,\eta=5)$: el exponente
de la CDF en $t=3$ es $(3/5)^2=0.36$ exacto (la evaluación decimal
$1-e^{-0.36}\approx0.3023$ es Tier C). La tasa de riesgo $h(t)=(2/5)(t/5)$
es creciente en $t$ (coeficiente positivo), consistente con $\beta=2>1$. -/
theorem exmp_2_8_8_exponente : ((3 : ℝ) / 5) ^ 2 = 0.36 := by norm_num

end DistribucionesTipoGamma
