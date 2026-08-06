import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# Muestreo aleatorio — verificación

Formaliza la parte cuantitativa de `latex/muestreo_aleatorio.tex`. El único
`teorema` del archivo es el **Teorema del Límite Central** (TLC) en sí —
convergencia en distribución de la media muestral estandarizada a $N(0,1)$ —
que es un resultado analítico sustancial (requiere teoría de la medida, de
funciones características o convergencia débil) muy por encima del esfuerzo
razonable para este proyecto, y el libro tampoco da una demostración (solo
enuncia el resultado). **No formalizado — Tier D**, junto con las fórmulas
generales $E(\bar X)=\mu$, $\mathrm{Var}(\bar X)=\sigma^2/n$: estas
requerirían una capa de variables aleatorias reales con operador de esperanza
que el proyecto no ha construido (el marco `Axiomas` de
`FundamentosProbabilidad` solo modela probabilidades de eventos, no variables
aleatorias).

Lo que sí es aritmética exacta de racionales (Tier A) es el cálculo de $\mu$,
$\sigma^2$ y $\mathrm{Var}(\bar X)$ del ejemplo del dado. La estandarización a
puntajes $Z$ (que involucra $\sqrt{\mathrm{Var}(\bar X)}$) y la evaluación
final de la CDF normal ($P(-1.76<Z<1.76)\approx0.921$) se agrupan como Tier C
y se verifican numéricamente en
`verification/scipy/muestreo_aleatorio/tlc_dado.py`, ya que Mathlib no tiene
una versión computable de $\Phi$ y la raíz cuadrada exacta no es el punto de
interés matemático aquí (el libro mismo solo da valores redondeados, $\approx$).
-/

namespace MuestreoAleatorio

/-- Ejemplo ilustrativo (dado justo) — $\mu = (1+2+3+4+5+6)/6 = 3.5$ y
$\sigma^2 = \frac{\sum(i-3.5)^2}{6} = 35/12 \approx 2.917$, calculado como
suma exacta de los 6 términos (no solo citando el resultado). -/
theorem ejemplo_dado_mu_sigma2 :
    ((1 : ℚ) + 2 + 3 + 4 + 5 + 6) / 6 = 3.5 ∧
    (((1 : ℚ) - 3.5) ^ 2 + (2 - 3.5) ^ 2 + (3 - 3.5) ^ 2 + (4 - 3.5) ^ 2 +
      (5 - 3.5) ^ 2 + (6 - 3.5) ^ 2) / 6 = 35 / 12 := by
  norm_num

/-- Continuación del ejemplo — para $n=36$, $\mathrm{Var}(\bar X) = \sigma^2/36
= 35/432 \approx 0.081$. El denominador $n$ y $\sigma^2$ se ligan con `let` y
$\mathrm{Var}(\bar X)$ se calcula a partir de ellos, no se re-escribe. -/
theorem ejemplo_dado_var :
    let sigma2 : ℚ := 35 / 12
    let n : ℚ := 36
    let varXbar := sigma2 / n
    varXbar = 35 / 432 ∧ |(varXbar : ℝ) - 0.081| < 1e-3 := by
  norm_num

end MuestreoAleatorio
