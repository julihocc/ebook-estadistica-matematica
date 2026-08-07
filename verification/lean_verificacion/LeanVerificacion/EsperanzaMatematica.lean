import Mathlib.Tactic
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals.Basic

/-!
# Esperanza matemática — teoría

Formaliza `latex/esperanza_matematica.tex`. Capítulo denso: linealidad,
König-Huygens, varianza de combinaciones lineales, covarianza, variable
estandarizada. Se construye una capa propia de esperanza/varianza sobre
`MeasureTheory.integral` directamente (`∫ ω, X ω ∂P`), **sin** citar
`ProbabilityTheory.variance`/`Mathlib.Probability.Moments.Variance` —
un test de humo confirmó que importar el paquete de independencia
(`Mathlib.Probability.Independence.Integration`, necesario para
`thm:2.9.2`) también dispara el mismo error de longitud de ruta de
Windows que bloqueó `VariablesAleatorias.lean` en este worktree
(transitivamente jala `ContinuousFunctionalCalculus.PosPart.Basic`). Por
eso `thm:2.9.2` (independencia $\Rightarrow E(XY)=E(X)E(Y)$) y
`eq:2.9.16` (que depende de él) se dejan como Tier D aquí, documentadas,
no como un fallo silencioso.
-/

namespace EsperanzaMatematica

open MeasureTheory intervalIntegral

variable {Ω : Type*} [MeasureSpace Ω] (P : Measure Ω) [IsProbabilityMeasure P]

/-- Bajo `IsProbabilityMeasure`, integrar la función constante `c` da `c` —
lema auxiliar reutilizado en cada identidad de esta capa. -/
theorem integral_const_eq_self (c : ℝ) : (∫ _ω : Ω, c ∂P) = c := by
  simp [MeasureTheory.integral_const]

/-- `thm:2.9.1` — Linealidad de la esperanza: $E(cX+dY)=cE(X)+dE(Y)$,
para cualesquiera $X,Y$ (no requiere independencia — solo linealidad de
la integral). -/
theorem linealidad {X Y : Ω → ℝ} (hX : Integrable X P) (hY : Integrable Y P) (c d : ℝ) :
    (∫ ω, c * X ω + d * Y ω ∂P) = c * (∫ ω, X ω ∂P) + d * (∫ ω, Y ω ∂P) := by
  rw [MeasureTheory.integral_add (hX.const_mul c) (hY.const_mul d),
    MeasureTheory.integral_const_mul, MeasureTheory.integral_const_mul]

/-- `eq:2.9.14` — Identidad de König-Huygens general: $\sigma^2=E(X^2)-\mu^2$,
para cualquier `X` integrable con segundo momento integrable. -/
theorem konig_huygens {X : Ω → ℝ} (hX : Integrable X P) (hX2 : Integrable (fun ω => X ω ^ 2) P) :
    (∫ ω, (X ω - ∫ ω', X ω' ∂P) ^ 2 ∂P) = (∫ ω, X ω ^ 2 ∂P) - (∫ ω, X ω ∂P) ^ 2 := by
  set mu := ∫ ω, X ω ∂P with hmu
  have heq : (fun ω => (X ω - mu) ^ 2) = fun ω => X ω ^ 2 - 2 * mu * X ω + mu ^ 2 := by
    funext ω; ring
  have hstep1 : Integrable (fun ω => X ω ^ 2 - 2 * mu * X ω) P := hX2.sub (hX.const_mul (2 * mu))
  have hstep2 : Integrable (fun ω : Ω => mu ^ 2) P := integrable_const _
  rw [heq, MeasureTheory.integral_add hstep1 hstep2,
    MeasureTheory.integral_sub hX2 (hX.const_mul (2 * mu)),
    MeasureTheory.integral_const_mul, integral_const_eq_self]
  ring

/-- `eq:2.9.15` — $\mathrm{Var}(cX)=c^2\mathrm{Var}(X)$. -/
theorem var_escalar {X : Ω → ℝ} (c : ℝ) :
    (∫ ω, (c * X ω - ∫ ω', c * X ω' ∂P) ^ 2 ∂P) = c ^ 2 * ∫ ω, (X ω - ∫ ω', X ω' ∂P) ^ 2 ∂P := by
  have hmean : (∫ ω, c * X ω ∂P) = c * ∫ ω, X ω ∂P := MeasureTheory.integral_const_mul c X
  have heq : (fun ω => (c * X ω - ∫ ω', c * X ω' ∂P) ^ 2)
      = fun ω => c ^ 2 * (X ω - ∫ ω', X ω' ∂P) ^ 2 := by
    funext ω; rw [hmean]; ring
  rw [heq, MeasureTheory.integral_const_mul]

/-- `thm:2.9.3` — $\sigma^2=\min_a E[(X-a)^2]$: completando el cuadrado,
$E[(X-a)^2]=\mathrm{Var}(X)+(\mu-a)^2\ge\mathrm{Var}(X)$, con igualdad
sii $a=\mu$. -/
theorem varianza_es_minimo {X : Ω → ℝ} (hX : Integrable X P)
    (hX2 : Integrable (fun ω => X ω ^ 2) P) (a : ℝ) :
    (∫ ω, (X ω - a) ^ 2 ∂P) = (∫ ω, (X ω - ∫ ω', X ω' ∂P) ^ 2 ∂P) + (∫ ω', X ω' ∂P - a) ^ 2 := by
  set mu := ∫ ω, X ω ∂P with hmu
  have heq : (fun ω => (X ω - a) ^ 2)
      = fun ω => (X ω - mu) ^ 2 + 2 * (mu - a) * (X ω - mu) + (mu - a) ^ 2 := by
    funext ω; ring
  have hint1 : Integrable (fun ω => (X ω - mu) ^ 2) P := by
    have heq1 : (fun ω => (X ω - mu) ^ 2) = fun ω => X ω ^ 2 - 2 * mu * X ω + mu ^ 2 := by
      funext ω; ring
    have : Integrable (fun ω => X ω ^ 2 - 2 * mu * X ω + mu ^ 2) P :=
      (hX2.sub (hX.const_mul (2 * mu))).add (integrable_const (mu ^ 2))
    rwa [heq1]
  have hint2 : Integrable (fun ω => 2 * (mu - a) * (X ω - mu)) P := by
    have heq2 : (fun ω => 2 * (mu - a) * (X ω - mu)) = fun ω => (2 * (mu - a)) * X ω - (2 * (mu - a)) * mu := by
      funext ω; ring
    have : Integrable (fun ω => 2 * (mu - a) * X ω - 2 * (mu - a) * mu) P :=
      (hX.const_mul (2 * (mu - a))).sub (integrable_const _)
    rwa [heq2]
  have hint12 : Integrable (fun ω => (X ω - mu) ^ 2 + 2 * (mu - a) * (X ω - mu)) P :=
    hint1.add hint2
  have hint3 : Integrable (fun ω : Ω => (mu - a) ^ 2) P := integrable_const _
  rw [heq, MeasureTheory.integral_add hint12 hint3, MeasureTheory.integral_add hint1 hint2,
    MeasureTheory.integral_const_mul, integral_const_eq_self]
  have hmuint : (∫ ω, (X ω - mu) ∂P) = 0 := by
    have heq3 : (fun ω => X ω - mu) = fun ω => X ω - mu := rfl
    have : Integrable (fun ω : Ω => mu) P := integrable_const _
    rw [MeasureTheory.integral_sub hX this, integral_const_eq_self, hmu]
    ring
  rw [show (∫ ω, X ω - mu ∂P) = 0 from hmuint]
  ring

/-- `eq:2.9.24` — $\sigma_{XY}=\mathrm{Cov}(X,Y)=E(XY)-\mu_X\mu_Y$. -/
theorem covarianza {X Y : Ω → ℝ} (hX : Integrable X P) (hY : Integrable Y P)
    (hXY : Integrable (fun ω => X ω * Y ω) P) :
    (∫ ω, (X ω - ∫ ω', X ω' ∂P) * (Y ω - ∫ ω', Y ω' ∂P) ∂P) =
      (∫ ω, X ω * Y ω ∂P) - (∫ ω, X ω ∂P) * ∫ ω, Y ω ∂P := by
  set muX := ∫ ω, X ω ∂P with hmuX
  set muY := ∫ ω, Y ω ∂P with hmuY
  have heq : (fun ω => (X ω - muX) * (Y ω - muY))
      = fun ω => X ω * Y ω - muY * X ω - muX * Y ω + muX * muY := by
    funext ω; ring
  have h1 : Integrable (fun ω => X ω * Y ω - muY * X ω) P := hXY.sub (hX.const_mul muY)
  have h2 : Integrable (fun ω => muX * Y ω) P := hY.const_mul muX
  have h12 : Integrable (fun ω => X ω * Y ω - muY * X ω - muX * Y ω) P := h1.sub h2
  have h3 : Integrable (fun ω : Ω => muX * muY) P := integrable_const _
  rw [heq, MeasureTheory.integral_add h12 h3, MeasureTheory.integral_sub h1 h2,
    MeasureTheory.integral_sub hXY (hX.const_mul muY), MeasureTheory.integral_const_mul,
    MeasureTheory.integral_const_mul, integral_const_eq_self]
  ring

/-- `eq:2.9.25`/`eq:2.9.26` — $\mathrm{Var}(X\pm Y)=\mathrm{Var}(X)\pm2\mathrm{Cov}(X,Y)+\mathrm{Var}(Y)$,
general (no requiere independencia; la versión con $\mathrm{Cov}=0$ para
independientes, `eq:2.9.16`, es Tier D en este worktree — ver nota del
archivo). -/
theorem varianza_suma {X Y : Ω → ℝ} (hX : Integrable X P) (hY : Integrable Y P)
    (hX2 : Integrable (fun ω => X ω ^ 2) P) (hY2 : Integrable (fun ω => Y ω ^ 2) P)
    (hXY : Integrable (fun ω => X ω * Y ω) P) :
    (∫ ω, ((X ω + Y ω) - ∫ ω', X ω' + Y ω' ∂P) ^ 2 ∂P) =
      (∫ ω, (X ω - ∫ ω', X ω' ∂P) ^ 2 ∂P) +
        2 * (∫ ω, (X ω - ∫ ω', X ω' ∂P) * (Y ω - ∫ ω', Y ω' ∂P) ∂P) +
          ∫ ω, (Y ω - ∫ ω', Y ω' ∂P) ^ 2 ∂P := by
  have hsum : (∫ ω, X ω + Y ω ∂P) = (∫ ω, X ω ∂P) + ∫ ω, Y ω ∂P :=
    MeasureTheory.integral_add hX hY
  set muX := ∫ ω, X ω ∂P
  set muY := ∫ ω, Y ω ∂P
  have heq : (fun ω => ((X ω + Y ω) - (muX + muY)) ^ 2)
      = fun ω => (X ω - muX) ^ 2 + 2 * ((X ω - muX) * (Y ω - muY)) + (Y ω - muY) ^ 2 := by
    funext ω; ring
  have hint1 : Integrable (fun ω => (X ω - muX) ^ 2) P := by
    have heq1 : (fun ω => (X ω - muX) ^ 2) = fun ω => X ω ^ 2 - 2 * muX * X ω + muX ^ 2 := by
      funext ω; ring
    have : Integrable (fun ω => X ω ^ 2 - 2 * muX * X ω + muX ^ 2) P :=
      (hX2.sub (hX.const_mul (2 * muX))).add (integrable_const _)
    rwa [heq1]
  have hint2 : Integrable (fun ω => (X ω - muX) * (Y ω - muY)) P := by
    have heq2 : (fun ω => (X ω - muX) * (Y ω - muY))
        = fun ω => X ω * Y ω - muY * X ω - muX * Y ω + muX * muY := by funext ω; ring
    have : Integrable (fun ω => X ω * Y ω - muY * X ω - muX * Y ω + muX * muY) P :=
      (((hXY.sub (hX.const_mul muY)).sub (hY.const_mul muX)).add (integrable_const _))
    rwa [heq2]
  have hint3 : Integrable (fun ω => (Y ω - muY) ^ 2) P := by
    have heq3 : (fun ω => (Y ω - muY) ^ 2) = fun ω => Y ω ^ 2 - 2 * muY * Y ω + muY ^ 2 := by
      funext ω; ring
    have : Integrable (fun ω => Y ω ^ 2 - 2 * muY * Y ω + muY ^ 2) P :=
      (hY2.sub (hY.const_mul (2 * muY))).add (integrable_const _)
    rwa [heq3]
  have hint2' : Integrable (fun ω => 2 * ((X ω - muX) * (Y ω - muY))) P := hint2.const_mul 2
  have hint12 : Integrable (fun ω => (X ω - muX) ^ 2 + 2 * ((X ω - muX) * (Y ω - muY))) P :=
    hint1.add hint2'
  rw [hsum, heq, MeasureTheory.integral_add hint12 hint3, MeasureTheory.integral_add hint1 hint2',
    MeasureTheory.integral_const_mul]

/-- `eq:2.9.17`/`eq:2.9.18` — variable estandarizada $X^*=(X-\mu)/\sigma$:
$E(X^*)=0$ (dado $\sigma\ne0$; la parte $\mathrm{Var}(X^*)=1$ se sigue de
`var_escalar` con $c=1/\sigma$ y `konig_huygens`, no se repite). -/
theorem estandarizada {X : Ω → ℝ} (hX : Integrable X P) (sigma : ℝ) :
    (∫ ω, (X ω - ∫ ω', X ω' ∂P) / sigma ∂P) = 0 := by
  have hmuint : (∫ ω, (X ω - ∫ ω', X ω' ∂P) ∂P) = 0 := by
    have : Integrable (fun ω : Ω => ∫ ω', X ω' ∂P) P := integrable_const _
    rw [MeasureTheory.integral_sub hX this, integral_const_eq_self]
    ring
  have heq : (fun ω => (X ω - ∫ ω', X ω' ∂P) / sigma) = fun ω => sigma⁻¹ * (X ω - ∫ ω', X ω' ∂P) := by
    funext ω; ring
  rw [heq, MeasureTheory.integral_const_mul, hmuint]
  ring

/-- **`exmp:2.9.1` — hallazgo confirmado.** El enunciado (línea 75) dice
que la cara $6$ paga \$30, pero la PMF/cálculo de la solución (líneas
82–93) usa \$60 para la cara $6$ y llega a $E(X)=\$20$. Con los datos del
propio enunciado ($20,\$0,\$40,\$0,\$0,\$30$) la esperanza correcta es
$\$15$, no $\$20$. La solución en sí es internamente consistente
($(20+40+60)/6=20$) — el error está entre lo dado y lo resuelto, no en
la aritmética de la solución. Verificado con `git log -p` que este
desacuerdo estatement/solución existe **desde la introducción original
del ejemplo** (no es una regresión de la auditoría de 2026-07-13, que
solo eliminó un bloque `align` residual y duplicado con un error
aritmético distinto, $120/6=15$ en vez de $20$, dejando intacto este
desacuerdo $30$ vs. $60$ que sobrevivió sin ser detectado). Presente
idéntico en EN (`en_esperanza_matematica.tex`). -/
theorem exmp_2_9_1_hallazgo :
    ((20 : ℚ) * (1 / 6) + 40 * (1 / 6) + 30 * (1 / 6) + 0 * (3 / 6) ≠ 20) ∧
      ((20 : ℚ) * (1 / 6) + 40 * (1 / 6) + 30 * (1 / 6) + 0 * (3 / 6) = 15) ∧
      ((20 : ℚ) * (1 / 6) + 40 * (1 / 6) + 60 * (1 / 6) + 0 * (3 / 6) = 20) := by
  norm_num

/-- Ejemplo del dado (línea 37): $E(X)=3.5$ para $X$ uniforme en
$\{1,\ldots,6\}$. -/
theorem esperanza_dado : ((1 : ℚ) + 2 + 3 + 4 + 5 + 6) / 6 = 3.5 := by norm_num

/-- Varianza del dado: $\sigma^2=17.5/6\approx2.9166\ldots$ — el libro
trunca a $2.916$ en vez de redondear a $2.917$; convención de
truncamiento, no error. -/
theorem varianza_dado :
    ((1 - 3.5 : ℚ) ^ 2 + (2 - 3.5) ^ 2 + (3 - 3.5) ^ 2 + (4 - 3.5) ^ 2 + (5 - 3.5) ^ 2 +
        (6 - 3.5) ^ 2) / 6 = 35 / 12 := by norm_num

/-- `exmp:2.9.2` — $E(X)=4/3$ para $f(x)=x/2$ en $(0,2)$. -/
theorem exmp_2_9_2 : (∫ x in (0 : ℝ)..2, x * (x / 2)) = 4 / 3 := by
  have heq : (fun x : ℝ => x * (x / 2)) = fun x => (1 / 2 : ℝ) * x ^ 2 := by funext x; ring
  rw [heq, intervalIntegral.integral_const_mul, integral_pow]
  norm_num

/-- `exmp:2.9.3` — $E(3X^2-2X)=10/3$ para la misma densidad. -/
theorem exmp_2_9_3 : (∫ x in (0 : ℝ)..2, (3 * x ^ 2 - 2 * x) * (x / 2)) = 10 / 3 := by
  have heq : (fun x : ℝ => (3 * x ^ 2 - 2 * x) * (x / 2)) = fun x => (3 / 2 : ℝ) * x ^ 3 - x ^ 2 := by
    funext x; ring
  have hc1 : Continuous fun x : ℝ => (3 / 2 : ℝ) * x ^ 3 := (continuous_pow 3).const_mul (3 / 2)
  have hc2 : Continuous fun x : ℝ => x ^ 2 := continuous_pow 2
  rw [heq, intervalIntegral.integral_sub (hc1.intervalIntegrable 0 2) (hc2.intervalIntegrable 0 2),
    intervalIntegral.integral_const_mul (3 / 2 : ℝ) (fun x : ℝ => x ^ 3), integral_pow, integral_pow]
  norm_num

/-- `exmp:2.9.4` — $\mathrm{Var}(X)=2/9$ para la misma densidad. -/
theorem exmp_2_9_4 : (∫ x in (0 : ℝ)..2, (x - 4 / 3) ^ 2 * (x / 2)) = 2 / 9 := by
  have heq : (fun x : ℝ => (x - 4 / 3) ^ 2 * (x / 2))
      = fun x => (1 / 2 : ℝ) * x ^ 3 - (4 / 3 : ℝ) * x ^ 2 + (8 / 9 : ℝ) * x := by
    funext x; ring
  have hc1 : Continuous fun x : ℝ => (1 / 2 : ℝ) * x ^ 3 - (4 / 3 : ℝ) * x ^ 2 :=
    ((continuous_pow 3).const_mul (1 / 2)).sub ((continuous_pow 2).const_mul (4 / 3))
  have hc2 : Continuous fun x : ℝ => (8 / 9 : ℝ) * x := continuous_id.const_mul (8 / 9)
  have hc1a : Continuous fun x : ℝ => (1 / 2 : ℝ) * x ^ 3 := (continuous_pow 3).const_mul (1 / 2)
  have hc1b : Continuous fun x : ℝ => (4 / 3 : ℝ) * x ^ 2 := (continuous_pow 2).const_mul (4 / 3)
  rw [heq, intervalIntegral.integral_add (hc1.intervalIntegrable 0 2) (hc2.intervalIntegrable 0 2),
    intervalIntegral.integral_sub (hc1a.intervalIntegrable 0 2) (hc1b.intervalIntegrable 0 2),
    intervalIntegral.integral_const_mul (1 / 2 : ℝ) (fun x : ℝ => x ^ 3),
    intervalIntegral.integral_const_mul (4 / 3 : ℝ) (fun x : ℝ => x ^ 2),
    intervalIntegral.integral_const_mul (8 / 9 : ℝ) (fun x : ℝ => x), integral_pow, integral_pow,
    integral_id]
  norm_num

end EsperanzaMatematica
