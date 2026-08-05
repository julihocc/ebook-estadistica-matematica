import Mathlib.Tactic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Finset.Card
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.GroupTheory.Perm.Fin
import LeanVerificacion.FundamentosProbabilidad

/-!
# Fundamentos de probabilidad — problemas

Formaliza los problemas de `latex/fundamentos_de_probabilidad(p).tex`, uno por
nivel de Bloom, citando la etiqueta `\label{prob:<hex>}` del libro. Cada lema
transcribe los números/pasos del libro tal como están escritos (metodología:
no se re-demuestra "la versión correcta" y se compara a ojo).
-/

namespace FundamentosProbabilidadProblemas

open FundamentosProbabilidad

/-- `prob:de3947a` (Recordar) — El espacio muestral de una carta de una baraja
inglesa es el producto cartesiano de 4 palos y 13 rangos, con $4 \times 13 = 52$
puntos muestrales. -/
theorem prob_de3947a : Fintype.card (Fin 4 × Fin 13) = 52 := by decide

/-!
`prob:cfa53ca` (Comprender), incisos 4–7 — los incisos 1–3 son
interpretaciones en prosa sin contenido formalizable ("se obtiene un rey o un
trébol", etc.), pero 4–7 son identidades de conjuntos concretas que la
solución del libro usa implícitamente (Ley de De Morgan, definición de
diferencia, distributividad).
-/

/-- Inciso 4 — $A' \cup B' = (A\cap B)'$ (Ley de De Morgan). -/
theorem prob_cfa53ca_inciso4 {Ω : Type*} (A B : Set Ω) : Aᶜ ∪ Bᶜ = (A ∩ B)ᶜ :=
  (Set.compl_inter A B).symm

/-- Inciso 5 — $A - B = A \cap B'$. -/
theorem prob_cfa53ca_inciso5 {Ω : Type*} (A B : Set Ω) : A \ B = A ∩ Bᶜ :=
  Set.sdiff_eq A B

/-- Inciso 6 — $A' - B' = A' \cap B$. -/
theorem prob_cfa53ca_inciso6 {Ω : Type*} (A B : Set Ω) : Aᶜ \ Bᶜ = Aᶜ ∩ B := by
  rw [Set.sdiff_eq, compl_compl]

/-- Inciso 7 — $(A \cap B) \cup (A \cap B') = A$ (distributividad). -/
theorem prob_cfa53ca_inciso7 {Ω : Type*} (A B : Set Ω) :
    (A ∩ B) ∪ (A ∩ Bᶜ) = A :=
  Set.inter_union_compl A B

/-- `prob:69a20ec` (Aplicar) — La probabilidad de obtener al menos un 4 en dos
lanzamientos de un dado de 6 caras es $11/36$, calculada vía el complemento:
$1 - 25/36$. Convención: `Fin 6` indexa las caras $1$–$6$ como $0$–$5$, así que
la cara "4" es el índice `3`. -/
theorem prob_69a20ec :
    let favorable := Finset.univ.filter (fun p : Fin 6 × Fin 6 => p.1 = 3 ∨ p.2 = 3)
    let complemento := Finset.univ.filter (fun p : Fin 6 × Fin 6 => ¬(p.1 = 3 ∨ p.2 = 3))
    (favorable.card : ℚ) / 36 = 1 - (complemento.card : ℚ) / 36 ∧
    (favorable.card : ℚ) / 36 = 11 / 36 := by
  intro favorable complemento
  have hfav : favorable.card = 11 := by decide
  have hcomp : complemento.card = 25 := by decide
  rw [hfav, hcomp]
  refine ⟨by norm_num, by norm_num⟩

/-- `prob:1f335a1` (Analizar) — La regla general de adición, demostrada
exclusivamente a partir de los tres axiomas de Kolmogorov. Idéntica a
`FundamentosProbabilidad.thm_2_2_6`, que es la formalización de este problema. -/
theorem prob_1f335a1 {Ω : Type*} {P : Set Ω → ℝ} (h : FundamentosProbabilidad.Axiomas P)
    (A B : Set Ω) : P (A ∪ B) = P A + P B - P (A ∩ B) :=
  FundamentosProbabilidad.thm_2_2_6 h A B

/-- `prob:a4ff50c` (Evaluar), verificación de caso pequeño ($n=3$) — el libro
deriva $P(\bigcup A_i) = \sum_{k=1}^n (-1)^{k-1}/k!$ para el problema del
guardarropa mediante inclusión-exclusión general; aquí se verifica la fórmula
concretamente para $n=3$ por conteo directo de permutaciones, como evidencia
parcial (la derivación simbólica general y el límite $n\to\infty$ se clasifican
Tier D — ver bitácora de hallazgos). Para $n=3$: 6 permutaciones totales, 2
sin puntos fijos (derangements), por lo que 4 tienen al menos un punto fijo,
y $4/6 = 2/3 = 1 - 1/2 + 1/6$. -/
theorem prob_a4ff50c_n3 :
    (Finset.univ.filter (fun σ : Equiv.Perm (Fin 3) => ∃ i, σ i = i)).card = 4 ∧
    (4 : ℚ) / 6 = 1 - 1/2 + 1/6 := by
  constructor
  · decide
  · norm_num

/-- `prob:b993271` (Crear) — el ejemplo numérico de la solución (dado de 8
caras, $A=\{2,3,4,5\}$, $B=\{4,5,6,7\}$) satisface la regla general de adición
$P(A) + P(B) - P(A \cap B) = P(A \cup B)$: $0.5 + 0.5 - 0.25 = 0.75$. Convención:
`Fin 8` indexa las caras $1$–$8$ como $0$–$7$, así que $A=\{2,3,4,5\}$ es
`{1,2,3,4}` y $B=\{4,5,6,7\}$ es `{3,4,5,6}`. -/
theorem prob_b993271 :
    let A : Finset (Fin 8) := {1, 2, 3, 4}
    let B : Finset (Fin 8) := {3, 4, 5, 6}
    (A.card : ℚ) / 8 = 0.5 ∧ (B.card : ℚ) / 8 = 0.5 ∧
    ((A ∩ B).card : ℚ) / 8 = 0.25 ∧ ((A ∪ B).card : ℚ) / 8 = 0.75 ∧
    (A.card : ℚ) / 8 + (B.card : ℚ) / 8 - ((A ∩ B).card : ℚ) / 8 = ((A ∪ B).card : ℚ) / 8 := by
  intro A B
  have hA : A.card = 4 := by decide
  have hB : B.card = 4 := by decide
  have hAB : (A ∩ B).card = 2 := by decide
  have hU : (A ∪ B).card = 6 := by decide
  rw [hA, hB, hAB, hU]
  refine ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

end FundamentosProbabilidadProblemas
