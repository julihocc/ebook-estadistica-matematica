import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

/-!
# Distribución binomial — verificación

Formaliza `latex/distribucion_binomial.tex`. Sin entornos `teorema`, pero
`eq:2.10.2`/`eq:2.10.3` ($\mu=Np$, $\sigma^2=Npq$) son afirmaciones generales
sustanciales — Tier B, probadas aquí desde la definición
$f(x)=\binom{N}{x}p^xq^{N-x}$ vía la identidad de absorción
`Nat.add_one_mul_choose_eq` y el teorema del binomio `add_pow` de Mathlib, sin
citar un lema de media/varianza binomial ya empaquetado (Mathlib no tiene uno
para `PMF.binomial`). `exmp:2.10.3` (desarrollar $(p+q)^4$) solo referencia un
script Python sin dar la expansión explícita en el texto — nada que verificar
ahí.
-/

namespace DistribucionBinomial

/-- `exmp:2.10.1` — $\binom{6}{2}(1/2)^2(1/2)^4=15/64$. -/
theorem exmp_2_10_1 :
    (Nat.choose 6 2 : ℚ) * (1 / 2) ^ 2 * (1 / 2) ^ (6 - 2) = 15 / 64 := by
  norm_num [Nat.choose]

/-- `exmp:2.10.2` — $P(X\ge4)=\binom64(1/2)^4(1/2)^2+\binom65(1/2)^5(1/2)^1+
\binom66(1/2)^6=15/64+6/64+1/64=22/64=11/32\approx0.344$, para $\mathrm{Bin}(6,1/2)$. -/
theorem exmp_2_10_2 :
    let p46 : ℚ := (Nat.choose 6 4 : ℚ) * (1 / 2) ^ 4 * (1 / 2) ^ 2
    let p56 : ℚ := (Nat.choose 6 5 : ℚ) * (1 / 2) ^ 5 * (1 / 2) ^ 1
    let p66 : ℚ := (Nat.choose 6 6 : ℚ) * (1 / 2) ^ 6
    p46 = 15 / 64 ∧ p56 = 6 / 64 ∧ p66 = 1 / 64 ∧
      p46 + p56 + p66 = 11 / 32 ∧ |(p46 + p56 + p66 : ℝ) - 0.344| < 1e-3 := by
  norm_num [Nat.choose]

/-- Identidad de absorción de coeficientes binomiales, en la forma exacta que
se usa abajo: para $M,i\in\mathbb N$, $(i+1)\binom{M+1}{i+1}=(M+1)\binom{M}{i}$
— reordenamiento de `Nat.add_one_mul_choose_eq`. -/
theorem absorcion_binomial (M i : ℕ) :
    (i + 1) * (M + 1).choose (i + 1) = (M + 1) * M.choose i := by
  rw [Nat.mul_comm (i + 1)]
  exact (Nat.add_one_mul_choose_eq M i).symm

/-- Normalización de la PMF binomial: $\sum_{x=0}^n\binom nxp^xq^{n-x}=1$
cuando $p+q=1$, vía el teorema del binomio. Se prueba reordenando el
producto de `add_pow` (que da $p^xq^{n-x}\binom nx$, no $\binom nxp^xq^{n-x}$)
término a término con `ring`, en vez de forzar `rw` directo sobre el orden
distinto. -/
theorem suma_normalizada (n : ℕ) (p q : ℝ) (hpq : p + q = 1) :
    ∑ i ∈ Finset.range (n + 1), (n.choose i : ℝ) * p ^ i * q ^ (n - i) = 1 := by
  have h1 : (1 : ℝ) = (p + q) ^ n := by rw [hpq]; ring
  rw [h1, add_pow p q n]
  exact Finset.sum_congr rfl fun i _ => by ring

/-- `eq:2.10.2` — esperanza de una $\mathrm{Bin}(N,p)$ con $q=1-p$:
$\sum_{x=0}^N x\binom Nx p^xq^{N-x}=Np$. Se elimina el término $x=0$ (nulo),
se reindexa $x=i+1$, se aplica `absorcion_binomial` y se cierra con el
teorema del binomio ($p+q=1\Rightarrow(p+q)^M=1$). -/
theorem esperanza_binomial (N : ℕ) (p q : ℝ) (hpq : p + q = 1) :
    ∑ x ∈ Finset.range (N + 1), (x : ℝ) * (N.choose x : ℝ) * p ^ x * q ^ (N - x) =
      (N : ℝ) * p := by
  cases N with
  | zero => simp
  | succ M =>
    rw [Finset.sum_range_succ']
    simp only [Nat.cast_zero, zero_mul, pow_zero, mul_one, add_zero]
    push_cast
    have hterm : ∀ i ∈ Finset.range (M + 1),
        ((i : ℝ) + 1) * ((M + 1).choose (i + 1) : ℝ) * p ^ (i + 1) *
            q ^ (M - i) =
          (M + 1 : ℝ) * p * ((M.choose i : ℝ) * p ^ i * q ^ (M - i)) := by
      intro i _
      have habs' : ((i : ℝ) + 1) * ((M + 1).choose (i + 1) : ℝ) =
          (M + 1 : ℝ) * (M.choose i : ℝ) := by
        exact_mod_cast absorcion_binomial M i
      calc ((i : ℝ) + 1) * ((M + 1).choose (i + 1) : ℝ) * p ^ (i + 1) * q ^ (M - i)
          = (((i : ℝ) + 1) * ((M + 1).choose (i + 1) : ℝ)) * (p ^ i * p) * q ^ (M - i) := by
            ring
        _ = ((M + 1 : ℝ) * (M.choose i : ℝ)) * (p ^ i * p) * q ^ (M - i) := by rw [habs']
        _ = (M + 1 : ℝ) * p * ((M.choose i : ℝ) * p ^ i * q ^ (M - i)) := by ring
    rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum, suma_normalizada M p q hpq, mul_one]

/-- Segundo momento factorial: $\sum_{x=0}^N x(x-1)\binom Nx p^xq^{N-x}=
N(N-1)p^2$. Se eliminan los términos $x=0,1$ (nulos) y se aplica
`absorcion_binomial` dos veces (a $M+2\to M+1$ y a $M+1\to M$). Necesario
para $\mathrm{Var}(X)$ vía $\mathrm{Var}(X)=E[X(X-1)]+E[X]-E[X]^2$. -/
theorem momento_factorial_binomial (N : ℕ) (p q : ℝ) (hpq : p + q = 1) :
    ∑ x ∈ Finset.range (N + 1), (x : ℝ) * ((x : ℝ) - 1) * (N.choose x : ℝ) * p ^ x *
        q ^ (N - x) =
      (N : ℝ) * ((N : ℝ) - 1) * p ^ 2 := by
  match N with
  | 0 => simp
  | 1 => norm_num [Finset.sum_range_succ]
  | M + 2 =>
    rw [Finset.sum_range_succ', Finset.sum_range_succ']
    push_cast
    simp only [sub_self, zero_mul, mul_zero, add_zero]
    have hterm : ∀ i ∈ Finset.range (M + 1),
        ((i : ℝ) + 1 + 1) * ((i : ℝ) + 1 + 1 - 1) * ((M + 2).choose (i + 1 + 1) : ℝ) *
              p ^ (i + 1 + 1) * q ^ (M - i) =
          ((M : ℝ) + 2) * ((M : ℝ) + 1) * p ^ 2 *
            ((M.choose i : ℝ) * p ^ i * q ^ (M - i)) := by
      intro i _
      have habs1 : ((i : ℝ) + 1 + 1) * ((M + 2).choose (i + 1 + 1) : ℝ) =
          ((M : ℝ) + 2) * ((M + 1).choose (i + 1) : ℝ) := by
        exact_mod_cast absorcion_binomial (M + 1) (i + 1)
      have habs2 : ((i : ℝ) + 1) * ((M + 1).choose (i + 1) : ℝ) =
          ((M : ℝ) + 1) * (M.choose i : ℝ) := by
        exact_mod_cast absorcion_binomial M i
      rw [show (i : ℝ) + 1 + 1 - 1 = (i : ℝ) + 1 by ring]
      calc ((i : ℝ) + 1 + 1) * ((i : ℝ) + 1) * ((M + 2).choose (i + 1 + 1) : ℝ) *
            p ^ (i + 1 + 1) * q ^ (M - i)
          = (((i : ℝ) + 1 + 1) * ((M + 2).choose (i + 1 + 1) : ℝ)) *
              (((i : ℝ) + 1) * p ^ (i + 1)) * (p * q ^ (M - i)) := by ring
        _ = (((M : ℝ) + 2) * ((M + 1).choose (i + 1) : ℝ)) *
              (((i : ℝ) + 1) * p ^ (i + 1)) * (p * q ^ (M - i)) := by rw [habs1]
        _ = ((M : ℝ) + 2) * (((i : ℝ) + 1) * ((M + 1).choose (i + 1) : ℝ)) *
              (p ^ (i + 1) * p) * q ^ (M - i) := by ring
        _ = ((M : ℝ) + 2) * (((M : ℝ) + 1) * (M.choose i : ℝ)) *
              (p ^ (i + 1) * p) * q ^ (M - i) := by rw [habs2]
        _ = ((M : ℝ) + 2) * ((M : ℝ) + 1) * p ^ 2 *
              ((M.choose i : ℝ) * p ^ i * q ^ (M - i)) := by ring
    rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum, suma_normalizada M p q hpq, mul_one]
    ring

/-- `eq:2.10.3` — varianza de una $\mathrm{Bin}(N,p)$: $\mathrm{Var}(X)=Npq$,
combinando `esperanza_binomial` y `momento_factorial_binomial` vía
$\mathrm{Var}(X)=E[X(X-1)]+E[X]-E[X]^2$ (identidad algebraica pura, sin
necesidad de la capa de esperanza sobre `MeasureTheory` — aquí $E[\cdot]$ es
literalmente la suma finita `Finset.sum`, no una integral). -/
theorem varianza_binomial (N : ℕ) (p q : ℝ) (hpq : p + q = 1) :
    ∑ x ∈ Finset.range (N + 1), ((x : ℝ) - N * p) ^ 2 * (N.choose x : ℝ) * p ^ x *
        q ^ (N - x) =
      (N : ℝ) * p * q := by
  have hmean := esperanza_binomial N p q hpq
  have hmom2 : ∑ x ∈ Finset.range (N + 1),
      (x : ℝ) ^ 2 * (N.choose x : ℝ) * p ^ x * q ^ (N - x) =
        (N : ℝ) * ((N : ℝ) - 1) * p ^ 2 + (N : ℝ) * p := by
    have hfact := momento_factorial_binomial N p q hpq
    have hrw : ∀ x ∈ Finset.range (N + 1),
        (x : ℝ) * ((x : ℝ) - 1) * (N.choose x : ℝ) * p ^ x * q ^ (N - x) +
            (x : ℝ) * (N.choose x : ℝ) * p ^ x * q ^ (N - x) =
          (x : ℝ) ^ 2 * (N.choose x : ℝ) * p ^ x * q ^ (N - x) := by
      intro x _; ring
    rw [← Finset.sum_congr rfl hrw, Finset.sum_add_distrib, hfact, hmean]
  have hnorm := suma_normalizada N p q hpq
  have hexpand :
      ∑ x ∈ Finset.range (N + 1), ((x : ℝ) - N * p) ^ 2 * (N.choose x : ℝ) * p ^ x * q ^ (N - x) =
        (∑ x ∈ Finset.range (N + 1), (x : ℝ) ^ 2 * (N.choose x : ℝ) * p ^ x * q ^ (N - x)) -
          2 * ((N : ℝ) * p) *
            (∑ x ∈ Finset.range (N + 1), (x : ℝ) * (N.choose x : ℝ) * p ^ x * q ^ (N - x)) +
          ((N : ℝ) * p) ^ 2 *
            (∑ x ∈ Finset.range (N + 1), (N.choose x : ℝ) * p ^ x * q ^ (N - x)) := by
    rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun x _ => ?_
    ring
  rw [hexpand, hmom2, hmean, hnorm, show q = 1 - p from by linarith]
  ring

end DistribucionBinomial
