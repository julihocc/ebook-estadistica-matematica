# Diagnóstico de los cuadernos de problemas (`latex/*(p).tex`, Caps. 2-8, ES)

**Fecha:** 2026-07-20
**Alcance:** solo diagnóstico de solo lectura. No se modificó ningún archivo `.tex` existente. No se compiló nada nuevo — todo lo aquí reportado se extrajo del `[Modelación Estadística].aux` ya compilado tras la sesión anterior.
**Fuera de alcance de este documento:** capítulo 1 (Estadística Descriptiva) y capítulo 9 (Regresiones), suplementarios y fuera del temario oficial MA1001B; el espejo en inglés (`en_*(p).tex`).

## Resumen ejecutivo

La restructuración de teoría del 2026-07-20 alineó cada `\section` de los capítulos 2-8 al temario MA1001B, pero **no tocó los 19 archivos `(p).tex`** correspondientes — quedó explícitamente fuera de alcance. El resultado, confirmado contra el `.aux` compilado:

- **255 de 315 etiquetas `\label{prob:X.Y.Z}` con nombre numérico (81 %) compilan con un número de sección distinto al que su propio nombre sugiere.** No es un problema marginal: es el estado normal, no la excepción.
- **5 secciones del temario tienen cero problemas**: 2.2 (Técnicas de conteo), 7.2 (Relación IC↔pruebas), 7.4 (Prueba t, varianza desconocida), y dentro de 8.5, los subtemas de cuadrados latinos/grecolatinos; 8.6 (Diseños factoriales) también en cero.
- **Bug activo y visible en el PDF, no solo teórico**: `distribuciones_especiales(p).tex` y `chi_cuadrada(p).tex` reutilizan por accidente los mismos 5 nombres de etiqueta (`prob:3.9.1`–`prob:3.9.5`). Como `chi_cuadrada` se procesa después, sus valores ganan la resolución de `\ref`, y las pistas de solución dentro de `distribuciones_especiales(p).tex` (que citan `\ref{prob:3.9.1}` esperando referirse a su propio Problema 3.7.51) imprimen erróneamente "7.9.1" — un problema de un capítulo completamente distinto (independencia $\chi^2$). Esto ya está en el PDF compilado, no es hipotético.
- **La mayoría de los cuadernos concentran sus problemas en la última sección real que los precede**, no en la sección a la que temáticamente pertenecen: 70 problemas de `distribuciones_especiales(p).tex` (que cubren 6 distribuciones distintas) aparecen todos bajo "3.7 Ciencia de Datos"; 40 de `variables_aleatorias_continuas_avanzado(p).tex` bajo "4.6 FGM"; 50 de `distribuciones_muestreo_avanzado(p).tex` bajo "5.7 Ciencia de Datos".

## 1. Tabla maestra por archivo

Orden real de `\input{}` en el maestro. "Patrón" es **A** (bloque en línea, sin `\section` propio — hereda el número de lo último que precede) o **B** (el archivo declara su propio `\section{Problemas resueltos...}`, con número dedicado).

| Archivo | Sección(es) de teoría que cubre temáticamente | # Problemas | Patrón | Estilo de `\label` (ejemplos) | ¿Mezcla temas sin separar? |
|---|---|---|---|---|---|
| `conjuntos(p).tex` | 2.1 Teoría de conjuntos | 10 | A | `prob:2.1.1`…`.10` | No |
| `fundamentos_de_probabilidad(p).tex` | 2.1 (subsección, sin `\section` propio) | 10 | A | `prob:2.3.1`…`.10` | No (pero etiqueta intenta "2.3", tema real es 2.1) |
| `probabilidad_condicional(p).tex` | 2.3 Probabilidad condicional y Bayes | 10 | A | `prob:2.4.1`…`.10` | No |
| `teorema_de_bayes(p).tex` | 2.3 (subsección, sin `\section` propio) | 10 | A | `prob:2.5.1`…`.10` | No (etiqueta intenta "2.5", tema real es 2.3) |
| `muestreo_aleatorio(p).tex` | 2.4 Muestreo aleatorio | 10 | A | `prob:2.6.1`…`.10` | No |
| `variables_aleatorias_discretas(p).tex` | 3.1 (PMF+CDF+Esperanza, fusionadas en 1 sección) | 30 | A | `prob:3.1.x`/`3.2.x`/`3.3.x` (3 sub-bloques) | Ya no — la teoría se fusionó en 1 sola sección real |
| `distribuciones_especiales(p).tex` | 3.2-3.7 (Binomial, Multinomial, Geom./BinNeg, Hipergeom., Poisson, CienciaDatos) — **6 secciones reales** | 70 | A | `prob:3.4.x`…`prob:3.10.x` (7 sub-bloques rotulados "Sección 03.04"-"03.10") | **Sí** — 70 problemas de 6 distribuciones distintas, todos cayendo bajo la última sección (3.7) |
| `variables_aleatorias_continuas(p).tex` | 4.1 (PDF+CDF, fusionadas en 1 sección) | 20 | A | `prob:4.1.x`/`4.2.x` (2 sub-bloques) | Ya no — teoría fusionada |
| `esperanza_matematica(p).tex` | 4.2 Valor esperado | 10 | A | `prob:4.3.1`…`.10` | No |
| `variables_aleatorias_continuas_avanzado(p).tex` | 4.3-4.6 (Uniforme, Normal, Gamma-tipo, FGM) — **4 secciones reales** | 40 | A | `prob:4.4.x`…`prob:4.7.x` (4 sub-bloques) | **Sí** — 40 problemas de 4 distribuciones, todos bajo la última sección (4.6) |
| `distribuciones_muestreo_avanzado(p).tex` | 5.1-5.7 (Transf., dist.func.VA, dist.muestrales medias, $\chi^2$, $t$, $F$, CienciaDatos) — **7 secciones reales** | 50 | A | `prob:5.1.x`…`prob:5.5.x` (5 sub-bloques) | **Sí** — 50 problemas de 5+ subtemas, todos bajo la última sección (5.7) |
| `estadisticos_z_t(p).tex` | Cuelga de `estadisticos_z_t.tex`, `\section*` sin numerar | 10 | A | `prob-z-1`, `prob-t-1`, `prob-z-t-new1` (semántico, sin dos puntos) | No, pero cuelga de sección no numerada → cae también en 5.7 |
| `estimacion_puntual(p).tex` | 6.1 Métodos de estimación puntual | 40 | A | 1er bloque semántico (`prob:estim-fund-1`, `prob:mle_*`, `prob:mom_*`) + 3 sub-bloques `prob:6.1.x`/`6.2.x`/`6.3.x` | Internamente sí (4 sub-bloques con intención de 4 subtemas), pero todos caen correctamente en 6.1 |
| `intervalos_de_confianza(p).tex` | 6.2 Estimación por intervalo | 10 | A | `prob-ic-1`…`prob-ic-desaf-epistemologia` (semántico) | No — cae correctamente en 6.2 |
| `estimacion_intervalos_avanzado(p).tex` | 6.3-6.7 (media/dif.medias, errores estándar, proporción, varianza, tamaño muestra) — **5 secciones reales** | 10 | **B** (`\section{Problemas resueltos...}` = 6.8) | `prob:n_media`, `prob:ic_varianza`, etc. (semántico) | **Sí** — 10 problemas para 5 subtemas distintos, sin segmentar, aunque en sección dedicada |
| `pruebas_de_hipotesis(p).tex` | Temáticamente 7.1 (Elementos), cae en 7.3 (Valores P) | 10 | A | `prob:7.1.1`…`.10` | No cubre 7.2 (Relación IC/pruebas) ni deja rastro en 7.3 real |
| `chi_cuadrada(p).tex` | 7.8-7.9 (Bondad de ajuste, Independencia) — **2 secciones reales** | 10 | A | `prob:3.9.1`…`.5` (⚠️ **duplicados con `distribuciones_especiales(p).tex`**) + `prob:chi-*` (semántico) | **Sí** — bondad de ajuste e independencia mezclados, todos caen en 7.9 |
| `pruebas_hipotesis_avanzadas(p).tex` | Temáticamente 7.5-7.7 y 7.10-7.11 (dos medias/proporciones/varianzas + homogeneidad/Marascuilo, hoy repartidos en 2 archivos de teoría distintos) | 10 | **B** (`\section{Problemas resueltos...}` = 7.12) | `prob:doc_dos_medias_iguales`, `prob:homogeneidad_contingencia`, etc. (semántico) | **Sí** — mezcla temas que hoy viven en `pruebas_hipotesis_avanzadas.tex` (6.5-6.7) y en `pruebas_homogeneidad_varias_proporciones.tex` (6.10-6.11) |
| `diseno_experimentos_anova(p).tex` | Temáticamente 8.2-8.5 (ANOVA 1 factor, post-hoc, adecuación, DBCA) | 13 | **B** (`\section{Problemas resueltos...}` = 8.7) | `prob:anova_un_factor_ml`, `prob:dbca_servidores`, `prob:bartlett_*`, etc. (semántico) | **Sí** — mezcla 4 subtemas; no toca cuadrados latinos/grecolatinos (8.5) ni factoriales (8.6) |

**Nota sobre el Patrón B:** solo 3 de los 19 archivos (`estimacion_intervalos_avanzado(p)`, `pruebas_hipotesis_avanzadas(p)`, `diseno_experimentos_anova(p)`) declaran su propio `\section{Problemas resueltos de ...}`, lo que les da un número de sección real y dedicado en la tabla de contenidos (6.8, 7.12, 8.7 respectivamente). Los otros 16 son bloques "en línea" que heredan el número de lo último que los precede — ahí es donde ocurre casi todo el desfase de la sección 2.

## 2. Verificación cuantificada del desfase de numeración (Fase D)

Metodología: para cada `\label{prob:X.Y.Z}` cuyo nombre sigue el patrón numérico `X.Y.Z`, se comparó el prefijo de sección que el nombre *sugiere* (`X.Y`) contra el prefijo real que LaTeX le asignó, leído directamente de `\newlabel{...}` en el `.aux` (tomando la última ocurrencia — la que realmente gana la resolución de `\ref` en el documento compilado).

```
Total de etiquetas prob: en Caps. 2-8 .......... 383
  Con nombre numérico X.Y.Z (comparables) ....... 315
    Coinciden (sección sugerida = sección real) ..  60  (19 %)
    NO coinciden ................................ 255  (81 %)
  Con nombre semántico (sin número que comparar) ..  68
```

Los 60 casos que "coinciden" son casi todos el primer sub-bloque de cada archivo (ej. `prob:2.1.1`–`.10`, `prob:3.1.1`–`.10`, `prob:4.1.1`–`.10`, `prob:5.1.1`–`.10`) — coinciden por ser el bloque que abre el archivo, no porque el archivo esté bien anclado.

### Ejemplos representativos del desfase

| Etiqueta | Sección que sugiere | Sección real compilada | Archivo |
|---|---|---|---|
| `prob:2.3.1` | 2.3 | **2.1** | `fundamentos_de_probabilidad(p).tex` |
| `prob:2.6.1` | 2.6 | **2.4** | `muestreo_aleatorio(p).tex` |
| `prob:3.4.1` | 3.4 | **3.7** | `distribuciones_especiales(p).tex` |
| `prob:3.9.1` | 3.9 | **3.7.51** (o **7.9.1**, ver §2.1) | `distribuciones_especiales(p).tex` / `chi_cuadrada(p).tex` |
| `prob:4.7.10` | 4.7 | **4.6** | `variables_aleatorias_continuas_avanzado(p).tex` |
| `prob:5.5.10` | 5.5 | **5.7** | `distribuciones_muestreo_avanzado(p).tex` |
| `prob:6.3.10` | 6.3 | **6.1** | `estimacion_puntual(p).tex` |
| `prob:7.1.1` | 7.1 | **7.3** | `pruebas_de_hipotesis(p).tex` |

### 2.1 Hallazgo aparte: colisión activa de etiquetas duplicadas

`prob:3.9.1` a `prob:3.9.5` están **definidos dos veces** — una en `distribuciones_especiales(p).tex` (problemas propios, sección real 3.7) y otra en `chi_cuadrada(p).tex` (problemas propios, sección real 7.9). El compilador ya avisa "Label ... multiply defined" para los 5. Como `chi_cuadrada` se procesa después en el `\input`, su valor sobrescribe al anterior en el `.aux`, así que **cualquier `\ref{prob:3.9.1}` en el documento resuelve a 7.9.1**, sin importar cuál de los dos problemas se quiso citar.

Esto no es solo una advertencia dormida: `distribuciones_especiales(p).tex` cita `\ref{prob:3.9.1}`…`\ref{prob:3.9.5}` **dentro de sus propias Sugerencias y Soluciones**, esperando referirse a sus propios problemas 3.7.51-3.7.55. En el PDF compilado, esas pistas dicen literalmente "Para el Problema 7.9.1..." en vez de "Para el Problema 3.7.51...", apuntando al lector hacia un problema de bondad de ajuste/independencia $\chi^2$ que no tiene nada que ver. Confirmado en ambos idiomas (`distribuciones_especiales(p).tex` y `en_distribuciones_especiales(p).tex` tienen el mismo patrón de cita interna).

## 3. Mapa de cobertura por sección del temario (Caps. 2-8)

| Sección | Título compilado | Archivo(s) `(p).tex` que aportan problemas aquí | # Problemas físicos aquí |
|---|---|---|---|
| 2.1 | Teoría de conjuntos... | `conjuntos(p)` + `fundamentos_de_probabilidad(p)` | 20 |
| **2.2** | **Técnicas de conteo** | — | **0** |
| 2.3 | Probabilidad condicional y regla de Bayes | `probabilidad_condicional(p)` + `teorema_de_bayes(p)` | 20 |
| 2.4 | Muestreo aleatorio | `muestreo_aleatorio(p)` | 10 |
| 3.1 | Distribución de probabilidad discreta | `variables_aleatorias_discretas(p)` | 30 |
| 3.2-3.6 | Binomial, Multinomial, Geom./BinNeg, Hipergeom., Poisson | — (temáticamente cubiertas, pero físicamente en 3.7) | 0 directamente |
| 3.7 | V.A. discretas y ciencia de datos | `distribuciones_especiales(p)` (todo el archivo) | 70 |
| 4.1 | Función de densidad | `variables_aleatorias_continuas(p)` | 20 |
| 4.2 | Valor esperado | `esperanza_matematica(p)` | 10 |
| 4.3-4.5 | Uniforme, Normal, Gamma-tipo | — (temáticamente cubiertas, pero físicamente en 4.6) | 0 directamente |
| 4.6 | Función generadora de momentos | `variables_aleatorias_continuas_avanzado(p)` (todo el archivo) | 40 |
| 5.1-5.6 | Transf., dist.func.VA, medias, $\chi^2$, $t$, $F$ | — (temáticamente cubiertas, pero físicamente en 5.7) | 0 directamente |
| 5.7 | Dist. de muestreo y ciencia de datos | `distribuciones_muestreo_avanzado(p)` + `estadisticos_z_t(p)` | 60 |
| 6.1 | Métodos de estimación puntual | `estimacion_puntual(p)` | 40 |
| 6.2 | Estimación por intervalo | `intervalos_de_confianza(p)` | 10 |
| 6.3-6.7 | Media, errores estándar, proporción, varianza, tamaño muestra | — (temáticamente cubiertas, pero físicamente en 6.8) | 0 directamente |
| 6.8 | Problemas resueltos (estimación por intervalos) | `estimacion_intervalos_avanzado(p)` | 10 |
| 7.1 | Elementos de prueba de hipótesis | — (etiquetas dicen "7.1", pero caen físicamente en 7.3) | 0 directamente |
| **7.2** | **Relación IC↔pruebas de hipótesis** | — | **0** |
| 7.3 | Uso de los valores P | `pruebas_de_hipotesis(p)` (todo el archivo) | 10 |
| **7.4** | **Prueba t (varianza desconocida)** | — | **0** |
| 7.5-7.7 | Dos medias, proporciones, varianzas | — (temáticamente cubiertas, pero físicamente en 7.12) | 0 directamente |
| 7.8 | Bondad de ajuste | — (temáticamente cubierta, pero físicamente en 7.9) | 0 directamente |
| 7.9 | Independencia | `chi_cuadrada(p)` (todo el archivo, incluye bondad de ajuste) | 10 |
| 7.10-7.11 | Homogeneidad, varias proporciones | — (temáticamente cubiertas, pero físicamente en 7.12) | 0 directamente |
| 7.12 | Problemas resueltos (docimasia avanzada) | `pruebas_hipotesis_avanzadas(p)` | 10 |
| 8.1-8.4 | Estrategias, ANOVA 1 factor, efectos, residuos | — (temáticamente cubiertas, pero físicamente en 8.7) | 0 directamente |
| **8.5** | **DBCA + cuadrados latinos/grecolatinos** | — (DBCA cubierta indirectamente vía 8.7; **latinos/grecolatinos: 0**) | 0 directamente |
| **8.6** | **Diseños factoriales** | — | **0** |
| 8.7 | Problemas resueltos (DoE y ANOVA) | `diseno_experimentos_anova(p)` | 13 |

**Secciones con cero problemas, directa o indirectamente: 2.2, 7.2, 7.4, 8.6, y los subtemas de cuadrados latinos/grecolatinos dentro de 8.5.** (Coincide exactamente con las 5 secciones de contenido nuevo redactadas en la tarea anterior — nunca tuvieron cuaderno de problemas propio.)

## 4. Aclaración: los rótulos "Sección XX.YY" no son la numeración del temario

Varios archivos (`distribuciones_especiales(p)`, `variables_aleatorias_continuas(p)`/`variables_aleatorias_continuas_avanzado(p)`, `distribuciones_muestreo_avanzado(p)`, `estimacion_puntual(p)`, `pruebas_de_hipotesis(p)`) tienen sub-bloques con comentarios/subtítulos tipo "Sección 03.04" o "Sugerencias — Sección 03.02". **Esa numeración pertenece a los mazos de `presentaciones/` (convención de la Fase G), no al temario MA1001B ni a la numeración real del libro.** Por ejemplo, "Sección 03.04" en `distribuciones_especiales(p).tex` se refiere al mazo `presentaciones/es/03_variables_aleatorias_discretas/03.04_....tex`, mientras que la sección real del libro donde ese bloque de problemas termina cayendo es "3.7" (ver §1 y §3). Confundir ambos sistemas de numeración al planear la siguiente tarea produciría un mapeo incorrecto.

## 5. Contraste: convención vieja (actual) vs. nueva (decidida, no ejecutada)

Según `CHANGELOG.md`, entrada `2026-07-18`, "Reorganización de cuadernos de problemas... decisión de alcance, no ejecutada aún":

| | Convención vieja (la que existe hoy, ver §1) | Convención nueva (decidida el 2026-07-18, sin ejecutar) |
|---|---|---|
| Alcance del archivo | 1 archivo `(p).tex` cubre varias `\section` (a veces todo un capítulo) | 1 archivo `(p).tex` por cada `\section` real (mapeo 1:1) |
| Cantidad de problemas | 10 fijos, taxonomía "3-3-2-2" | 3-6 flexibles, priorizando variedad sobre conteo |
| Encabezados de dificultad | `\subsubsection*{Nivel Fundamental}` etc., **visibles** en el PDF | Comentario LaTeX `% Nivel Fundamental`, invisible en el PDF |
| Mazos (`presentaciones/`) | "Ejercicio en Clase" cita un problema del cuaderno | Se reemplaza por ejemplos ya resueltos en la teoría (`\ejemplo`/`\solucion`) |
| Alcance retroactivo declarado | — | Caps. 3-5 (ya reestructurados en julio) + Caps. 6-9 hacia adelante |

El CHANGELOG registra explícitamente: *"Estado: solo documentado, sin ejecutar... la ejecución se retomará un paso a la vez, empezando por un piloto en una sola sección pequeña."* Es decir, esta decisión llevaba dos días sin tocarse incluso antes de la restructuración de teoría del día 20, que la dejó todavía más desalineada.

## 6. Recomendaciones — rutas de ejecución posibles

No se ejecuta ninguna de estas en este documento; se listan para elegir sin tener que re-derivar el análisis.

1. **Cerrar solo los 5 huecos de cobertura (2.2, 7.2, 7.4, 8.5-latinos/grecolatinos, 8.6).** Alcance más acotado y de menor riesgo: escribir cuadernos nuevos únicamente donde hoy hay cero problemas, sin tocar los 19 archivos existentes. No resuelve el desfase de numeración ni la colisión de etiquetas duplicadas.
2. **Corregir primero la colisión activa de `prob:3.9.1`-`prob:3.9.5`.** Es un bug real y visible en el PDF (§2.1), acotado a 2 archivos, y de bajo riesgo — renombrar las 5 etiquetas en uno de los dos archivos (probablemente en `chi_cuadrada(p).tex`, ya que `distribuciones_especiales(p).tex` las usa también internamente en sus propias citas). Se puede hacer independientemente de cualquier decisión sobre la convención nueva/vieja.
3. **Ejecutar la convención nueva completa (1 archivo por sección, 3-6 problemas flexibles).** Es la opción de mayor alcance: toca los 19 archivos, resolvería el desfase de numeración como efecto colateral (según la nota del propio CHANGELOG de julio 18), y alinearía por fin los cuadernos con la teoría ya renumerada. Requiere el mismo enfoque "un paso a la vez" que el usuario ya pidió en julio.
4. **Aceptar el desfase de numeración como está y solo documentarlo** (ej. una nota al inicio de cada `(p).tex` aclarando que el número impreso no es el número de sección temático), sin reestructurar nada. Es la opción de menor esfuerzo pero no resuelve ninguno de los problemas de fondo, incluida la colisión de etiquetas duplicadas.

Ninguna opción es mutuamente excluyente con las demás salvo la 3 y la 4 (que son visiones opuestas de fondo); 1 y 2 pueden hacerse en cualquier orden y son compatibles con emprender la 3 después.
