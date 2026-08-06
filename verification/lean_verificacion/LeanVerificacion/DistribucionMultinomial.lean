import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Multinomial

/-!
# Distribución multinomial — verificación

Formaliza `latex/distribucion_multinomial.tex`.

**Hallazgo confirmado (no matemático del contenido probabilístico, sino un
error de transcripción en la fórmula) — presente idénticamente en ES y EN,
por lo que no es una divergencia de traducción sino un error de la fuente
compartida:** `eq:2.10.8` afirma
$$f(x_1,\dots,x_k)=\frac{x_1+\cdots+x_k}{x_1!\cdots x_k!}p_1^{x_1}\cdots p_k^{x_k}$$
— al numerador le falta el signo de factorial; la fórmula correcta de la PMF
multinomial es $\frac{(x_1+\cdots+x_k)!}{x_1!\cdots x_k!}p_1^{x_1}\cdots
p_k^{x_k}$. Esto se confirma por el propio libro: el ejemplo resuelto
`exmp:2.10.6` que sigue inmediatamente usa $12!$ (no $12$) en el numerador,
y `latex/distribucion_multinomial(p).tex`'s `prob:2499194` da la fórmula
correcta con factorial. Es decir, el libro *usa* la fórmula correcta en la
práctica pero la *escribe* mal en `eq:2.10.8`. No se corrige aquí (regla del
proyecto: solo se reporta, la corrección de `.tex` requiere aprobación
explícita).
-/

namespace DistribucionMultinomial

/-- `exmp:2.10.6` — dado lanzado 12 veces, cada cara exactamente dos veces:
$P=\frac{12!}{(2!)^6}\left(\frac16\right)^{12}=\frac{479001600}{64}\cdot
\frac1{2176782336}\approx0.00344$. Usa la fórmula *correcta* (con factorial
en el numerador), consistente con la observación de arriba. -/
theorem exmp_2_10_6 :
    let P : ℚ := (Nat.factorial 12 : ℚ) / (Nat.factorial 2 : ℚ) ^ 6 * (1 / 6) ^ 12
    Nat.factorial 12 = 479001600 ∧ (Nat.factorial 2 : ℚ) ^ 6 = 64 ∧
      (6 : ℚ) ^ 12 = 2176782336 ∧ |(P : ℝ) - 0.00344| < 1e-5 := by
  norm_num [Nat.factorial]

/-- Normalización de la PMF multinomial: $\sum$ sobre todas las
composiciones $k:s\to\mathbb N$ con $\sum_i k(i)=n$ de
$\binom{n}{k}\prod_ip_i^{k(i)}=1$ cuando $\sum_ip_i=1$ — vía el teorema
multinomial de Mathlib (`Finset.sum_pow_eq_sum_piAntidiag`), instanciado en
$1^n=1$. Generaliza `eq:2.10.8` (corregida) a $k$ categorías arbitrarias, y
respalda la fórmula que el libro realmente usa en `exmp:2.10.6` y
`prob:2499194`. -/
theorem suma_normalizada_multinomial {α : Type*} [DecidableEq α] (s : Finset α) (p : α → ℝ)
    (hp : ∑ i ∈ s, p i = 1) (n : ℕ) :
    ∑ k ∈ s.piAntidiag n, (Nat.multinomial s k : ℝ) * ∏ i ∈ s, p i ^ k i = 1 := by
  rw [← Finset.sum_pow_eq_sum_piAntidiag, hp, one_pow]

end DistribucionMultinomial
