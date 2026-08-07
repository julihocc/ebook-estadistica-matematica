import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Integral.Bochner.Basic

/-!
# Función generadora de momentos — teoría

Formaliza `latex/funcion_generadora_momentos.tex`. **Tier D, no
formalizado:** `eq:2.8.12` (intercambiar derivada y esperanza, general
para cualquier `n`), el Teorema de Unicidad (resultado profundo del
problema de momentos), y el Teorema de Suma (`M_{X+Y}=M_X M_Y` para
independientes — depende de la misma maquinaria `IndepFun` bloqueada por
MAX_PATH en este worktree, ver `EsperanzaMatematica.lean`). El ejemplo
de la Normal (`exmp:2.8.5`) reutiliza la identidad de completar-el-cuadrado
ya probada en `DistribucionNormal.mgf_exponente` — no se repite; su
cierre completo (evaluar la integral gaussiana desplazada) es Tier D por
la misma razón documentada en `DistribucionNormal.lean`.
-/

namespace FuncionGeneradoraMomentos

open MeasureTheory

/-- `exmp:2.8.4` — FGM de Bernoulli$(p)$: $M_X(t)=(1-p)+pe^t$, con
derivada $M_X'(t)=pe^t$ (general en $t$, no solo en $t=0$; la derivada de
$pe^t$ es de nuevo $pe^t$, así que la misma fórmula da $M_X''(t)$). -/
theorem exmp_2_8_4_derivada (p t : ℝ) :
    HasDerivAt (fun t => (1 - p) + p * Real.exp t) (p * Real.exp t) t := by
  have h : HasDerivAt (fun t => (1 - p) + p * Real.exp t) (0 + p * Real.exp t) t :=
    (hasDerivAt_const t (1 - p)).add ((Real.hasDerivAt_exp t).const_mul p)
  rwa [zero_add] at h

/-- `exmp:2.8.4` — $E[X]=M_X'(0)=p$, $E[X^2]=M_X''(0)=p$ (misma fórmula
$pe^t$ evaluada en $0$), $\mathrm{Var}(X)=p-p^2=p(1-p)$. -/
theorem exmp_2_8_4_momentos (p : ℝ) :
    p * Real.exp (0 : ℝ) = p ∧ p - p ^ 2 = p * (1 - p) := by
  constructor
  · simp
  · ring

/-- `exmp:2.8.6` — FGM de $\mathrm{Exp}(\lambda)$: $M_X(t)=\lambda/(\lambda-t)$
para $t<\lambda$, general. -/
theorem exmp_2_8_6_mgf (lam t : ℝ) (hlam : 0 < lam) (ht : t < lam) :
    (∫ x in Set.Ioi (0 : ℝ), Real.exp (t * x) * (lam * Real.exp (-lam * x)))
      = lam / (lam - t) := by
  have heq : (fun x : ℝ => Real.exp (t * x) * (lam * Real.exp (-lam * x)))
      = fun x => lam * Real.exp ((t - lam) * x) := by
    funext x
    rw [show (t - lam) * x = t * x + -lam * x by ring, Real.exp_add]
    ring
  rw [heq, MeasureTheory.integral_const_mul, integral_exp_mul_Ioi (show t - lam < 0 by linarith)]
  simp only [mul_zero, Real.exp_zero]
  have hne : lam - t ≠ 0 := by linarith
  have hne' : t - lam ≠ 0 := by intro h; apply hne; linarith
  field_simp
  ring

/-- `prob:cf5e60c` (Analizar) — para $Y=aX+b$, $M_Y(t)=e^{bt}M_X(at)$,
general para cualquier densidad $f$ (no requiere $a\ne0$ ni hipótesis de
integrabilidad — `MeasureTheory.integral_const_mul` es incondicional). -/
theorem prob_cf5e60c_general (f : ℝ → ℝ) (a b t : ℝ) :
    (∫ x, Real.exp (t * (a * x + b)) * f x) = Real.exp (b * t) * ∫ x, Real.exp (t * a * x) * f x := by
  have heq : (fun x : ℝ => Real.exp (t * (a * x + b)) * f x)
      = fun x => Real.exp (b * t) * (Real.exp (t * a * x) * f x) := by
    funext x
    rw [show t * (a * x + b) = b * t + t * a * x by ring, Real.exp_add]
    ring
  rw [heq, MeasureTheory.integral_const_mul]

/-- `prob:a48cc99` (Crear) — FGM de $U(0,1)$: $M_X(t)=(e^t-1)/t$ para
$t\ne0$, general. -/
theorem prob_a48cc99_mgf (t : ℝ) (ht : t ≠ 0) :
    (∫ x in (0 : ℝ)..1, Real.exp (t * x)) = (Real.exp t - 1) / t := by
  have hderiv : ∀ x ∈ Set.uIcc (0 : ℝ) 1,
      HasDerivAt (fun x => Real.exp (t * x) / t) (Real.exp (t * x)) x := by
    intro x _
    have h1 : HasDerivAt (fun x : ℝ => t * x) t x := by
      simpa using (hasDerivAt_id x).const_mul t
    have h2 : HasDerivAt (fun x : ℝ => Real.exp (t * x)) (Real.exp (t * x) * t) x :=
      (Real.hasDerivAt_exp (t * x)).comp x h1
    have h3 : HasDerivAt (fun x : ℝ => Real.exp (t * x) / t) (Real.exp (t * x) * t / t) x :=
      h2.div_const t
    rwa [mul_div_assoc, div_self ht, mul_one] at h3
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv
      (Continuous.intervalIntegrable (by fun_prop) 0 1)]
  simp only [mul_one, mul_zero, Real.exp_zero]
  ring

end FuncionGeneradoraMomentos
