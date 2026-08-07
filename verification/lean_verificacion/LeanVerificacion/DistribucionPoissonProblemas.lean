import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Exp

/-!
# Distribución Poisson — problemas

Formaliza `latex/distribucion_poisson(p).tex`. `prob:06f83cc` (Recordar) es
puro recordatorio de la PMF — no se formaliza aparte. `prob:8fd3390`
(Aplicar) es idéntico a `exmp:2.10.5` de la teoría — no se repite.
`prob:5e9408a` (Evaluar) requiere una cola de Poisson con $\lambda=200$
sumada hasta $k=220$ y la CDF normal — **Tier C completo**, ver
`verification/scipy/distribucion_poisson/prob_5e9408a.py`. `prob:9dc367e`
(Crear) solo restablece $\mathbb E[X]=\mathrm{Var}(X)=\lambda=4$ sin cálculo
adicional — trivial por definición del parámetro, no se formaliza aparte.
-/

namespace DistribucionPoissonProblemas

/-- `prob:c35cfa7` (Comprender) — identidad algebraica exacta detrás de la
equivalencia Poisson/Bernoulli: $(e^{-\lambda/4})^4=e^{-\lambda}$ (aquí con
$\lambda=2$, $\lambda/4=0.5$), de modo que $1-(1-p)^4=1-e^{-\lambda}$ con
$p=1-e^{-\lambda/4}$. Es una identidad de exponentes, no necesita el valor
numérico de $e^{-2}$. -/
theorem prob_c35cfa7 (lam : ℝ) :
    1 - (1 - (1 - Real.exp (-(lam / 4)))) ^ 4 = 1 - Real.exp (-lam) := by
  have : (Real.exp (-(lam / 4))) ^ 4 = Real.exp (-lam) := by
    rw [← Real.exp_nat_mul]
    ring_nf
  simp only [sub_sub_cancel]
  rw [this]

/-- `prob:8dad711` (Analizar) — identidad general: la distribución
condicional de una Poisson($\lambda_1$) dado que la suma con una
Poisson($\lambda_2$) independiente vale $n$, es exactamente
$\mathrm{Bin}(n,\lambda_1/(\lambda_1+\lambda_2))$. Es álgebra pura (los
factores $e^{-\lambda_1}$, $e^{-\lambda_2}$ se cancelan exactamente contra
$e^{-(\lambda_1+\lambda_2)}$ — no se necesita ningún valor numérico de la
exponencial), reutilizando `Nat.choose_mul_factorial_mul_factorial`. -/
theorem prob_8dad711 (lam1 lam2 : ℝ) (hlam1 : 0 < lam1) (hlam2 : 0 < lam2) (n k : ℕ)
    (hk : k ≤ n) :
    (Real.exp (-lam1) * lam1 ^ k / (Nat.factorial k : ℝ) *
        (Real.exp (-lam2) * lam2 ^ (n - k) / (Nat.factorial (n - k) : ℝ))) /
      (Real.exp (-(lam1 + lam2)) * (lam1 + lam2) ^ n / (Nat.factorial n : ℝ)) =
    (n.choose k : ℝ) * (lam1 / (lam1 + lam2)) ^ k * (lam2 / (lam1 + lam2)) ^ (n - k) := by
  have hexp : Real.exp (-lam1) * Real.exp (-lam2) = Real.exp (-(lam1 + lam2)) := by
    rw [← Real.exp_add]; ring_nf
  have hpow : (lam1 + lam2) ^ n = (lam1 + lam2) ^ k * (lam1 + lam2) ^ (n - k) := by
    rw [← pow_add]; congr 1; omega
  have hchoose : (n.choose k : ℝ) * (Nat.factorial k : ℝ) * (Nat.factorial (n - k) : ℝ) =
      (Nat.factorial n : ℝ) := by
    exact_mod_cast Nat.choose_mul_factorial_mul_factorial hk
  have hsumpos : (0 : ℝ) < lam1 + lam2 := by linarith
  have hk0 : (Nat.factorial k : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero k)
  have hnk0 : (Nat.factorial (n - k) : ℝ) ≠ 0 :=
    Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero (n - k))
  have hn0 : (Nat.factorial n : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero n)
  have hexpn0 : Real.exp (-(lam1 + lam2)) ≠ 0 := (Real.exp_pos _).ne'
  rw [hpow, div_pow, div_pow]
  rw [← hexp]
  field_simp
  nlinarith [hchoose, sq_nonneg (lam1 + lam2)]

/-- `prob:8dad711`, evaluación numérica — $\lambda_1=3,\lambda_2=5,n=8,k=3$:
$P(X=3\mid X+Y=8)=\binom83(3/8)^3(5/8)^5$, instancia exacta racional (no
depende de `prob_8dad711`, que involucra exponenciales irracionales — se
verifica por separado como aritmética directa). **Hallazgo menor**: el
libro afirma $\approx0.2815$, pero el valor exacto es $590625/2097152
\approx0.28163$ (redondea a $0.2816$, no $0.2815$) — un desliz de redondeo
del último dígito, mucho menor que otros hallazgos de capítulos previos. -/
theorem prob_8dad711_numerico :
    let coef : ℝ := Nat.choose 8 3
    ¬ |coef * (3 / 8 : ℝ) ^ 3 * (5 / 8 : ℝ) ^ 5 - 0.2815| < 1e-4 ∧
      |coef * (3 / 8 : ℝ) ^ 3 * (5 / 8 : ℝ) ^ 5 - 0.28163| < 1e-4 := by
  constructor
  · rw [not_lt]; norm_num [Nat.choose]
  · norm_num [Nat.choose]

end DistribucionPoissonProblemas
