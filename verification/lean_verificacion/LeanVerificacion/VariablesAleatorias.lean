import Mathlib.Tactic
import Mathlib.Probability.Moments.Variance
import Mathlib.Probability.Independence.Basic
import LeanVerificacion.MuestreoAleatorioProblemas

/-!
# Capa de variables aleatorias / esperanza — PROBADA, pero excluida del build
por defecto de este worktree (razón: longitud de ruta de Windows, no el
contenido matemático)

**Las tres afirmaciones de abajo SÍ elaboran/type-check — están probadas,
sin `sorry`, verificadas por el compilador.** Esto se confirmó compilando
este archivo (junto con los 5 capítulos ya verificados, 3458/3458 jobs) en
un worktree temporal de ruta corta (`C:\w\ad26-lean\...`), reutilizando el
mismo cache de Mathlib (`rev = "v4.32.2"`) que el resto del proyecto — no se
tocó el pin ni el `lakefile.toml`. Los nombres de lema de Mathlib citados
abajo ya no son solo resultado de `grep`: son los que el compilador aceptó.

**Por qué este archivo NO está importado por `LeanVerificacion.lean` en
*este* worktree:** `import Mathlib.Probability.Moments.Variance` arrastra
transitivamente `Mathlib.Analysis.SpecialFunctions.
ContinuousFunctionalCalculus.PosPart.Basic`, y la ruta completa hasta el
artefacto `...PosPart\Basic.olean.server` en la ubicación de este worktree
(`...\ebook-estadistica-matematica.worktrees\corregir-hallazgos-ad26\
verification\lean_verificacion\...`) mide ~255 caracteres — contra el límite
MAX_PATH=260 de Windows — y `lean.exe` (no manifestado para rutas largas)
falla de forma determinista al escribirla. Esto es un límite de **longitud
de ruta de esta ubicación de checkout**, no un defecto de Mathlib ni del
toolchain de Lean en Windows en general: confirmado empíricamente
construyendo el mismo import (y luego este archivo completo, con las tres
pruebas ya escritas) en `C:\lv\` (ruta corta, ~139 caracteres hasta el mismo
archivo) y en un worktree temporal `C:\w\ad26-lean\` (~179 caracteres) — en
ambos, éxito total sin ningún cambio de código. (Diagnóstico previo,
descartado: un primer intento concluyó "no es longitud de ruta" a partir de
que escribir el mismo nombre de archivo vía .NET `File.WriteAllText`
funcionaba — pero .NET Core antepone automáticamente `\\?\` a sus rutas y
por tanto no está sujeto al mismo límite que `lean.exe`; esa prueba no era
discriminante.)

Ver `docs/verificacion-lean-hallazgos.md` (sección "muestreo_aleatorio" /
"decisión de la capa de esperanza") para el detalle completo, incluyendo la
decisión pendiente del usuario sobre el flujo de trabajo a seguir en este
worktree (compilar en un worktree temporal de ruta corta y copiar el
resultado, relocalizar este worktree, u otra alternativa).

Segunda capa axiomática del proyecto, construida sobre `MeasureTheory.Measure`
y `ProbabilityTheory.variance` de Mathlib (a diferencia de `Axiomas : Set Ω →
ℝ` en `FundamentosProbabilidad.lean`, que modela solo probabilidades de
eventos). División de trabajo: los capítulos que razonan sobre eventos
(fundamentos, técnicas de conteo, probabilidad condicional, teorema de Bayes)
usan `Axiomas`; los capítulos que razonan sobre variables aleatorias y su
esperanza/varianza (muestreo aleatorio en adelante) usan esta capa. No se
intenta unificarlas.

Tres lemas generales que desbloquean los capítulos de estimación
puntual/inferencia, aplicados aquí a una muestra i.i.d. `X : ι → Ω → ℝ` de
tamaño `Fintype.card ι`:

* `esperanza_media_muestral` : `E[X̄] = μ` — probado.
* `varianza_media_muestral`  : `Var(X̄) = σ²/n` — probado.
* `esperanza_varianza_muestral` : `E[S²] = σ²` (varianza muestral insesgada,
  reutiliza `MuestreoAleatorioProblemas.descomposicion_varianza`) — probado,
  incluyendo el paso final de esperanza que en `MuestreoAleatorioProblemas.
  lean` (`prob:0c980d4`) había quedado Tier D.

Lemas de Mathlib usados (confirmados por el compilador, `Mathlib` pin
`v4.32.2`): `ProbabilityTheory.variance_eq_integral`,
`ProbabilityTheory.variance_smul`,
`ProbabilityTheory.IndepFun.variance_sum` (`Mathlib/Probability/Moments/
Variance.lean`); `MeasureTheory.integral_finsetSum`, `integral_div`,
`integral_const_mul`, `integral_sub` (`Mathlib/MeasureTheory/Integral/
Bochner/Basic.lean`); `MeasureTheory.MemLp.integrable`,
`MemLp.integrable_sq`, `MemLp.sub`, `memLp_const`, `memLp_finsetSum'`,
`integrable_finsetSum` (`Mathlib/MeasureTheory/Function/L1Space/
Integrable.lean`, `L2Space.lean`, `LpSeminorm/TriangleInequality.lean`,
`LpSeminorm/Basic.lean`).
-/

open MeasureTheory ProbabilityTheory
open scoped MeasureTheory ProbabilityTheory

namespace VariablesAleatorias

variable {Ω : Type*} [MeasurableSpace Ω] {μ : Measure Ω} [IsProbabilityMeasure μ]

/-- Muestra aleatoria simple i.i.d. de tamaño `Fintype.card ι`: variables
cuadrado-integrables, independientes por pares, con media común `m` y
varianza común `sigma2`. -/
structure MuestraIID {ι : Type*} [Fintype ι]
    (X : ι → Ω → ℝ) (μ : Measure Ω) (m sigma2 : ℝ) : Prop where
  memLp : ∀ i, MemLp (X i) 2 μ
  indep : (↑(Finset.univ : Finset ι) : Set ι).Pairwise (fun i j => X i ⟂ᵢ[μ] X j)
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
  have hn : (Fintype.card ι : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  have hint : ∀ i ∈ (Finset.univ : Finset ι), Integrable (X i) μ :=
    fun i _ => (h.memLp i).integrable one_le_two
  change ∫ ω, (∑ i, X i ω) / (Fintype.card ι : ℝ) ∂μ = m
  rw [integral_div, integral_finsetSum Finset.univ hint]
  simp only [h.media, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  field_simp

omit [IsProbabilityMeasure μ] in
theorem varianza_media_muestral [Nonempty ι] (h : MuestraIID X μ m sigma2) :
    Var[mediaMuestral X; μ] = sigma2 / (Fintype.card ι : ℝ) := by
  have hn : (Fintype.card ι : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr Fintype.card_ne_zero
  have hsum : Var[∑ i, X i; μ] = ∑ i : ι, Var[X i; μ] :=
    IndepFun.variance_sum (s := Finset.univ) (fun i _ => h.memLp i) h.indep
  have hmedia_eq : mediaMuestral X = (Fintype.card ι : ℝ)⁻¹ • (∑ i, X i) := by
    funext ω
    simp [mediaMuestral, Pi.smul_apply, Finset.sum_apply, div_eq_inv_mul]
  rw [hmedia_eq, variance_smul, hsum]
  simp only [h.varianza, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  field_simp

theorem esperanza_varianza_muestral [Nonempty ι] (h : MuestraIID X μ m sigma2)
    (hn2 : 2 ≤ Fintype.card ι) :
    μ[varianzaMuestral X] = sigma2 := by
  have hcard2 : (2 : ℝ) ≤ (Fintype.card ι : ℝ) := by exact_mod_cast hn2
  have hn0 : (Fintype.card ι : ℝ) ≠ 0 := by linarith
  have hn1 : (Fintype.card ι : ℝ) - 1 ≠ 0 := by linarith
  have hne : (Finset.univ : Finset ι).Nonempty := Finset.univ_nonempty
  have hintsq : ∀ i, Integrable (fun ω => (X i ω - m) ^ 2) μ := fun i =>
    ((h.memLp i).sub (memLp_const m)).integrable_sq
  have hEXi : ∀ i, (∫ ω, (X i ω - m) ^ 2 ∂μ) = sigma2 := fun i => by
    have hae : AEMeasurable (X i) μ := (h.memLp i).aestronglyMeasurable.aemeasurable
    have hv := variance_eq_integral (μ := μ) hae
    rw [h.media i] at hv
    rw [← hv, h.varianza i]
  have hmedia_eq : mediaMuestral X = (Fintype.card ι : ℝ)⁻¹ • (∑ i, X i) := by
    funext ω
    simp [mediaMuestral, Pi.smul_apply, Finset.sum_apply, div_eq_inv_mul]
  have hmemXbar : MemLp (mediaMuestral X) 2 μ := by
    rw [hmedia_eq]
    exact (memLp_finsetSum' Finset.univ (fun i _ => h.memLp i)).const_smul _
  have hintXbarsq : Integrable (fun ω => (mediaMuestral X ω - m) ^ 2) μ :=
    (hmemXbar.sub (memLp_const m)).integrable_sq
  have hEXbar : (∫ ω, (mediaMuestral X ω - m) ^ 2 ∂μ) = sigma2 / (Fintype.card ι : ℝ) := by
    have hae : AEMeasurable (mediaMuestral X) μ := hmemXbar.aestronglyMeasurable.aemeasurable
    have hv := variance_eq_integral (μ := μ) hae
    rw [esperanza_media_muestral h] at hv
    rw [← hv, varianza_media_muestral h]
  have hpointwise : varianzaMuestral X = fun ω =>
      ((∑ i, (X i ω - m) ^ 2) - (Fintype.card ι : ℝ) * (mediaMuestral X ω - m) ^ 2) /
        ((Fintype.card ι : ℝ) - 1) := by
    funext ω
    have hdec := MuestreoAleatorioProblemas.descomposicion_varianza
      (ι := ι) Finset.univ (fun i => X i ω) m hne
    simp only [Finset.card_univ] at hdec
    change (∑ i, (X i ω - mediaMuestral X ω) ^ 2) / ((Fintype.card ι : ℝ) - 1) = _
    have hXbar_eq : mediaMuestral X ω = (∑ i, X i ω) / (Fintype.card ι : ℝ) := rfl
    rw [hXbar_eq, hdec]
  change ∫ ω, varianzaMuestral X ω ∂μ = sigma2
  rw [hpointwise]
  rw [integral_div]
  rw [integral_sub (integrable_finsetSum Finset.univ (fun i _ => hintsq i))
      (hintXbarsq.const_mul _)]
  rw [integral_finsetSum Finset.univ (fun i _ => hintsq i)]
  rw [integral_const_mul]
  simp only [hEXi, Finset.sum_const, Finset.card_univ, nsmul_eq_mul]
  rw [hEXbar]
  field_simp

end VariablesAleatorias
