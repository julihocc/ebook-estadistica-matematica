import Mathlib.Tactic

/-!
# Distribución normal — teoría

Formaliza `latex/distribucion_normal.tex`. **Tier D confirmado por test de
humo:** `Mathlib.Probability.Distributions.Gaussian.Real` (que tiene
`gaussianPDFReal`/`integral_gaussianPDFReal_eq_one`, exactamente la
normalización que necesitaría una demostración completa de la función
generadora de momentos) resultó bloqueado por el mismo problema de
longitud de ruta de Windows documentado para `VariablesAleatorias.lean` y
`Mathlib.Probability.Independence.Integration` — pero además esta vez
también bloqueó `Mathlib.MeasureTheory.Integral.IntervalIntegral.LebesgueDifferentiationThm`,
una dependencia transitiva nueva no vista en capítulos anteriores. La
integral gaussiana "cruda" (`Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral`,
`integral_gaussian (b) : ∫ x, exp(-b*x²) = √(π/b)`) SÍ se pudo importar
sin problema, pero completar la demostración de la FGM con ella requeriría
además un lema de invarianza por traslación de `MeasureTheory.integral`
sobre `ℝ` que no se localizó en un tiempo razonable de búsqueda — se deja
como Tier D/C explícito (razón documentada, no un fallo silencioso), no
como una limitación matemática. Sí se formalizan las dos piezas
algebraicas puras que no requieren evaluar ninguna integral: la identidad
de estandarización de densidades y la identidad de completar-el-cuadrado
que sustenta la demostración de la FGM.
-/

namespace DistribucionNormal

open Real

/-- `eq:2.8.4`/`eq:2.8.5` — la estandarización $Z=(X-\mu)/\sigma$ conecta
las densidades: $\sigma\cdot f(\mu+\sigma z)=\varphi(z)$ (el factor
$\sigma$ es el jacobiano de $x=\mu+\sigma z$), para cualquier $\mu,\sigma>0$. -/
theorem estandarizacion_densidad (mu sigma : ℝ) (hsigma : 0 < sigma) (z : ℝ) :
    sigma * (1 / (sigma * Real.sqrt (2 * π)) *
        Real.exp (-(mu + sigma * z - mu) ^ 2 / (2 * sigma ^ 2)))
      = 1 / Real.sqrt (2 * π) * Real.exp (-z ^ 2 / 2) := by
  have hs : sigma ≠ 0 := hsigma.ne'
  have hexp : (-(mu + sigma * z - mu) ^ 2 / (2 * sigma ^ 2) : ℝ) = -z ^ 2 / 2 := by
    field_simp
    ring
  rw [hexp]
  field_simp

/-- `prob:dd1e027` — el paso de "completar el cuadrado" central a la
demostración de la FGM $M_X(t)=e^{\mu t+\sigma^2t^2/2}$: la identidad
algebraica exacta que usa el libro, general para cualquier $\mu,\sigma\ne
0,t,x$. **No formalizado en este pase el cierre completo de la FGM**
(necesitaría evaluar $\int\exp(-(x-c)^2/(2\sigma^2))dx=\sigma\sqrt{2\pi}$
para $c=\mu+\sigma^2t$, bloqueado en este worktree — ver nota del
archivo); esta identidad es la pieza algebraica que sí se verifica. -/
theorem mgf_exponente (mu sigma t x : ℝ) (hsigma : sigma ≠ 0) :
    t * x - (x - mu) ^ 2 / (2 * sigma ^ 2) =
      (mu * t + sigma ^ 2 * t ^ 2 / 2) - (x - (mu + sigma ^ 2 * t)) ^ 2 / (2 * sigma ^ 2) := by
  field_simp
  ring

end DistribucionNormal
