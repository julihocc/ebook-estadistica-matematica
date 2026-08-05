import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import LeanVerificacion.FundamentosProbabilidad

/-!
# Probabilidad condicional y regla de Bayes — verificación

Formaliza la definición y los 2 `teorema`s de `latex/probabilidad_condicional.tex`
(la fórmula de Bayes en sí está comentada — inactiva — en ese archivo del libro;
se define en `teorema_de_bayes.tex`, el siguiente capítulo). Reutiliza la
estructura `Axiomas` de `FundamentosProbabilidad`.
-/

namespace ProbabilidadCondicional

open FundamentosProbabilidad

variable {Ω : Type*} {P : Set Ω → ℝ}

/-- `definicion` (Probabilidad condicional) — $P(B|A) = P(A\cap B)/P(A)$. En
Lean, la división real por cero da $0$ (convención estándar de Mathlib); esto
no afecta ninguna demostración aquí porque `cond_mul_eq_inter` de abajo es
válida incondicionalmente, incluso cuando $P(A)=0$. -/
noncomputable def condicional (P : Set Ω → ℝ) (A B : Set Ω) : ℝ := P (A ∩ B) / P A

/-- Segunda mitad de la misma `definicion` del libro — $P(A\cap B) = P(A)P(B|A)$
— demostrada incondicionalmente (sin requerir $P(A)\neq 0$): si $P(A)=0$,
monotonía + no-negatividad fuerzan $P(A\cap B)=0$ también, y ambos lados son
$0$. -/
theorem cond_mul_eq_inter (h : Axiomas P) (A B : Set Ω) :
    P A * condicional P A B = P (A ∩ B) := by
  unfold condicional
  by_cases hA : P A = 0
  · have hsub : A ∩ B ⊆ A := Set.inter_subset_left
    have hle : P (A ∩ B) ≤ P A := (thm_2_2_1 h hsub).1
    have hnn : 0 ≤ P (A ∩ B) := h.no_neg _
    have hz : P (A ∩ B) = 0 := le_antisymm (hA ▸ hle) hnn
    simp [hA, hz]
  · field_simp

/-- `thm:2.4.1` — regla de la cadena para 3 eventos:
$P(A_1\cap A_2\cap A_3) = P(A_1)P(A_2|A_1)P(A_3|A_1\cap A_2)$. El libro exige
$P(A_1)>0$ (y, implícitamente, $P(A_1\cap A_2)>0$) para que la probabilidad
condicional esté definida; aquí, como en `cond_mul_eq_inter`, la igualdad se
prueba sin esa hipótesis porque la convención de Mathlib da $0$ para división
entre cero — cuando $P(A_1)=0$ (o $P(A_1\cap A_2)=0$) el enunciado degenera a
una identidad trivial ($0=0$ vía monotonía), no falla, así que esta versión es
estrictamente más general que la del libro, no una versión distinta. -/
theorem thm_2_4_1 (h : Axiomas P) (A1 A2 A3 : Set Ω) :
    P A1 * condicional P A1 A2 * condicional P (A1 ∩ A2) A3 = P (A1 ∩ A2 ∩ A3) := by
  rw [cond_mul_eq_inter h A1 A2, cond_mul_eq_inter h (A1 ∩ A2) A3]

/-- `thm:2.4.2` — regla de la probabilidad total: si $S=A_1\sqcup\dots\sqcup A_N$,
$P(A)=\sum_i P(A_i)P(A|A_i)$. Se deriva de `thm_2_2_8` (partición general,
`FundamentosProbabilidad`) combinado con `cond_mul_eq_inter`. -/
theorem thm_2_4_2 (h : Axiomas P) {ι : Type*} (s : Finset ι)
    (Apart : ι → Set Ω) (hpd : ∀ i ∈ s, ∀ j ∈ s, i ≠ j → Disjoint (Apart i) (Apart j))
    (hcover : (⋃ i ∈ s, Apart i) = Set.univ) (A : Set Ω) :
    P A = ∑ i ∈ s, P (Apart i) * condicional P (Apart i) A := by
  have hstep : ∀ i ∈ s, P (Apart i) * condicional P (Apart i) A = P (A ∩ Apart i) := by
    intro i _
    rw [cond_mul_eq_inter h (Apart i) A, Set.inter_comm]
  rw [Finset.sum_congr rfl hstep]
  exact thm_2_2_8 h s Apart hpd hcover A

/-- Ejemplo de la teoría (canicas, sin etiqueta explícita): en un bote con 3
canicas blancas y 2 negras, extraídas sin reemplazo, $P(E_1\cap E_2')=
\frac{3}{5}\times\frac{2}{4}=\frac{6}{20}$ y $P(E_2'|E_1)=\frac{1}{2}$
(dado que $P(E_1)=3/5$). Verificado como aritmética exacta de racionales, tal
como el libro lo calcula (sin construir el espacio muestral discreto
completo). -/
theorem exmp_canicas :
    (3 : ℚ) / 5 * (2 / 4) = 6 / 20 ∧ ((3 : ℚ) / 5 * (2 / 4)) / (3 / 5) = 1 / 2 := by
  constructor <;> norm_num

end ProbabilidadCondicional
