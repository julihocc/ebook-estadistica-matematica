import Mathlib.Tactic

/-!
# Variables discretas y ciencia de datos — problemas

Formaliza `latex/variables_discretas_ciencia_datos(p).tex`. `prob:9b48fd0`
(Recordar) es puramente definicional ($D=s^2/\bar x$, valor de referencia
$D\approx1$ bajo equidispersión de Poisson) — no aporta ningún cálculo que
verificar, no se formaliza aparte. Los demás problemas (`prob:65ac238`,
`prob:486b84f`, `prob:395bc31`, `prob:a28b8e6`) son todos instancias del
mismo cociente de dispersión $D=s^2/\bar x$ sobre datos concretos — Tier A,
aritmética racional exacta.

**Tier D, no formalizado:** `prob:8fd9d7f` (Analizar) — demostración de que
la PMF de la Binomial Negativa converge a la de Poisson($\lambda$) cuando
$r\to\infty$ con $p=r/(r+\lambda)$ fijo. Es un teorema límite genuino
(`Filter.Tendsto` sobre una sucesión indexada por $r$), análogo al teorema
del límite de Poisson que Mathlib ya tiene para la Binomial
(`ProbabilityTheory.tendsto_choose_mul_pow_of_tendsto_mul_atTop` en
`Mathlib.Probability.Distributions.Poisson.PoissonLimitThm`), pero para la
parametrización Binomial Negativa, que Mathlib no cubre directamente. Un
intento futuro necesitaría: (1) un análogo de `isEquivalent_choose`
reindexado para $\binom{k+r-1}{k}\sim r^k/k!$ cuando $r\to\infty$ con $k$
fijo; (2) `Real.tendsto_one_add_pow_exp_of_tendsto` para
$(1+(-\lambda)/r)^r\to e^{-\lambda}$; (3) combinar ambos con
`Tendsto.mul` igual que en el archivo de Mathlib citado. Factible pero
sustancial — no se completó en este pase; los pasos aritméticos concretos
del resto del capítulo (arriba) sí se verificaron.
-/

namespace VariablesDiscretasCienciaDatosProblemas

/-- `prob:65ac238` — $n=500$, $\bar x=3.2$, $s^2=12.5$: el cociente de
dispersión $D=s^2/\bar x=125/32=3.90625$ redondea a $3.91$, como afirma el
libro. -/
theorem prob_65ac238 :
    (12.5 : ℚ) / 3.2 = 125 / 32 ∧ |(125 : ℚ) / 32 - 391 / 100| < 1 / 200 := by
  constructor <;> norm_num

/-- `prob:486b84f` — $n=100$, $\bar x=4.2$, $s^2=8.7$: el MLE de Poisson es
$\hat\lambda=\bar x=4.2$ (trivial), y $D=s^2/\bar x=8.7/4.2\approx2.07$
redondea correctamente. -/
theorem prob_486b84f :
    (4.2 : ℚ) = 4.2 ∧ |(8.7 : ℚ) / 4.2 - 207 / 100| < 1 / 200 := by
  constructor <;> norm_num

/-- `prob:395bc31` — $n=200$, $\bar x=8.5$, $s^2=9.8$: el cociente de
dispersión $D=s^2/\bar x=9.8/8.5\approx1.15$ redondea correctamente (el
libro no deriva $\hat r\approx55.6$ en Lean — es un dato dado del ajuste
por máxima verosimilitud, no una cantidad recuperable de $\bar x,s^2$ por
sí sola). -/
theorem prob_395bc31 : |(9.8 : ℚ) / 8.5 - 115 / 100| < 1 / 200 := by norm_num

/-- `prob:a28b8e6` — ejemplo ilustrativo de la solución propuesta: $n=300$,
$\bar x=2.1$, $s^2=6.8$: $D=s^2/\bar x=6.8/2.1\approx3.24$ redondea
correctamente. -/
theorem prob_a28b8e6 : |(6.8 : ℚ) / 2.1 - 324 / 100| < 1 / 200 := by norm_num

end VariablesDiscretasCienciaDatosProblemas
