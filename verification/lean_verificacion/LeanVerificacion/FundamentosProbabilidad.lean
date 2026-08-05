import Mathlib.Tactic
import Mathlib.Data.Set.Lattice
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Fundamentos de probabilidad — verificación

Formaliza los 8 `teorema`s de `latex/fundamentos_de_probabilidad.tex` (etiquetas
`thm:2.2.1`–`thm:2.2.8`) y los problemas Analizar/Aplicar/Crear de
`latex/fundamentos_de_probabilidad(p).tex`, tal como el libro los enuncia: a partir
únicamente de los tres axiomas de Kolmogorov dados en el texto (líneas 213-247),
sin recurrir a teoría de la medida de Mathlib (que trabaja con `ℝ≥0∞` y
σ-álgebras, maquinaria que el libro no introduce en este capítulo).

Cada lema cita la etiqueta `\label{...}` del libro que formaliza.
-/

namespace FundamentosProbabilidad

variable {Ω : Type*}

/-- Los tres axiomas de Kolmogorov como los enuncia el libro
(fundamentos_de_probabilidad.tex, líneas 213-247): no negatividad, probabilidad
total 1, y aditividad para eventos mutuamente excluyentes. El libro enuncia la
aditividad para colecciones numerables; aquí se toma la versión de dos eventos
(la única que se usa realmente en cada demostración del capítulo) como axioma
primitivo, y la versión finita/N-aria se deriva por inducción. -/
structure Axiomas (P : Set Ω → ℝ) : Prop where
  no_neg : ∀ A : Set Ω, 0 ≤ P A
  prob_total : P (Set.univ : Set Ω) = 1
  aditividad : ∀ A B : Set Ω, Disjoint A B → P (A ∪ B) = P A + P B

variable {P : Set Ω → ℝ}

/-- `thm:2.2.1` — Si $A_1 \subset A_2$, entonces $P(A_1) \le P(A_2)$ y
$P(A_2 - A_1) = P(A_2) - P(A_1)$. -/
theorem thm_2_2_1 (h : Axiomas P) {A1 A2 : Set Ω} (hsub : A1 ⊆ A2) :
    P A1 ≤ P A2 ∧ P (A2 \ A1) = P A2 - P A1 := by
  have hunion : A1 ∪ (A2 \ A1) = A2 := Set.union_sdiff_cancel hsub
  have hdisj : Disjoint A1 (A2 \ A1) := disjoint_sdiff_self_right
  have hadd : P A2 = P A1 + P (A2 \ A1) := by
    conv_lhs => rw [← hunion]
    exact h.aditividad A1 (A2 \ A1) hdisj
  have hnn : 0 ≤ P (A2 \ A1) := h.no_neg _
  constructor
  · linarith
  · linarith

/-- `thm:2.2.2` — Para cada evento $A$, $0 \le P(A) \le 1$. -/
theorem thm_2_2_2 (h : Axiomas P) (A : Set Ω) : 0 ≤ P A ∧ P A ≤ 1 := by
  refine ⟨h.no_neg A, ?_⟩
  have hle := (thm_2_2_1 h (Set.subset_univ A)).1
  rwa [h.prob_total] at hle

/-- `thm:2.2.3` — El evento imposible tiene probabilidad cero. -/
theorem thm_2_2_3 (h : Axiomas P) : P (∅ : Set Ω) = 0 := by
  have hdisj : Disjoint (Set.univ : Set Ω) (∅ : Set Ω) := disjoint_bot_right
  have hadd := h.aditividad Set.univ ∅ hdisj
  simp only [Set.union_empty] at hadd
  linarith [hadd, h.prob_total]

/-- `thm:2.2.4` — $P(A') = 1 - P(A)$. -/
theorem thm_2_2_4 (h : Axiomas P) (A : Set Ω) : P Aᶜ = 1 - P A := by
  have hdisj : Disjoint A Aᶜ := disjoint_compl_right
  have hunion : A ∪ Aᶜ = Set.univ := Set.union_compl_self A
  have hadd := h.aditividad A Aᶜ hdisj
  rw [hunion, h.prob_total] at hadd
  linarith

/-- Lema auxiliar (no está numerado en el libro, pero cada demostración de
`thm:2.2.5`/`thm:2.2.8` lo usa implícitamente): la aditividad de dos eventos se
extiende por inducción a una familia finita de eventos disjuntos por pares
indexada por un `Finset`. -/
theorem aditividad_finita (h : Axiomas P) {ι : Type*} (s : Finset ι)
    (A : ι → Set Ω) (hpd : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (A i) (A j)) :
    P (⋃ i ∈ s, A i) = ∑ i ∈ s, P (A i) := by
  classical
  induction s using Finset.induction_on with
  | empty => simp [thm_2_2_3 h]
  | @insert a s ha ih =>
    have hpd' : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (A i) (A j) := fun i hi j hj hij =>
      hpd i (Finset.mem_insert_of_mem hi) j (Finset.mem_insert_of_mem hj) hij
    have hdisj_a : Disjoint (A a) (⋃ i ∈ s, A i) := by
      rw [Set.disjoint_iUnion₂_right]
      intro i hi
      exact hpd a (Finset.mem_insert_self a s) i (Finset.mem_insert_of_mem hi)
        (fun heq => ha (heq ▸ hi))
    have hset : (⋃ i ∈ insert a s, A i) = A a ∪ ⋃ i ∈ s, A i := by
      simp
    rw [hset, h.aditividad (A a) _ hdisj_a, ih hpd', Finset.sum_insert ha]

/-- `thm:2.2.5` — Si $A = A_1 \sqcup \dots \sqcup A_N$ es unión disjunta,
$P(A) = P(A_1) + \dots + P(A_N)$; en particular si $S = A_1 \sqcup \dots \sqcup A_N$
entonces $\sum P(A_i) = 1$. -/
theorem thm_2_2_5 (h : Axiomas P) {ι : Type*} (s : Finset ι) (A : ι → Set Ω)
    (hpd : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (A i) (A j)) :
    P (⋃ i ∈ s, A i) = ∑ i ∈ s, P (A i) :=
  aditividad_finita h s A hpd

theorem thm_2_2_5_particion (h : Axiomas P) {ι : Type*} (s : Finset ι)
    (A : ι → Set Ω) (hpd : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (A i) (A j))
    (hcover : (⋃ i ∈ s, A i) = Set.univ) :
    ∑ i ∈ s, P (A i) = 1 := by
  rw [← thm_2_2_5 h s A hpd, hcover, h.prob_total]

/-- `thm:2.2.6` — Para $A, B$ no necesariamente disjuntos,
$P(A \cup B) = P(A) + P(B) - P(A \cap B)$. Esta es también la solución de
`prob:1f335a1`. -/
theorem thm_2_2_6 (h : Axiomas P) (A B : Set Ω) : P (A ∪ B) = P A + P B - P (A ∩ B) := by
  have hdecomp : A ∪ B = A ∪ (B \ A) := by
    rw [Set.union_sdiff_self]
  have hdisj1 : Disjoint A (B \ A) := disjoint_sdiff_self_right
  have h1 : P (A ∪ B) = P A + P (B \ A) := by
    rw [hdecomp]; exact h.aditividad A (B \ A) hdisj1
  have hBdecomp : B = (A ∩ B) ∪ (B \ A) := by
    rw [Set.inter_comm, Set.inter_union_sdiff]
  have hdisj2 : Disjoint (A ∩ B) (B \ A) := by
    apply Set.disjoint_left.mpr
    rintro x ⟨_, hxB⟩ ⟨_, hxnA⟩
    exact hxnA ‹x ∈ A›
  have h2 : P B = P (A ∩ B) + P (B \ A) := by
    conv_lhs => rw [hBdecomp]
    exact h.aditividad (A ∩ B) (B \ A) hdisj2
  linarith

/-- `thm:2.2.6`, caso de tres eventos — $P(A\cup B\cup C) = P(A)+P(B)+P(C) -
P(A\cap B)-P(B\cap C)-P(C\cap A) + P(A\cap B\cap C)$. Se deriva aplicando dos
veces el caso de dos eventos: primero a $(A\cup B)$ y $C$, luego a $A\cap C$ y
$B\cap C$ (usando que $(A\cup B)\cap C = (A\cap C)\cup(B\cap C)$). -/
theorem thm_2_2_6_tres_eventos (h : Axiomas P) (A B C : Set Ω) :
    P (A ∪ B ∪ C) = P A + P B + P C - P (A ∩ B) - P (B ∩ C) - P (C ∩ A) + P (A ∩ B ∩ C) := by
  have e1 : P (A ∪ B ∪ C) = P (A ∪ B) + P C - P ((A ∪ B) ∩ C) := thm_2_2_6 h (A ∪ B) C
  have e2 : P (A ∪ B) = P A + P B - P (A ∩ B) := thm_2_2_6 h A B
  have hset : (A ∪ B) ∩ C = (A ∩ C) ∪ (B ∩ C) := Set.union_inter_distrib_right A B C
  have e3 : P ((A ∪ B) ∩ C) = P (A ∩ C) + P (B ∩ C) - P ((A ∩ C) ∩ (B ∩ C)) := by
    rw [hset]; exact thm_2_2_6 h (A ∩ C) (B ∩ C)
  have hset2 : (A ∩ C) ∩ (B ∩ C) = A ∩ B ∩ C := by
    ext x; simp only [Set.mem_inter_iff]; tauto
  have hCA : P (C ∩ A) = P (A ∩ C) := by rw [Set.inter_comm]
  rw [e3, hset2] at e1
  rw [hCA]
  linarith

/-- `thm:2.2.7` — Para cualesquiera eventos $A, B$,
$P(A) = P(A \cap B) + P(A \cap B')$. -/
theorem thm_2_2_7 (h : Axiomas P) (A B : Set Ω) : P A = P (A ∩ B) + P (A ∩ Bᶜ) := by
  have hdecomp : A = (A ∩ B) ∪ (A ∩ Bᶜ) := (Set.inter_union_compl A B).symm
  have hdisj : Disjoint (A ∩ B) (A ∩ Bᶜ) := by
    apply Set.disjoint_left.mpr
    rintro x ⟨_, hxB⟩ ⟨_, hxnB⟩
    exact hxnB hxB
  conv_lhs => rw [hdecomp]
  exact h.aditividad (A ∩ B) (A ∩ Bᶜ) hdisj

/-- `thm:2.2.8` — Si $A_1, \dots, A_N$ es una partición de $S$, entonces para
cualquier evento $A$, $P(A) = \sum_i P(A \cap A_i)$. -/
theorem thm_2_2_8 (h : Axiomas P) {ι : Type*} (s : Finset ι)
    (Apart : ι → Set Ω) (hpd : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (Apart i) (Apart j))
    (hcover : (⋃ i ∈ s, Apart i) = Set.univ) (A : Set Ω) :
    P A = ∑ i ∈ s, P (A ∩ Apart i) := by
  have hpd' : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (A ∩ Apart i) (A ∩ Apart j) := by
    intro i hi j hj hij
    exact (hpd i hi j hj hij).mono (Set.inter_subset_right) (Set.inter_subset_right)
  have hcover' : (⋃ i ∈ s, A ∩ Apart i) = A := by
    rw [← Set.inter_iUnion₂]
    rw [hcover]
    simp
  conv_lhs => rw [← hcover']
  exact aditividad_finita h s (fun i => A ∩ Apart i) hpd'

end FundamentosProbabilidad
