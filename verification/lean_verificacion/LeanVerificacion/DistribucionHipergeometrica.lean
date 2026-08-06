import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import LeanVerificacion.DistribucionBinomial
import LeanVerificacion.DistribucionBinomialProblemas

/-!
# Distribución hipergeométrica — verificación

Formaliza `latex/distribucion_hipergeometrica.tex`. Sin entornos `teorema`.
$\mu_X=nK/N$ (`eq:2.10.11`/propiedades) se prueba en general — Tier B —
reutilizando `absorcion_binomial` de `DistribucionBinomial.lean` y
`vandermonde_binomial` de `DistribucionMultinomialProblemas.lean`, sin
necesidad de una identidad nueva: es exactamente el mismo patrón de
absorción+Vandermonde ya construido para otros capítulos. $\sigma^2_X=
n\frac{K}{N}\left(1-\frac{K}{N}\right)\frac{N-n}{N-1}$ se verifica por la
ruta algebraica que el propio libro usa en `prob:64e9a8d` (suma de
indicadoras correlacionadas, $\mathrm{Var}(X)=n\mathrm{Var}(I_i)-n(n-1)
|\mathrm{Cov}(I_i,I_j)|$), no re-derivando la covarianza desde cero (eso
requeriría la misma infraestructura de covarianza entre variables
correlacionadas que quedó Tier D en `distribucion_multinomial`) sino
verificando que la combinación algebraica de las piezas ya dadas por el
libro (`Var(I_i)`, `Cov(I_i,I_j)`) efectivamente produce la fórmula cerrada
— es una identidad de álgebra pura, Tier B.
-/

namespace DistribucionHipergeometrica

/-- `exmp:2.10.16` — lote $N=20,K=5,n=4$: $P(X=2)=\binom52\binom{15}2/
\binom{20}4=1050/4845\approx0.2167$. -/
theorem exmp_2_10_16 :
    let num : ℝ := (Nat.choose 5 2 : ℝ) * (Nat.choose 15 2 : ℝ)
    let den : ℝ := Nat.choose 20 4
    num = 1050 ∧ den = 4845 ∧ |num / den - 0.2167| < 1e-4 := by
  norm_num [Nat.choose]

/-- `exmp:2.10.17` — póker $N=52,K=4,n=5$: $P(X=3)=\binom43\binom{48}2/
\binom{52}5=4512/2598960\approx0.00174$. -/
theorem exmp_2_10_17 :
    let num : ℝ := (Nat.choose 4 3 : ℝ) * (Nat.choose 48 2 : ℝ)
    let den : ℝ := Nat.choose 52 5
    num = 4512 ∧ den = 2598960 ∧ |num / den - 0.00174| < 1e-5 := by
  norm_num [Nat.choose]

/-- Identidad combinatoria central detrás de $\mu_X=nK/N$: $\sum_{k=0}^n
k\binom Kk\binom{N-K}{n-k}=K\binom{N-1}{n-1}$, para $1\le K\le N$, $1\le n$.
Se elimina el término $k=0$ (nulo), se reindexa $k=j+1$, se aplica
`absorcion_binomial` (con $M:=K-1$) y se cierra con `vandermonde_binomial`. -/
theorem suma_k_hipergeometrica (N K n : ℕ) (hK1 : 1 ≤ K) (hKN : K ≤ N) (hn1 : 1 ≤ n) :
    ∑ k ∈ Finset.range (n + 1), k * K.choose k * (N - K).choose (n - k) =
      K * (N - 1).choose (n - 1) := by
  obtain ⟨K', rfl⟩ := Nat.exists_eq_add_of_le hK1
  obtain ⟨n', rfl⟩ := Nat.exists_eq_add_of_le hn1
  simp only [Nat.add_sub_cancel_left]
  rw [Finset.sum_range_succ']
  simp only [Nat.zero_mul, Nat.add_zero]
  have hterm : ∀ j ∈ Finset.range (1 + n'), (j + 1) * (1 + K').choose (j + 1) *
      (N - (1 + K')).choose (1 + n' - (j + 1)) =
        (1 + K') * (K'.choose j * (N - (1 + K')).choose (n' - j)) := by
    intro j _
    rw [show 1 + n' - (j + 1) = n' - j by omega]
    have habs : (j + 1) * (1 + K').choose (j + 1) = (1 + K') * K'.choose j := by
      rw [Nat.add_comm 1 K']
      exact DistribucionBinomial.absorcion_binomial K' j
    rw [habs, Nat.mul_assoc]
  rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum]
  have hvander := DistribucionBinomialProblemas.vandermonde_binomial K' (N - (1 + K')) n'
  rw [Nat.add_comm 1 n', hvander]
  congr 2
  omega

/-- Identidad de absorción para `N`/`n`: $N\binom{N-1}{n-1}=n\binom Nn$, para
$1\le N$, $1\le n$ — reordenamiento de `Nat.add_one_mul_choose_eq`, misma
técnica que `absorcion_binomial`. -/
theorem absorcion_Nn (N n : ℕ) (hN1 : 1 ≤ N) (hn1 : 1 ≤ n) :
    N * (N - 1).choose (n - 1) = n * N.choose n := by
  obtain ⟨N', rfl⟩ := Nat.exists_eq_add_of_le hN1
  obtain ⟨n', rfl⟩ := Nat.exists_eq_add_of_le hn1
  simp only [Nat.add_sub_cancel_left]
  have h := Nat.add_one_mul_choose_eq N' n'
  rw [Nat.add_comm 1 N', Nat.add_comm 1 n', h]
  ring

/-- `eq:2.10.11`/propiedades — esperanza de la hipergeométrica $\mu=nK/N$,
combinando `suma_k_hipergeometrica` y `absorcion_Nn`. -/
theorem esperanza_hipergeometrica (N K n : ℕ) (hK1 : 1 ≤ K) (hKN : K ≤ N) (hn1 : 1 ≤ n)
    (hN1 : 1 ≤ N) (hnN : n ≤ N) :
    (∑ k ∈ Finset.range (n + 1), (k : ℝ) * (K.choose k : ℝ) * ((N - K).choose (n - k) : ℝ)) /
        (N.choose n : ℝ) =
      (n : ℝ) * K / N := by
  have hnat := suma_k_hipergeometrica N K n hK1 hKN hn1
  have hcast : ∑ k ∈ Finset.range (n + 1), (k : ℝ) * (K.choose k : ℝ) *
      ((N - K).choose (n - k) : ℝ) = (K : ℝ) * ((N - 1).choose (n - 1) : ℝ) := by
    exact_mod_cast hnat
  rw [hcast]
  have habsorb := absorcion_Nn N n hN1 hn1
  have habsorb' : (N : ℝ) * ((N - 1).choose (n - 1) : ℝ) = (n : ℝ) * (N.choose n : ℝ) := by
    exact_mod_cast habsorb
  have hNpos : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have hCpos : (N.choose n : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (Nat.choose_ne_zero (by omega))
  field_simp
  linarith [habsorb']

/-- `prob:64e9a8d`/`eq:2.10.11` propiedades — verificación algebraica de
$\mathrm{Var}(X)=n\frac{K}{N}\left(1-\frac{K}{N}\right)\frac{N-n}{N-1}$ a
partir de la descomposición en indicadoras correlacionadas
($\mathrm{Var}(X)=n\mathrm{Var}(I_i)-n(n-1)|\mathrm{Cov}(I_i,I_j)|$, con
$\mathrm{Var}(I_i)=\frac KN(1-\frac KN)$ y $\mathrm{Cov}(I_i,I_j)=
-\frac{K(N-K)}{N^2(N-1)}$, ambas dadas por el libro, no re-derivadas aquí —
esa derivación necesitaría la infraestructura de covarianza Tier D de
`distribucion_multinomial`). Es una identidad de álgebra pura. -/
theorem varianza_hipergeometrica_algebra (N K n : ℕ) (hN2 : 2 ≤ N) :
    (n : ℝ) * ((K : ℝ) / N * (1 - (K : ℝ) / N)) -
        (n : ℝ) * ((n : ℝ) - 1) * ((K : ℝ) * (N - K) / ((N : ℝ) ^ 2 * ((N : ℝ) - 1))) =
      (n : ℝ) * ((K : ℝ) / N) * (1 - (K : ℝ) / N) * (((N : ℝ) - n) / ((N : ℝ) - 1)) := by
  have hNpos : (N : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  have hN1pos : (N : ℝ) - 1 ≠ 0 := by
    have : (2 : ℝ) ≤ (N : ℝ) := by exact_mod_cast hN2
    linarith
  field_simp
  ring

end DistribucionHipergeometrica
