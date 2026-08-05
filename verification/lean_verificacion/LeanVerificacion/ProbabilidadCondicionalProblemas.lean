import Mathlib.Tactic
import Mathlib.Data.Real.Basic

/-!
# Probabilidad condicional — problemas

Formaliza los problemas de `latex/probabilidad_condicional(p).tex`. Todos se
tratan, como el libro mismo lo hace, como aritmética directa de números
racionales/reales dados como datos (probabilidades ya conocidas), sin
necesidad de construir un espacio muestral discreto completo — es el mismo
estilo de cálculo que el libro usa para Monty Hall y el problema del
diagnóstico médico.

Cada cantidad **derivada** (no dato original del problema) se liga con `let` y
se reutiliza en los pasos siguientes, en vez de re-escribir su valor numérico
literal — así, si el libro cometiera un error de transcripción entre un paso y
el siguiente (p.ej. calcular $P(B')$ correctamente pero dividir entre un
número distinto al usarlo), el lema fallaría en vez de reproducir en silencio
el error. -/

namespace ProbabilidadCondicionalProblemas

/-- `prob:8794f31` (Recordar) — dados $P(A)=0.60$, $P(B)=0.50$,
$P(A\cap B)=0.30$: $P(A|B)=0.60$, $P(B|A)=0.50$, $P(A\cap B')=0.30$,
$P(A|B')=0.60$. Las cantidades derivadas $P(A\cap B')$ y $P(B')$ se ligan con
`let` y se usan (no se re-escriben) al calcular $P(A|B')$. -/
theorem prob_8794f31 :
    let PA : ℝ := 0.60
    let PB : ℝ := 0.50
    let PAB : ℝ := 0.30
    let PAcapBc := PA - PAB
    let PBc := 1 - PB
    (PAB / PB = 0.60) ∧ (PAB / PA = 0.50) ∧ (PAcapBc = 0.30) ∧
      (PAcapBc / PBc = 0.60) := by
  norm_num

/-- `prob:cf929e4` (Comprender) — urna con 5 rojas, 3 azules, extracción sin
reemplazo: $P(A)=5/8$, $P(B|A)=4/7$, $P(B|A')=5/7$, y por probabilidad total
$P(B) = (4/7)(5/8)+(5/7)(3/8) = 5/8 = P(A)$. El libro da el peso $P(A')=3/8$
directamente (3 azules de 8); se verifica esa igualdad como conjunto propio en
vez de sustituirla silenciosamente por `1 - PA`, para que un valor incorrecto
de $P(A')$ en el libro pudiera detectarse. -/
theorem prob_cf929e4 :
    let PA : ℚ := 5 / 8
    let PAc := 1 - PA
    let PBgA : ℚ := 4 / 7
    let PBgAc : ℚ := 5 / 7
    let PB := PBgA * PA + PBgAc * PAc
    PAc = 3 / 8 ∧ PB = 5 / 8 ∧ PB = PA := by
  norm_num

/-- `prob:52e63a3` (Aplicar) — control de calidad: $P(D) = (0.05)(0.70)+(0.10)(0.30)
= 0.065$, y $P(A|D) = P(D|A)P(A)/P(D) = 7/13 \approx 0.5385$ (tolerancia
$10^{-4}$ para la forma decimal, igualdad exacta para la fracción). El
numerador de Bayes, $P(D|A)P(A)$, se liga con `let` y se reutiliza (no se
re-escribe como `0.035`) al dividir entre $P(D)$. -/
theorem prob_52e63a3 :
    let PDgA : ℝ := 0.05
    let PA : ℝ := 0.70
    let PDgB : ℝ := 0.10
    let PB : ℝ := 0.30
    let PD := PDgA * PA + PDgB * PB
    let numBayes := PDgA * PA
    PD = 0.065 ∧ numBayes / PD = 7 / 13 ∧ |numBayes / PD - 0.5385| < 1e-4 := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  rw [abs_lt]; constructor <;> norm_num

/-- `prob:8a7282b` (Analizar), parte 2 — extracción de 4 cartas de palos
distintos: $1\times(39/51)\times(26/50)\times(13/49)\approx 0.1055$ (tolerancia
$10^{-4}$). La parte 1 (inducción de la regla de la cadena para $n$ eventos
arbitrarios) no se formaliza en general — ver bitácora de hallazgos — pero el
caso concreto de 4 eventos usado aquí sí es una instancia directa de dos
aplicaciones de `ProbabilidadCondicional.cond_mul_eq_inter`. -/
theorem prob_8a7282b_parte2 :
    |(1 : ℝ) * (39 / 51) * (26 / 50) * (13 / 49) - 0.1055| < 1e-4 := by
  rw [abs_lt]; constructor <;> norm_num

/-- `prob:c840e8f` (Evaluar) — la Paradoja de Monty Hall: dados $P(C_1)=P(C_2)=
P(C_3)=1/3$ y $P(A_3|C_1)=1/2$, $P(A_3|C_2)=1$, $P(A_3|C_3)=0$, por
probabilidad total $P(A_3)=1/2$, y por Bayes $P(C_1|A_3)=1/3$ (mantener) y
$P(C_2|A_3)=2/3$ (cambiar). $P(A_3)$ se liga con `let` (regla de probabilidad
total) y se reutiliza como denominador de ambas fórmulas de Bayes, en vez de
re-escribir `1/2` en cada una. -/
theorem prob_c840e8f :
    let pC1 : ℚ := 1 / 3
    let pC2 : ℚ := 1 / 3
    let pC3 : ℚ := 1 / 3
    let pA3gC1 : ℚ := 1 / 2
    let pA3gC2 : ℚ := 1
    let pA3gC3 : ℚ := 0
    let pA3 := pA3gC1 * pC1 + pA3gC2 * pC2 + pA3gC3 * pC3
    pA3 = 1 / 2 ∧ (pA3gC1 * pC1) / pA3 = 1 / 3 ∧ (pA3gC2 * pC2) / pA3 = 2 / 3 := by
  norm_num

/-- `prob:4241cab` (Crear) — falacia de la tasa base en diagnóstico médico:
$P(D)=0.01$, sensibilidad $0.95$, especificidad $0.90$ $\Rightarrow$
$P(D')=0.99$, $P(+) = (0.95)(0.01)+(0.10)(0.99) = 0.1085$, y $P(D|+) =
P(+|D)P(D)/P(+) \approx 0.0876$ (tolerancia $10^{-4}$). El libro da $P(D')=0.99$
explícitamente (complemento de la prevalencia $1\%$); se verifica esa igualdad
como conjunto propio en vez de sustituirla silenciosamente por `1 - PD`. El
numerador de Bayes, $P(+|D)P(D)$, se liga con `let` (no se re-escribe como
`0.0095`) y $P(+)$ se reutiliza como denominador. -/
theorem prob_4241cab :
    let PD : ℝ := 0.01
    let PDc := 1 - PD
    let sens : ℝ := 0.95
    let fpr : ℝ := 0.10
    let PPos := sens * PD + fpr * PDc
    let numBayes := sens * PD
    PDc = 0.99 ∧ PPos = 0.1085 ∧ |numBayes / PPos - 0.0876| < 1e-4 := by
  refine ⟨by norm_num, by norm_num, ?_⟩
  rw [abs_lt]; constructor <;> norm_num

end ProbabilidadCondicionalProblemas
