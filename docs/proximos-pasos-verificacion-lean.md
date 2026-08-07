# Próximos pasos: verificación formal con Lean 4 + Mathlib

Documento de seguimiento de alto nivel para el proyecto de verificación
formal del libro (rama `verify-result-with-lean`). El detalle capítulo por
capítulo (tablas de afirmaciones, tiers, notas técnicas de Lean) vive en
`docs/verificacion-lean-hallazgos.md`; este archivo es el resumen ejecutivo
y el plan de continuación, siguiendo la misma convención que
`docs/proximos-pasos-2026-07-22.md` para la migración de presentaciones.

## Estado al 2026-08-07 16:40:09 -06:00

### Resumen de la sesión

Se procesaron y confirmaron (commit) **13 capítulos** en esta sesión, en
orden `\input` del libro, cubriendo el resto de la Unidad 3 (Variables
Aleatorias Continuas) y la mayor parte de la Unidad 4 (Distribuciones de
Muestreo):

1. `variables_discretas_ciencia_datos` (commit `5ed9f72`)
2. `variables_aleatorias_continuas` (commit `402df6a`)
3. `esperanza_matematica` (commit `2c6976c`; hallazgos corregidos en commit `34c514f`)
4. `distribucion_uniforme_continua` (commit `31e48b7`)
5. `distribucion_normal` (commit `e65f57f`)
6. `distribuciones_tipo_gamma` (commit `b5b5bff`)
7. `funcion_generadora_momentos` (commit `2e9ed82`)
8. `transformacion_variables` (commit `bb52b6a`; + `introduccion_estadistica_inferencial`, sin `(p)`, solo prosa)
9. `distribuciones_funciones_variable_aleatoria` (commit `61f7dd6`)
10. `distribuciones_muestrales_medias` (commit `78a5a34`)
11. `distribucion_muestral_chi_cuadrada` (commit `5e8e0c9`)
12. `distribucion_muestral_t` (commit `634e147`)
13. `distribucion_muestral_f` (commit `fe044a3`)

14 commits en total (13 capítulos + 1 commit de corrección de hallazgos).

Cada capítulo siguió el mismo flujo: lectura de teoría + `(p)`, triage en
tiers A/B/C/D, prueba en Lean, `lake build` completo, verificación EN por
`diff` de etiquetas y literales numéricos, actualización de
`docs/verificacion-lean-hallazgos.md` y de la memoria persistente del
proyecto, y commit individual.

**Estado del build:** `lake build` en `verification/lean_verificacion/`
pasa en verde — **3458/3458 jobs, cero `sorry`, cero errores** — al cierre
de `distribucion_muestral_f` (commit `fe044a3`).

### Hallazgos nuevos confirmados esta sesión

- **`esperanza_matematica`** (3 hallazgos, **ya corregidos** en ES y EN,
  aprobado explícitamente por el usuario): `exmp:2.9.1` (\$30 vs. \$60 en
  el enunciado del juego del dado), `prob:f43c638` (fórmula $1/\lambda^2$
  vs. $2/\lambda^2$), `prob:7b147c4` ($n=100$ vs. $n=101$ en el límite de
  la desigualdad estricta).
- **`distribucion_muestral_t`** (`prob:c34507c`, **pendiente de
  corrección**): suma de cuadrados de desviaciones $0.3033$ en el libro
  vs. $1/3\approx0.3333$ exacto; se propaga a $S^2$, $S$, error estándar,
  margen e intervalo de confianza final.
- **`distribucion_muestral_f`** (`exmp:3.2.6`, **pendiente de
  corrección**): dos errores aritméticos en el ejemplo de ANOVA —
  $\mathrm{SC}_{\text{trat}}=290.0$ (correcto: $281.2$) y suma de
  cuadrados intra-grupo del Método C $=23.2$ (correcto: $29.2$); se
  propagan a $\mathrm{SC}_{\text{error}}$ y al estadístico $F$
  ($8.955$ correcto vs. $9.54$ del libro). La conclusión cualitativa de
  la prueba (rechazar $H_0$) sobrevive por casualidad.

Todos los hallazgos nuevos se verificaron independientemente (Python
`fractions.Fraction` o `scipy`) antes de escribir la prueba de Lean que
los documenta, y se confirmó que están presentes idénticos en el espejo
EN (fuente compartida, no error de traducción) en cada caso.

### Hallazgos acumulados aún pendientes de decisión del usuario

Ninguno de estos se ha corregido en `.tex` — están reportados en la
bitácora únicamente, a la espera de aprobación explícita por hallazgo:

| Hallazgo | Capítulo | Descripción |
|---|---|---|
| `eq:2.10.8` | `distribucion_multinomial` | Fórmula del PMF sin el factorial en el numerador |
| `prob:33bf5d2` | `distribucion_multinomial` | Valor numérico erróneo por ~$10^{42}$ |
| `prob:7cf587b` | `distribucion_hipergeometrica` | $0.189725$ vs. $0.189525$ |
| `prob:969b25a` | `distribucion_hipergeometrica` | $\mathrm{Var}(X)\approx1.5254$ vs. $1.5252$ |
| `prob:8dad711` (numérico) | `distribucion_poisson` | $0.2815$ vs. $0.28163$ (redondeo) |
| `prob:5e9408a` | `distribucion_poisson` | **El más sustancial**: invierte la conclusión pedagógica sobre la calidad de la aproximación Normal |
| `prob:c34507c` | `distribucion_muestral_t` | Suma de cuadrados $0.3033$ vs. $0.3333$ |
| `exmp:3.2.6` (×2) | `distribucion_muestral_f` | $\mathrm{SC}_{\text{trat}}$ y SS del Método C en el ejemplo de ANOVA |

### Cobertura — capítulos aún sin procesar

**Gap previo al piloto** (en el orden real de `\input` del libro, antes de
`fundamentos_de_probabilidad`): `introduccion_estadistica_descriptiva`,
`medidas_tendencia_central`, `medidas_dispersion`, `introduccion_probabilidad`,
`conjuntos` — y sus 5 pares `(p)`. Se saltaron deliberadamente al elegir el
piloto por riqueza axiomática, no por posición en el libro. Quedan
pendientes de una pasada posterior.

**Resto del libro tras `distribucion_muestral_f`**: quedan por procesar los
archivos de teoría/problemas restantes de las Unidades 4 (cierre de
Distribuciones de Muestreo) en adelante, y las Unidades 5+ (Inferencia,
regresión, etc., según la estructura del `\input` del master file).

## Plan de continuación (próximo paso inmediato)

1. **Próximo capítulo: `distribuciones_muestreo_ciencia_datos`** (teoría +
   `(p)`) — siguiente en el orden `\input` tras `distribucion_muestral_f`.
2. Continuar capítulo por capítulo con el mismo flujo (triage → Lean →
   `lake build` → diff EN → bitácora → memoria → commit), **sin pausar a
   reportar entre capítulos** — instrucción explícita del usuario de esta
   sesión ("no pares, solo haz commits al final de cada paso").
3. Cuando se agote el resto del libro en orden `\input`, retomar el gap
   de 5 archivos que precede al piloto (arriba).
4. Los hallazgos confirmados se siguen reportando en
   `docs/verificacion-lean-hallazgos.md` pero **no se corrigen** salvo
   aprobación explícita del usuario por hallazgo — como ya ocurrió una
   vez con los 3 de `esperanza_matematica`.
5. Este archivo (`proximos-pasos-verificacion-lean.md`) se debe actualizar
   al cierre de cada bloque de trabajo significativo (no necesariamente
   cada capítulo individual, para no duplicar el detalle que ya vive en
   la bitácora), siguiendo el mismo patrón de secciones fechadas que
   `docs/proximos-pasos-2026-07-22.md`.

No se hizo `git push`. Todos los commits de esta sesión están en la rama
local `verify-result-with-lean`.
