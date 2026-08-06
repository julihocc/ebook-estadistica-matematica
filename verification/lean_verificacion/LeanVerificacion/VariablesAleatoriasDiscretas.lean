import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Variables aleatorias discretas — verificación

Formaliza la parte cuantitativa de `latex/variables_aleatorias_discretas.tex`.
El archivo no tiene entornos `teorema`; el contenido verificable es: los tres
ejemplos de distribuciones de probabilidad discretas (lanzamiento de monedas,
suma de dos dados, número de niños en una familia de 3 hijos), todos Tier A
(conteo exacto sobre tipos finitos vía `decide`); y la identidad de
König-Huygens $\mathrm{Var}(X)=E[X^2]-\mu^2$ (`eq:varianza_formula_corta`),
Tier B, probada aquí en forma general para cualquier variable aleatoria
discreta de soporte finito — es pura álgebra de sumas ponderadas finitas, no
requiere la capa de esperanza/varianza construida sobre `MeasureTheory` en
`VariablesAleatorias.lean` (esa capa modela muestras i.i.d. vía
`ProbabilityTheory.variance`; aquí basta con `Finset.sum`).

Los ejemplos 2.6.5–2.6.7 (funciones de distribución acumulada, solo descritas
mediante figuras/gráficas, sin fórmula explícita en el texto) y la
observación sobre monotonía/continuidad por la derecha de la CDF no se
formalizan — no hay una afirmación numérica o algebraica concreta que
verificar, solo prosa y gráficas.
-/

namespace VariablesAleatoriasDiscretas

/-- `exmp:2.6.2` — dos lanzamientos de moneda, $X$ = número de soles.
Espacio muestral `Bool × Bool` (`true` = sol), $X(\omega)$ cuenta los soles.
Las cardinalidades se cuentan con `decide` (no se citan a mano) para que un
conteo erróneo en el libro pudiera detectarse. -/
theorem exmp_2_6_2 :
    let X : Bool × Bool → ℕ := fun ω => (if ω.1 then 1 else 0) + (if ω.2 then 1 else 0)
    (Finset.univ.filter (fun ω => X ω = 0)).card = 1 ∧
      (Finset.univ.filter (fun ω : Bool × Bool => X ω = 1)).card = 2 ∧
      (Finset.univ.filter (fun ω : Bool × Bool => X ω = 2)).card = 1 := by
  decide

/-- `exmp:2.6.2`, continuación — la función de probabilidad como fracciones
exactas: $f(0)=1/4$, $f(1)=1/2$, $f(2)=1/4$, calculadas a partir de las
cardinalidades de `exmp_2_6_2` (no re-escritas). -/
theorem exmp_2_6_2_probabilidades :
    let X : Bool × Bool → ℕ := fun ω => (if ω.1 then 1 else 0) + (if ω.2 then 1 else 0)
    let card0 : ℚ := (Finset.univ.filter (fun ω => X ω = 0)).card
    let card1 : ℚ := (Finset.univ.filter (fun ω => X ω = 1)).card
    let card2 : ℚ := (Finset.univ.filter (fun ω => X ω = 2)).card
    card0 / 4 = 1 / 4 ∧ card1 / 4 = 1 / 2 ∧ card2 / 4 = 1 / 4 := by
  have h : ((Finset.univ.filter
      (fun ω : Bool × Bool => (if ω.1 then 1 else 0) + (if ω.2 then 1 else 0) = 0)).card = 1) ∧
      ((Finset.univ.filter
      (fun ω : Bool × Bool => (if ω.1 then 1 else 0) + (if ω.2 then 1 else 0) = 1)).card = 2) ∧
      ((Finset.univ.filter
      (fun ω : Bool × Bool => (if ω.1 then 1 else 0) + (if ω.2 then 1 else 0) = 2)).card = 1) := by
    decide
  simp only [h.1, h.2.1, h.2.2]
  norm_num

/-- `exmp:2.6.3` — suma de dos dados, $X = D_1+D_2$ (con $D_1,D_2\in\{1,\dots,6\}$
representados como `Fin 6` desplazado por 1). Se verifican las 11
cardinalidades de la tabla del libro ($x=2,\dots,12$) contra el número de
formas de obtenerlas, todas por `decide` sobre `Fin 6 × Fin 6` (36 resultados). -/
theorem exmp_2_6_3 :
    let X : Fin 6 × Fin 6 → ℕ := fun ω => ω.1.val + ω.2.val + 2
    (Finset.univ.filter (fun ω => X ω = 2)).card = 1 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 3)).card = 2 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 4)).card = 3 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 5)).card = 4 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 6)).card = 5 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 7)).card = 6 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 8)).card = 5 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 9)).card = 4 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 10)).card = 3 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 11)).card = 2 ∧
      (Finset.univ.filter (fun ω : Fin 6 × Fin 6 => X ω = 12)).card = 1 := by
  decide

/-- `exmp:2.6.4` — número de niños en una familia de 3 hijos (`Bool × Bool ×
Bool`, `true` = niño). Las cardinalidades $1,3,3,1$ coinciden con
$\binom{3}{0},\binom{3}{1},\binom{3}{2},\binom{3}{3}$, confirmando la
observación del libro de que es una distribución binomial $N=3$, $p=1/2$. -/
theorem exmp_2_6_4 :
    let X : Bool × Bool × Bool → ℕ :=
      fun ω => (if ω.1 then 1 else 0) + (if ω.2.1 then 1 else 0) + (if ω.2.2 then 1 else 0)
    (Finset.univ.filter (fun ω => X ω = 0)).card = 1 ∧
      (Finset.univ.filter (fun ω : Bool × Bool × Bool => X ω = 1)).card = 3 ∧
      (Finset.univ.filter (fun ω : Bool × Bool × Bool => X ω = 2)).card = 3 ∧
      (Finset.univ.filter (fun ω : Bool × Bool × Bool => X ω = 3)).card = 1 := by
  decide

/-- `eq:varianza_formula_corta` — identidad de König-Huygens para una
variable aleatoria discreta de soporte finito `s`, con función de masa `f`
que suma 1: $\mathrm{Var}(X)=\sum_i(X_i-\mu)^2 f_i = \sum_i X_i^2 f_i - \mu^2$,
donde $\mu=\sum_i X_i f_i$. Álgebra pura de sumas ponderadas — no requiere la
capa de esperanza sobre `MeasureTheory`. -/
theorem konig_huygens {ι : Type*} (s : Finset ι) (X f : ι → ℝ) (hf : ∑ i ∈ s, f i = 1) :
    let mu := ∑ i ∈ s, X i * f i
    ∑ i ∈ s, (X i - mu) ^ 2 * f i = ∑ i ∈ s, (X i) ^ 2 * f i - mu ^ 2 := by
  intro mu
  have expand : ∑ i ∈ s, (X i - mu) ^ 2 * f i =
      ∑ i ∈ s, ((X i) ^ 2 * f i - 2 * mu * (X i * f i) + mu ^ 2 * f i) := by
    refine Finset.sum_congr rfl fun i _ => ?_
    ring
  rw [expand, Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
    hf]
  ring

end VariablesAleatoriasDiscretas
