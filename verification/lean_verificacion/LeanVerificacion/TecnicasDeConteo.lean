import Mathlib.Tactic
import Mathlib.Data.Fintype.Card
import Mathlib.Data.Fintype.Prod
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Nat.Factorial.Basic

/-!
# Técnicas de conteo — verificación

Formaliza el teorema y los ejemplos de `latex/tecnicas_de_conteo.tex`: principio
de multiplicación, permutaciones (`Nat.descFactorial`), combinaciones
(`Nat.choose`), y los 4 ejemplos numéricos resueltos en el texto (menús,
medallas, comité, "flor" en póker), transcribiendo los números del libro tal
como están escritos.
-/

namespace TecnicasDeConteo

/-- Principio de multiplicación (2 operaciones) — el libro lo enuncia para $k$
operaciones sucesivas; aquí se formaliza el caso general de 2 tipos finitos
(instancia directa de `Fintype.card_prod` de Mathlib) y se verifica el ejemplo
concreto del libro (4 entradas × 6 platos fuertes × 3 postres = 72 menús). -/
theorem principio_multiplicacion (α β : Type*) [Fintype α] [Fintype β] :
    Fintype.card (α × β) = Fintype.card α * Fintype.card β :=
  Fintype.card_prod α β

/-- `exmp:conteo.1` — $4\times 6\times 3 = 72$ menús distintos. -/
theorem exmp_conteo_1 : Fintype.card (Fin 4 × Fin 6 × Fin 3) = 72 := by decide

/-- `eq:conteo.2` / `exmp:conteo.2` — $P(n,r) = n!/(n-r)!$, verificado en el
caso concreto del ejemplo del libro ($n=8,r=3$, medallas de oro, plata y
bronce entre 8 corredores): ambas formas de la definición ($n(n-1)\cdots$ vía
`Nat.descFactorial`, y $n!/(n-r)!$ vía división de factoriales) coinciden en
$336$. -/
theorem exmp_conteo_2 :
    Nat.descFactorial 8 3 = 336 ∧ (Nat.factorial 8 / Nat.factorial (8 - 3)) = 336 := by decide

/-- `eq:conteo.3` — $\binom{n}{r} = \frac{n!}{r!(n-r)!}$, la definición del
coeficiente binomial, formalizada vía `Nat.choose`. -/
theorem combinacion_def (n r : ℕ) (hr : r ≤ n) :
    n.choose r * Nat.factorial r * Nat.factorial (n - r) = Nat.factorial n :=
  Nat.choose_mul_factorial_mul_factorial hr

/-- Propiedad de simetría del coeficiente binomial: $\binom{n}{r}=\binom{n}{n-r}$. -/
theorem propiedad_simetria (n r : ℕ) (hr : r ≤ n) : n.choose r = n.choose (n - r) :=
  (Nat.choose_symm hr).symm

/-- Casos extremos: $\binom{n}{0}=\binom{n}{n}=1$. -/
theorem propiedad_casos_extremos (n : ℕ) : n.choose 0 = 1 ∧ n.choose n = 1 :=
  ⟨Nat.choose_zero_right n, Nat.choose_self n⟩

/-- `exmp:conteo.3` — $\binom{10}{4} = 210$ (comité de 4 de entre 10 candidatos). -/
theorem exmp_conteo_3 : Nat.choose 10 4 = 210 := by decide

/-- `exmp:conteo.4` — probabilidad de "flor" en póker: $\binom{52}{5}=2{,}598{,}960$,
$\binom{13}{5}=1{,}287$, $4\times 1{,}287 = 5{,}148$, y
$P(\text{flor}) = 5148/2598960 \approx 0.00198$ (verificado con tolerancia
$10^{-5}$, ya que el libro mismo usa $\approx$). -/
theorem exmp_conteo_4 :
    Nat.choose 52 5 = 2598960 ∧ Nat.choose 13 5 = 1287 ∧ 4 * 1287 = 5148 ∧
    |(5148 : ℚ) / 2598960 - 0.00198| < 1e-5 := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  rw [abs_lt]
  constructor <;> norm_num

end TecnicasDeConteo
