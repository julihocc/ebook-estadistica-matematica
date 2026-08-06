import Mathlib.Tactic
import Mathlib.Probability.Moments.Variance
import Mathlib.Probability.Independence.Basic

/-!
# Capa de variables aleatorias / esperanza

Segunda capa axiomática del proyecto, construida sobre `MeasureTheory.Measure`
y `ProbabilityTheory.variance` de Mathlib (a diferencia de `Axiomas : Set Ω →
ℝ` en `FundamentosProbabilidad.lean`, que modela solo probabilidades de
eventos). Son dos objetos distintos con una división de trabajo: los
capítulos que razonan sobre eventos (fundamentos, técnicas de conteo,
probabilidad condicional, teorema de Bayes) usan `Axiomas`; los capítulos que
razonan sobre variables aleatorias y su esperanza/varianza (muestreo
aleatorio en adelante) usan esta capa. No se intenta unificarlas.

Objetivo: exactamente tres lemas generales que desbloquean los capítulos de
estimación puntual/inferencia, aplicados aquí a una muestra i.i.d.
`X : ι → Ω → ℝ` de tamaño `Fintype.card ι`:

* `esperanza_media_muestral` : `E[X̄] = μ`
* `varianza_media_muestral`  : `Var(X̄) = σ²/n`
* `esperanza_varianza_muestral` : `E[S²] = σ²` (varianza muestral insesgada,
  reutiliza `descomposicion_varianza` de `MuestreoAleatorioProblemas.lean`)
-/

open MeasureTheory
open scoped MeasureTheory ProbabilityTheory

namespace VariablesAleatorias

variable {Ω : Type*} [MeasurableSpace Ω] {μ : Measure Ω} [IsProbabilityMeasure μ]

/-- Muestra aleatoria simple i.i.d. de tamaño `Fintype.card ι`: variables
cuadrado-integrables, independientes por pares, con media común `m` y
varianza común `sigma2`. -/
structure MuestraIID {ι : Type*} [Fintype ι]
    (X : ι → Ω → ℝ) (μ : Measure Ω) (m sigma2 : ℝ) : Prop where
  memLp : ∀ i, MemLp (X i) 2 μ
  indep : (Finset.univ : Finset ι).toSet.Pairwise (fun i j => X i ⟂ᵢ[μ] X j)
  media : ∀ i, μ[X i] = m
  varianza : ∀ i, Var[X i; μ] = sigma2

variable {ι : Type*} [Fintype ι] {X : ι → Ω → ℝ} {m sigma2 : ℝ}

/-- Media muestral $\bar X = (1/n)\sum_i X_i$. -/
noncomputable def mediaMuestral (X : ι → Ω → ℝ) : Ω → ℝ :=
  fun ω => (∑ i, X i ω) / (Fintype.card ι : ℝ)

/-- Varianza muestral insesgada $S^2 = \frac{1}{n-1}\sum_i (X_i-\bar X)^2$. -/
noncomputable def varianzaMuestral (X : ι → Ω → ℝ) : Ω → ℝ :=
  fun ω => (∑ i, (X i ω - mediaMuestral X ω) ^ 2) / ((Fintype.card ι : ℝ) - 1)

theorem esperanza_media_muestral [Nonempty ι] (h : MuestraIID X μ m sigma2) :
    μ[mediaMuestral X] = m := by
  sorry

theorem varianza_media_muestral [Nonempty ι] (h : MuestraIID X μ m sigma2) :
    Var[mediaMuestral X; μ] = sigma2 / (Fintype.card ι : ℝ) := by
  sorry

theorem esperanza_varianza_muestral [Nonempty ι] (h : MuestraIID X μ m sigma2)
    (hn2 : 2 ≤ Fintype.card ι) :
    μ[varianzaMuestral X] = sigma2 := by
  sorry

end VariablesAleatorias
