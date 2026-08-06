import Mathlib.Tactic
import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecificLimits.Normed

/-!
# Distribución geométrica y binomial negativa — verificación

Formaliza `latex/distribucion_geometrica_binomial_negativa.tex`. Sin
entornos `teorema`, pero las propiedades de pérdida de memoria y las
fórmulas de $\mu$/$\sigma^2$ son afirmaciones generales — Tier B para
pérdida de memoria y $\mu$ de la geométrica (probadas aquí vía series
geométricas infinitas, `tsum`, de Mathlib: `hasSum_geometric_of_norm_lt_one`,
`hasSum_coe_mul_geometric_of_norm_lt_one`). $\sigma^2$ de la geométrica y
$\mu,\sigma^2$ de la binomial negativa quedan **Tier D**: requerirían un
segundo momento de la serie geométrica ($\sum k^2q^k$), que no está
empaquetado directamente en Mathlib y necesitaría además un reindexado de
`tsum` (desplazar el índice en 2, extendiendo con ceros los primeros
términos) — factible pero de esfuerzo notablemente mayor al resto del
capítulo. La normalización de la binomial negativa (que la PMF suma 1) sí se
formaliza (Tier B), vía `tsum_choose_mul_geometric_of_norm_lt_one` de
Mathlib, que da exactamente el patrón $\sum\binom{n+k}{k}r^n$ de
`eq:2.10.10`.

Convención de índices: $X$ cuenta el número de *ensayos* hasta el primer
éxito (como en `eq:2.10.9`, soporte $\{1,2,3,\dots\}$); se reindexa
internamente como $k=X-1\in\{0,1,2,\dots\}$ (número de fracasos previos)
para poder usar directamente las series geométricas indexadas desde 0 de
Mathlib.
-/

namespace DistribucionGeometricaBinomialNegativa

/-- `exmp:2.10.13` — vendedor con $p=0.2$: $P(X=5)=(0.8)^4(0.2)=0.08192$;
$\mu=1/p=5$. -/
theorem exmp_2_10_13 :
    (0.8 : ℝ) ^ (5 - 1) * 0.2 = 0.08192 ∧ (1 : ℝ) / 0.2 = 5 := by
  norm_num

/-- `exmp:2.10.15` — examen con $p=0.3$, $r=3$: $P(X=4)=\binom{6}{2}(0.3)^3
(0.7)^4=15\times0.027\times0.2401\approx0.0972$, con $X$ = número de
fracasos (convención de `eq:2.10.10`). -/
theorem exmp_2_10_15 :
    let coef : ℝ := Nat.choose (4 + 3 - 1) (3 - 1)
    coef = 15 ∧ |coef * (0.3 : ℝ) ^ 3 * (0.7 : ℝ) ^ 4 - 0.0972| < 1e-4 := by
  norm_num [Nat.choose]

/-- Cola de la distribución geométrica: $P(X>m)=(1-p)^m$ para $X$ = número
de ensayos hasta el primer éxito. Se prueba directamente como una serie
geométrica desplazada (`k+m`), sin necesidad de un lema de reindexado
separado: $\sum_k q^{k+m}p = q^mp\sum_kq^k=q^mp/p=q^m$. -/
theorem cola_geometrica (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) (m : ℕ) :
    ∑' k : ℕ, (1 - p) ^ (k + m) * p = (1 - p) ^ m := by
  have hq_lt : ‖(1 - p : ℝ)‖ < 1 := by rw [Real.norm_eq_abs, abs_lt]; constructor <;> linarith
  have h := (hasSum_geometric_of_norm_lt_one hq_lt).mul_right ((1 - p) ^ m * p)
  have heq : (fun k : ℕ => (1 - p) ^ k * ((1 - p) ^ m * p)) =
      fun k : ℕ => (1 - p) ^ (k + m) * p := by funext k; rw [pow_add]; ring
  rw [heq] at h
  rw [h.tsum_eq]
  have heq1 : 1 - (1 - p) = p := by ring
  rw [heq1]
  field_simp

/-- **Pérdida de memoria**: $P(X>m+n\mid X>m)=P(X>n)$, para $X$ el número de
ensayos hasta el primer éxito y $0<p<1$. Formalizado como la razón de las
colas (`cola_geometrica`), no como una probabilidad condicional abstracta
(el proyecto no tiene una capa de probabilidad condicional sobre variables
aleatorias continuas de soporte infinito). -/
theorem perdida_memoria (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) (m n : ℕ) :
    (∑' k : ℕ, (1 - p) ^ (k + (m + n)) * p) / (∑' k : ℕ, (1 - p) ^ (k + m) * p) =
      ∑' k : ℕ, (1 - p) ^ (k + n) * p := by
  rw [cola_geometrica p hp0 hp1 (m + n), cola_geometrica p hp0 hp1 m,
    cola_geometrica p hp0 hp1 n, pow_add]
  have hqpos : (0 : ℝ) < 1 - p := by linarith
  field_simp

/-- `eq:2.10.9`/propiedades — esperanza de la geométrica $\mu=1/p$ para
$0<p\le1$: $\sum_{k=0}^\infty(k+1)q^kp=1/p$ (con $k+1$ = número de ensayos,
$k$ = fracasos previos), vía linealidad de `tsum` sobre
`hasSum_coe_mul_geometric_of_norm_lt_one` y `hasSum_geometric_of_norm_lt_one`. -/
theorem esperanza_geometrica (p : ℝ) (hp0 : 0 < p) (hp1 : p < 1) :
    ∑' k : ℕ, ((k : ℝ) + 1) * (1 - p) ^ k * p = 1 / p := by
  have hq_lt : ‖(1 - p : ℝ)‖ < 1 := by rw [Real.norm_eq_abs, abs_lt]; constructor <;> linarith
  have h1 := hasSum_coe_mul_geometric_of_norm_lt_one hq_lt
  have h2 := hasSum_geometric_of_norm_lt_one hq_lt
  have h3 := (h1.add h2).mul_right p
  have heq : (fun k : ℕ => ((k : ℝ) * (1 - p) ^ k + (1 - p) ^ k) * p) =
      fun k : ℕ => ((k : ℝ) + 1) * (1 - p) ^ k * p := by funext k; ring
  rw [heq] at h3
  rw [h3.tsum_eq]
  have heq1 : 1 - (1 - p) = p := by ring
  rw [heq1]
  field_simp
  ring

/-- Normalización de la binomial negativa: $\sum_{k=0}^\infty\binom{k+r-1}{r-1}
p^r(1-p)^k=1$ para $r\ge1$, $0<p\le1$ — vía `tsum_choose_mul_geometric_of_norm_lt_one`
de Mathlib con `k:=r-1`, que da exactamente el patrón $\binom{n+m}{m}q^n$ de
`eq:2.10.10`. -/
theorem suma_normalizada_binomial_negativa (r : ℕ) (hr : 1 ≤ r) (p : ℝ) (hp0 : 0 < p)
    (hp1 : p < 1) :
    ∑' k : ℕ, (Nat.choose (k + r - 1) (r - 1) : ℝ) * p ^ r * (1 - p) ^ k = 1 := by
  have hq_lt : ‖(1 - p : ℝ)‖ < 1 := by rw [Real.norm_eq_abs, abs_lt]; constructor <;> linarith
  have h := (hasSum_choose_mul_geometric_of_norm_lt_one (r - 1) hq_lt).mul_left (p ^ r)
  have hidx : ∀ k : ℕ, k + r - 1 = k + (r - 1) := fun k => by omega
  have heq : (fun k : ℕ => p ^ r * ((k + (r - 1)).choose (r - 1) * (1 - p) ^ k)) =
      fun k : ℕ => (Nat.choose (k + r - 1) (r - 1) : ℝ) * p ^ r * (1 - p) ^ k := by
    funext k; rw [hidx k]; ring
  rw [heq] at h
  rw [h.tsum_eq]
  have heq1 : 1 - (1 - p) = p := by ring
  rw [heq1]
  have hr1 : r - 1 + 1 = r := by omega
  rw [hr1]
  have hpne : p ≠ 0 := ne_of_gt hp0
  field_simp

end DistribucionGeometricaBinomialNegativa
