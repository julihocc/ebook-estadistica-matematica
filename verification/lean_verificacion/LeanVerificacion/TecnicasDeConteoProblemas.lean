import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Factorial.Basic

/-!
# Técnicas de conteo — problemas

Formaliza los problemas de `latex/tecnicas_de_conteo(p).tex`. `prob:6369f2a`
(Recordar) solo pide enunciar fórmulas en prosa, sin contenido formalizable
más allá de lo ya cubierto en `TecnicasDeConteo.lean`.
-/

namespace TecnicasDeConteoProblemas

/-- `prob:4f6f981` (Comprender) — $5\times 4\times 2 = 40$ menús. -/
theorem prob_4f6f981 : Fintype.card (Fin 5 × Fin 4 × Fin 2) = 40 := by decide

/-- `prob:490657c` (Aplicar) — $P(10,3)=720$, $\binom{10}{3}=120$, y
$P(10,3) = 3! \times \binom{10}{3}$ (720 = 6×120). -/
theorem prob_490657c :
    Nat.descFactorial 10 3 = 720 ∧ Nat.choose 10 3 = 120 ∧
    Nat.descFactorial 10 3 = Nat.factorial 3 * Nat.choose 10 3 := by
  refine ⟨by decide, by decide, by decide⟩

/-- `prob:d8ce0cf` (Analizar) — $\binom{5}{2}\times\binom{5}{2} = 10\times 10 = 100$
comités posibles (Dr. Pérez fijo, 2 hombres restantes de 5, 2 mujeres de 5). -/
theorem prob_d8ce0cf : Nat.choose 5 2 * Nat.choose 5 2 = 100 := by decide

/-- `prob:3007304` (Evaluar) — el estudiante afirma que asignar 3 roles
distintos entre 8 candidatos es $\binom{8}{3}=56$; esto es incorrecto porque
subcuenta por un factor $3!=6$: el cálculo correcto es la permutación
$P(8,3)=336$, y en efecto $336 = 6\times 56 \neq 56$. -/
theorem prob_3007304 :
    Nat.choose 8 3 = 56 ∧ Nat.descFactorial 8 3 = 336 ∧
    Nat.descFactorial 8 3 = Nat.factorial 3 * Nat.choose 8 3 ∧
    Nat.descFactorial 8 3 ≠ Nat.choose 8 3 := by
  refine ⟨by decide, by decide, by decide, by decide⟩

/-- `prob:b53268b` (Crear) — probabilidad de "dos pares" en póker:
$\binom{13}{2}=78$, $\binom{4}{2}^2=36$, $\binom{11}{1}=11$, $\binom{4}{1}=4$,
producto $=123{,}552$, y $P(\text{dos pares}) = 123552/2598960 \approx 0.0475$
(tolerancia $10^{-4}$, el libro mismo usa $\approx$). -/
theorem prob_b53268b :
    Nat.choose 13 2 = 78 ∧ (Nat.choose 4 2) ^ 2 = 36 ∧ Nat.choose 11 1 = 11 ∧
    Nat.choose 4 1 = 4 ∧ 78 * 36 * 11 * 4 = 123552 ∧ Nat.choose 52 5 = 2598960 ∧
    |(123552 : ℚ) / 2598960 - 0.0475| < 1e-4 := by
  refine ⟨by decide, by decide, by decide, by decide, by decide, by decide, ?_⟩
  rw [abs_lt]
  constructor <;> norm_num

end TecnicasDeConteoProblemas
