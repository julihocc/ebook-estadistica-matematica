import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import LeanVerificacion.FundamentosProbabilidad
import LeanVerificacion.ProbabilidadCondicional

/-!
# Teorema de Bayes — verificación

Formaliza `latex/teorema_de_bayes.tex`. El teorema de Bayes y sus dos
generalizaciones (2 eventos, partición de $k$ eventos) están presentados
íntegramente en prosa/`align` — **ningún** `\begin{teorema}` explícito, de ahí
que el escaneo inicial por `grep` reportara 0 (el conteo de entornos no basta;
hay que leer el archivo completo). Se reutilizan `condicional`,
`cond_mul_eq_inter` y `thm_2_4_2` de `ProbabilidadCondicional`.

**Observación de terminología (no es un error matemático):** el libro llama
"regla de la cadena" tanto a la fórmula multiplicativa de intersecciones de
`probabilidad_condicional.tex` (`thm:2.4.1`, $P(A_1\cap A_2\cap A_3)=\dots$)
como, aquí, a la suma de probabilidad total $P(B)=\sum P(B|E_i)P(E_i)$ (línea
47 de este archivo). Son dos resultados distintos que comparten nombre —vale
la pena documentarlo para no confundirlos en una futura referencia cruzada.
-/

namespace TeoremaDeBayes

open FundamentosProbabilidad ProbabilidadCondicional

variable {Ω : Type*} {P : Set Ω → ℝ}

/-- Teorema de Bayes, caso básico (líneas 3-16) — $P(A|B) = P(A)P(B|A)/P(B)$,
derivado de que $P(A\cap B)=P(B\cap A)$. -/
theorem bayes_basico (h : Axiomas P) (A B : Set Ω) :
    condicional P B A = P A * condicional P A B / P B := by
  rw [cond_mul_eq_inter h A B]
  unfold condicional
  rw [Set.inter_comm A B]

/-- Generalización a 2 eventos (líneas 18-36) — $P(A|B) = \dfrac{P(A)P(B|A)}
{P(B|A)P(A)+P(B|A')P(A')}$, combinando `bayes_basico` con la probabilidad
total para la partición $\{A, A'\}$. -/
theorem bayes_dos_eventos (h : Axiomas P) (A B : Set Ω) :
    condicional P B A =
      P A * condicional P A B / (condicional P A B * P A + condicional P Aᶜ B * P Aᶜ) := by
  have hden : condicional P A B * P A + condicional P Aᶜ B * P Aᶜ = P B := by
    have h1 : P A * condicional P A B = P (A ∩ B) := cond_mul_eq_inter h A B
    have h2 : P Aᶜ * condicional P Aᶜ B = P (Aᶜ ∩ B) := cond_mul_eq_inter h Aᶜ B
    have hsum : P (A ∩ B) + P (Aᶜ ∩ B) = P B := by
      have := thm_2_2_7 h B A
      rw [Set.inter_comm B A, Set.inter_comm B Aᶜ] at this
      linarith
    nlinarith [h1, h2, hsum]
  rw [hden]
  exact bayes_basico h A B

/-- Generalización a una partición de $k$ eventos (líneas 38-57, y solución
idéntica de `prob:a7e87e4`) — $P(E_j|B) = \dfrac{P(B|E_j)P(E_j)}
{\sum_i P(B|E_i)P(E_i)}$. -/
theorem bayes_particion (h : Axiomas P) {ι : Type*} (s : Finset ι) (E : ι → Set Ω)
    (hpd : ∀ i ∈ s, ∀ i' ∈ s, i ≠ i' → Disjoint (E i) (E i'))
    (hcover : (⋃ i ∈ s, E i) = Set.univ) (B : Set Ω) {j : ι} (_hj : j ∈ s) :
    condicional P B (E j) =
      P (E j) * condicional P (E j) B / ∑ i ∈ s, P (E i) * condicional P (E i) B := by
  have hden : (∑ i ∈ s, P (E i) * condicional P (E i) B) = P B :=
    (thm_2_4_2 h s E hpd hcover B).symm
  rw [hden, cond_mul_eq_inter h (E j) B]
  unfold condicional
  rw [Set.inter_comm (E j) B]

/-- Ejemplo de la teoría (3 máquinas empacadoras, sin label explícita) — dado
$P(M_1)=0.38,P(M_2)=0.32,P(M_3)=0.30$ y $P(D|M_1)=0.11,P(D|M_2)=0.15,
P(D|M_3)=0.14$, $P(M_2|D)\approx 0.3642$. El numerador y denominador de Bayes
se ligan con `let` y se reutilizan (regla de encadenamiento). -/
theorem ejemplo_maquinas :
    let pM1 : ℝ := 0.38
    let pM2 : ℝ := 0.32
    let pM3 : ℝ := 0.30
    let pDgM1 : ℝ := 0.11
    let pDgM2 : ℝ := 0.15
    let pDgM3 : ℝ := 0.14
    let num := pDgM2 * pM2
    let den := pDgM1 * pM1 + pDgM2 * pM2 + pDgM3 * pM3
    |num / den - 0.3642| < 1e-4 := by
  rw [abs_lt]; constructor <;> norm_num

end TeoremaDeBayes
