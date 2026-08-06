import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Multinomial
import LeanVerificacion.DistribucionBinomial

/-!
# Distribución multinomial — problemas

Formaliza `latex/distribucion_multinomial(p).tex`. `prob:2499194` (Recordar)
es puro recordatorio de la fórmula de la PMF, ya cubierta en general por
`suma_normalizada_multinomial` de `DistribucionMultinomial.lean` — no se
repite. `prob:97df06e` es explicación en prosa, sin cálculo. `prob:277341a`
(la derivación de $\mathrm{Cov}(X_i,X_j)=-np_ip_j$ vía variables indicadoras)
y `prob:81748ff` (evaluación conceptual que depende de ese resultado)
requieren covarianza entre dos *componentes distintas* de un vector
aleatorio — no solo la varianza de una variable escalar vía su PMF (que sí
cubrimos con `Finset.sum` puro en capítulos previos), sino una noción real de
covarianza entre variables aleatorias correlacionadas, que el proyecto no ha
construido (ni siquiera la capa de `VariablesAleatorias.lean` la cubre — esa
modela solo muestras i.i.d. independientes, no vectores con covarianza
negativa por restricción de suma fija). **Tier D, no formalizados**, ver
"Infeasibles" en la bitácora.
-/

namespace DistribucionMultinomialProblemas

/-- Probabilidad de `prob:33bf5d2`: $\bm X\sim\mathrm{Mult}(100;0.45,0.35,0.20)$,
$P(X_1{=}50,X_2{=}30,X_3{=}20)=\frac{100!}{50!\,30!\,20!}(0.45)^{50}(0.35)^{30}
(0.20)^{20}$. El coeficiente se escribe como factoriales explícitos (mismo
patrón que `exmp_2_10_6`), no vía `Nat.multinomial` sobre un `Finset` (cuyo
cociente no se reduce a un literal con `norm_num`). -/
def P33bf5d2 : ℚ :=
  let p1 : ℚ := 9 / 20
  let p2 : ℚ := 7 / 20
  let p3 : ℚ := 1 / 5
  let coef : ℚ := (Nat.factorial 100 : ℚ) /
    ((Nat.factorial 50 : ℚ) * (Nat.factorial 30 : ℚ) * (Nat.factorial 20 : ℚ))
  coef * p1 ^ 50 * p2 ^ 30 * p3 ^ 20

/-- `prob:33bf5d2` (Aplicar) — **hallazgo: la respuesta del libro
($\approx4.32\times10^{-18}$) es incorrecta por un factor de ~$10^{42}$.**
El valor correcto (calculado aquí de forma independiente, cross-validado con
Python/`fractions.Fraction` antes de escribir la prueba) es
$P\approx0.0047908$ — sospechosamente cercano a $p_1^{50}\approx4.58\times
10^{-18}$ por sí solo, lo que sugiere que la solución del libro pudo haber
calculado solo una potencia aislada en vez de la expresión multinomial
completa. Se transcribe la afirmación del libro tal cual y se refuta
(`prob_33bf5d2_libro_incorrecto`), y por separado se confirma el valor
correcto (`prob_33bf5d2_valor_correcto`) — mismo patrón que la calibración
del método al inicio de esta bitácora. -/
theorem prob_33bf5d2_libro_incorrecto : ¬ |(P33bf5d2 : ℝ) - 4.32e-18| < 1e-3 := by
  simp only [P33bf5d2, not_lt]
  norm_num [Nat.factorial]

theorem prob_33bf5d2_valor_correcto : |(P33bf5d2 : ℝ) - 0.0047908| < 1e-6 := by
  simp only [P33bf5d2]
  norm_num [Nat.factorial]

/-- `prob:858a3a8` (Crear) — call center con $k=4$ categorías, $n=50$,
$p_1=0.4$: la marginal $X_1\sim\mathrm{Bin}(n,p_1)$ (propiedad conocida de la
multinomial, no se re-deriva aquí), así que $\mathbb E[X_1]=np_1=20$ y
$\mathrm{Var}(X_1)=np_1(1-p_1)=12$ se obtienen reutilizando directamente
`esperanza_binomial`/`varianza_binomial` de `DistribucionBinomial.lean` con
$N=50,p=0.4,q=0.6$ — validación cruzada entre capítulos, no una fórmula
nueva. -/
theorem prob_858a3a8 :
    ∑ x ∈ Finset.range (50 + 1), (x : ℝ) * ((50).choose x : ℝ) * (0.4 : ℝ) ^ x *
        (0.6 : ℝ) ^ (50 - x) = 20 ∧
      ∑ x ∈ Finset.range (50 + 1), ((x : ℝ) - (50 : ℕ) * 0.4) ^ 2 * ((50).choose x : ℝ) *
          (0.4 : ℝ) ^ x * (0.6 : ℝ) ^ (50 - x) = 12 := by
  constructor
  · have h := DistribucionBinomial.esperanza_binomial 50 0.4 0.6 (by norm_num)
    rw [h]; norm_num
  · have h := DistribucionBinomial.varianza_binomial 50 0.4 0.6 (by norm_num)
    rw [h]; norm_num

end DistribucionMultinomialProblemas
