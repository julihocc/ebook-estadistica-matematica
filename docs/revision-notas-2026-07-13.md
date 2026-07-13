# Auditoría de Inconsistencias en Notas LaTeX

**Fecha:** 2026-07-13  
**Alcance:** 39 archivos de teoría (Cap. 1-9), excluye problemas `(p).tex`  
**Entregable:** Inventario priorizado de hallazgos sin correcciones aplicadas

---

## Resumen Ejecutivo

Se encontraron **90+ hallazgos** distribuidos en 6 categorías. Los de **Alta prioridad** incluyen:
- Sintaxis LaTeX malformada (comandos inválidos: `\til`, `\s`, `\s/\sqrt{n}`, llaves desbalanceadas)
- Errores matemáticos (potencia incorrecta en fórmula χ², duplicación de contenido con resultado incorrecto)
- Referencias cruzadas rotas (etiquetas inexistentes, etiquetas apuntando a ejemplos incorrectos)
- Falta sistemática de `\label{}` en definiciones, teoremas, ejemplos en múltiples archivos
- Markdown residual masivo (`**negritas**` en vez de `\textbf{}`) en capítulo completo
- Traducción automática / artefactos de traducción ("Manejando otros Problemas", "problemaar", "predigamos")

Los de **Baja prioridad** son en su mayoría housekeeping (comentarios obsoletos, concordancia menor, tipografía).

---

## I. SINTAXIS LaTeX INCOMPLETA / MALFORMADA

### ALTA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| medidas_tendencia_central.tex | 165 | Comando inválido `\til{X}`, debería ser `\tilde{X}` |
| medidas_dispersion.tex | 94 | Comando inválido `\s`, debería ser `\sigma` |
| guia_prueba_hipotesis.tex | 11, 16, 34 | Comando malformado `\s/\sqrt{n}`, debería ser `\sigma` u otro comando válido |
| chi_cuadrada.tex | 48 | Error en fórmula matemática: `(447-500)^{5}` debería ser `(447-500)^{2}` (potencia incorrecta invalida el cálculo χ²) |
| regresion_multiple.tex | 347 | `\begin{problema}` sin cerrar, falta `\end{problema}` en línea 353 |

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| chi_cuadrada.tex | 12 | Mezcla ilegible `\texttt{valor }\chi^{2}\texttt{:}`; debería ser "estadístico $\chi^2$" o similar |
| chi_cuadrada.tex | 66-67 | Propiedad de χ² no encapsulada en `\begin{propiedad}...\end{propiedad}`; solo bloque `align` con label |
| esperanza_matematica.tex | 103-107 | Bloque `align` duplicado/residual que repite cálculo pero omite términos y da resultado incorrecto ($15 vs. $20) |
| esperanza_matematica.tex | 381-388, 394-400, 421-426 | `\label{}` dentro de `\[...\]` (displaymath no numerado) en vez de `align`; inconsistente |
| estadisticos_z_t.tex | 88-91 | Código Python con error de indentación: `return` no indentado dentro de `def ft()` |

---

## II. REFERENCIAS CRUZADAS ROTAS / INCONSISTENTES

### ALTA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| esperanza_matematica.tex | 165 | `\ref{exmp:2.8.2}` apunta a ejemplo incorrecto: refiere a cálculo con $f(x)=\frac{1}{2}x$ pero etiqueta indica ejemplo N(70,100); ejemplo correcto es `exmp:2.9.2` |
| esperanza_matematica.tex | 319 | Mismo error de `\ref{exmp:2.8.2}`; debería ser `exmp:2.9.2` |
| distribuciones_muestreo_avanzado.tex | 212, 269 | "(ver sección 2.11)" en texto plano; sección real es Cap. 3, no 2; no usa `\ref{}` |
| distribuciones_muestreo_avanzado.tex | 326 | "(sección 3.6)" hardcodeado; referencias Cap. 5 pero está etiquetada Cap. 3 |
| conceptos_estadisticos.tex | 0 (general) | Archivo entero sin `\label{}` en ningún entorno (`definicion`, `ejemplo`, `teorema`); impide referencias cruzadas futuras |
| introduccion_estadistica_inferencial.tex | 88-99 | "Estructura del capítulo" promete 6 temas de este capítulo pero pertenecen a 4 capítulos distintos (5-9) |

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| Chi_cuadrada.tex | 59 | Label incorrecto `\label{outline:19}` no sigue esquema `[cap.sec.item]`; debería ser `eq:3.9.X` o similar |

---

## III. FALTA SISTEMÁTICA DE `\label{}` EN ENTORNOS

### ALTA PRIORIDAD — Patrón a Nivel de Archivo

| Archivo | Entornos sin `\label{}` | Ejemplos (primeras líneas) |
|---------|------------------------|---------------------------|
| conceptos_estadisticos.tex | TODOS (defin:9,33,51; ejm:18,37,98; teo:68,85) | Línea 9 (`\begin{definicion}[Estimador insesgado]`) |
| introduccion_estadistica_inferencial.tex | `\begin{definicion}` x2 | Línea 22 (`[Población y muestra]`), línea 29 (`[Parámetro y estadístico]`) |
| variables_aleatorias_continuas_avanzado.tex | Definiciones (6), teoremas (4) | Línea 12 (`\begin{definicion}[Distribución uniforme]`), línea 258, 334, 353, 358 (teoremas) |
| distribuciones_muestreo_avanzado.tex | Teoremas y definiciones (8 total) | Línea 17 (`\begin{teorema}[Transformación afín]`), línea 41, 380, 512; defin: 255, 293, 338 |
| fundamentos_de_probabilidad.tex | Axioma mal etiquetado | Línea 213: `\begin{axioma}` con `\label{eq:2.3.1}` (esquema incorrecto, debería ser `ax:`) |

### MEDIA-ALTA PRIORIDAD — Ejemplos/Definiciones Individuales sin `\label{}`

| Archivo | Línea | Tipo | Contexto |
|---------|-------|------|----------|
| esperanza_matematica.tex | 29 | `\begin{ejemplo}` | Dado, cara (variable $X$) |
| esperanza_matematica.tex | 282 | `\begin{ejemplo}` | Varianza del dado |
| esperanza_matematica.tex | 474 | `\begin{teorema}` | Desigualdad `\|\sigma_{XY}\|\le\sigma_X\sigma_Y` |
| medidas_tendencia_central.tex | 74, 95, 125, 168, 207 | `\begin{ejemplo}` (x5) | Patrón: múltiples ejemplos sin etiqueta |
| medidas_dispersion.tex | 15, 31, 64, 125 | `\begin{ejemplo}` (x4) | Patrón: múltiples ejemplos sin etiqueta |
| probabilidad_condicional.tex | 40 | `\begin{ejemplo}` | |
| teorema_de_bayes.tex | 59 | `\begin{ejemplo}` | |
| introduccion_estadistica_descriptiva.tex | 28, 35 | `\begin{definicion}` (x2) | Población/muestra, parámetro/estadístico |
| fundamentos_de_probabilidad.tex | 75 | `\begin{figure}` | Sin `\caption{}`, solo label |
| estadisticos_z_t.tex | 123 | `\begin{ejemplo}` | Percentil t, $\nu=9$ |

---

## IV. ESQUEMA DE ETIQUETADO `[cap.sec.item]` INCONSISTENTE / INCORRECTO

### ALTA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| Variables_aleatorias_discretas.tex | 12 | Etiqueta `exmp:2.6.1` usa cap.2, pero archivo está en Cap. 3 del master (nombre engañoso; `\fmtnum` genera número correcto en PDF, pero etiqueta simbólica es falsa) |
| distribuciones_especiales.tex | 18 | Etiqueta `exmp:2.10.1` usa cap.2, en realidad Cap. 3 Sec. 2 |
| esperanza_matematica.tex | 74 | Etiqueta `exmp:2.9.1` usa cap.2, en realidad Cap. 4 Sec. 2 |
| distribuciones_muestreo_avanzado.tex | 31, etc. | Etiqueta `exmp:3.2.1` usa cap.3, en realidad Cap. 5 Sec. 2 (parcialmente correcto pero inconsistente con otros) |
| correlacion.tex | 147 | Etiqueta `\label{correlationMatrix}` no sigue esquema; debería ser `fig:9.1.X` |

**Nota general:** Capítulos 3-5 usan sistemáticamente prefijo de capítulo equivocado (todos dicen "cap.2" o "cap.3" cuando deberían ser "cap.3", "cap.4", "cap.5" según orden real en master file). Esto confunde a mantenedores que se fían del esquema documentado.

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| chi_cuadrada.tex | 80, 103 | Figuras etiquetadas `fig:3.9.1`, `fig:3.9.2` usan estructura `[cap.subsec.fig]` en lugar de `[cap.sec.fig]` (inconsistente con resto del archivo) |

---

## V. DISEÑO VISUAL / ENTORNOS LaTeX

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| variables_aleatorias_discretas.tex | 27 | Pseudo-encabezado `{Función de probabilidad}` (llaves vacías) — no produce efecto tipográfico; debería ser `\textbf{}` o entorno |
| distribuciones_especiales.tex | 94, 111, 120, 326, 334, 337, 354, 372, 413 | Patrón: 9+ pseudo-encabezados `{Título}` (p.ej. `{Percentil}`, `{Cuartiles}`, `{Distribución Normal}`); entorno `\begin{propiedad}` existe pero no se usa |
| esperanza_matematica.tex | 42, 57, 198, 211, 343, 360, 403, 419, 466, 487 | Patrón: 10+ pseudo-encabezados `{Texto}` |
| variables_aleatorias_continuas.tex | 177, 254 | Pseudo-encabezados `{Texto}` |
| variables_aleatorias_continuas_avanzado.tex | 456 | Pseudo-encabezado |
| distribuciones_muestreo_avanzado.tex | 265, 304, 349 | Pseudo-encabezados `{Propiedades}` (genérico, repetido) |
| esperanza_matematica.tex | 28, 127, 169, 281, 323, 333, 379 | Siete instancias de `{}` completamente vacías en líneas propias (restos de encabezados vaciados por error) |
| esperanza_matematica.tex | 127-134, 169-194, 323-341 | Soluciones presentadas como bloques `align` sueltos precedidos por `{}` vacío en lugar de `\begin{solucion}...\end{solucion}` (inconsistente) |
| variables_aleatorias_continuas.tex | 426-431 | `\begin{enumerate}` cierra fuera del `\end{ejemplo}` al que pertenece; entorno queda mal anidado |
| fundamentos_de_probabilidad.tex | 75 | `\begin{figure}` sin `\caption{}`, solo label (inconsistente; otras figuras sí tienen caption) |
| distribuciones_especiales.tex | 77-82, 133-138, 144-149 | Figuras sin `\caption` (inconsistente con otras figuras del mismo archivo: líneas 257-262 sí lo tienen) |
| variables_aleatorias_discretas.tex | 158-163, 197-202, 218-223 | Figuras sin `\caption` |
| variables_aleatorias_continuas.tex | 152-156, 162-166, 203-208, 392-397 | Figuras sin `\caption` ni `\label` (algunas) |

---

## VI. CALIDAD DE PROSA / ARTEFACTOS DE TRADUCCIÓN

### ALTA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| otros_problemas.tex | 1 | Título con traducción deficiente: `\section{Manejando otros Problemas en lineales regresión}` — orden de palabras incorrecto, "Problemas" capitalizado innecesariamente, "lineales" en lugar de "lineal". Debería ser: "Manejo de otros problemas en regresión lineal" |

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| conjuntos.tex | 64 | Error ortográfico: "diagrama de Ven" debería ser "diagrama de Venn" |
| fundamentos_de_probabilidad.tex | 200, 321 | Error de concordancia: "Ambos enfoque" (línea 200) debería ser "Ambos enfoques"; "evento complementarios" (321) debería ser "complementario" |
| variables_aleatorias_discretas.tex | 7 | Error de concordancia: "físico, geométrico, económico, financieros" (faltan "es" al final de los primeros 3) |
| esperanza_matematica.tex | 225 | Typo: "la espereza matemática" debería ser "la esperanza matemática" |
| estadisticos_z_t.tex | 31 | Error gramatical: "El investigador conoce a desviación estándar" debería ser "El investigador conoce LA desviación estándar" |
| validacion_modelo.tex | 51 | Probable error de traducción: "problemaar el rendimiento" — verbo inexistente; debería ser "probar" o "evaluar" |
| validacion_modelo.tex | 139 | Conjugación incorrecta: "predigamos" debería ser "predecimos" o "hagamos predicciones" |
| otros_problemas.tex | 39, 401 | Errores tipográficos: "Una breve La descripción" (falta "la" redundante); "Aunque hemo supuesto" debería ser "Aunque hemos supuesto" |
| valores_optimos.tex | 91, 109 | Concordancia: "hay otras estadísticos" debería ser "otros estadísticos" (género); "los Problemas discutido" debería ser "problemas discutidos" |
| regresion_multiple.tex | 351 | Estructura de oración deficiente: "trata de responde porque" debería ser "trata de responder por qué" |
| distribuciones_especiales.tex | 187 | Notación matemática incorrecta: "Si $N\sim \infty, p,q>>0,$" usa `\sim` para "tiende a"; debería ser $N \to \infty$ |
| estadisticos_z_t.tex | 4 | "$Ao$" debería ser "$A_0$" (subíndice sin formatear) |

### BAJA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| variables_aleatorias_discretas.tex | 4 | Falta punto entre oraciones: "...en el espacio muestral Esta función" |
| estadisticos_z_t.tex | 17 (comentario) | Comentario corrupto `% problemaabilidad` debería ser `% probabilidad` (artefacto de sustitución automática); sin impacto en PDF |
| estadisticos_z_t.tex | 108 | Comentario obsoleto: `% tPDF.png` no coincide con archivo incluido (`tCDF.png` línea 107) |
| diseno_experimentos_anova.tex | 3 | Anglicismo: "pruebas A/B/n" sin explicación; "computacional" en contexto que requeriría mejor redacción |
| intervalos_de_confianza.tex | 7 | Redacción: "la \emph{intervalo de confianza.}" (punto fuera de `\emph`; además "la" con sustantivo masculino) |
| diseno_experimentos_anova.tex | 21 | Anglicismo: "\emph{accuracy}" en párrafo español; debería ser "exactitud" o "precisión" |

---

## VII. MARKDOWN RESIDUAL

### ALTA PRIORIDAD

| Archivo | Línea | Hallazgo | Contexto |
|---------|-------|----------|----------|
| diseno_experimentos_anova.tex | 5, 9, 26, 36, 38, 65, 105, 118, 133, 140, 150, 155, 183, 189+ (30+ instancias) | Markdown `**texto**` para negritas en lugar de `\textbf{}` | Aparece repetidamente en todo el archivo |

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| valores_optimos.tex | 127 | Markdown `$-p$` innecesario dentro de "este valor$-p$"; debería ser "este valor-p" |
| regresion_multiple.tex | 19, 22, 55, etc. | Patrón "valor$-p$" repetido; `$...$` innecesarios fuera de modo matemático |

---

## VIII. ESTRUCTURA DE CAPÍTULOS

### MEDIA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| otros_problemas.tex | 0 (general) | **Nombre engañoso:** contiene teoría sobre "manejo de problemas en regresión lineal" (extensiones: variables categóricas, transformaciones), no un conjunto de ejercicios. Considerar renombrar a `manejo_problemas_regresion.tex` o `extensiones_regresion.tex`. |

---

## IX. IMÁGENES Y REFERENCIAS A ARCHIVOS

### BAJA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| chi_cuadrada.tex | 71 | Referencia `\lstinputlisting{../code/chi-cuadrada/statsChi2Simple.py}` — verificar que archivo existe en ruta relativa |
| valores_optimos.tex | 200 | Estructura de nota anómala: `[, ]{Error residual estándar}` con espacios vacíos en primer argumento |

**Nota:** Se verificó con spot-check que los 59 comentarios "0x0 pixel" en 18 archivos son auto-generados obsoletos, no indicadores de imágenes rotas. Las imágenes referenciadas existen realmente.

---

## X. DUPLICACIÓN Y CONTENIDO RESIDUAL

### ALTA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| esperanza_matematica.tex | 103-107 | Bloque `align` suelto que repite cálculo de ejemplo anterior (E(X) del dado) pero omite términos y da resultado incorrecto ($15 vs. $20). Parece contenido residual de borrador no eliminado. |

### BAJA PRIORIDAD

| Archivo | Línea | Hallazgo |
|---------|-------|----------|
| esperanza_matematica.tex | 512-526, 547-561 | Dentro de `\begin{multicols}{3}`, ítem `$\sigma_{Y}$` duplicado (líneas 520/522 y 555/557) en lista de estadísticos — error de copiar/pegar. |

---

## Recomendaciones Prioritarias para Corrección

1. **Fixes de sintaxis LaTeX de alto impacto** (impiden compilación limpia o distorsionan el PDF):
   - Comandos inválidos (`\til`, `\s`, `\s/\sqrt{n}`) → reemplazar con comandos válidos
   - Error matemático en chi_cuadrada.tex:48 (potencia `^{5}` → `^{2}`)
   - Entorno sin cerrar (regresion_multiple.tex:347)

2. **References rotas y etiquetado sistemático** (afecta navegabilidad y mantenimiento):
   - Agregar `\label{}` a todos los `\begin{definicion}`, `\begin{teorema}`, `\begin{ejemplo}` que carecen (especialmente conceptos_estadisticos.tex completo)
   - Corregir referencias cruzadas apuntando a ejemplos incorrectos (esperanza_matematica.tex:165, 319)
   - Auditar y corregir prefijos de capítulo en etiquetas (cap.2 → cap.3/4/5 según corresponda)

3. **Markdown residual masivo** (diseno_experimentos_anova.tex con 30+ instancias `**texto**` → `\textbf{}`)

4. **Calidad de traducción** (otros_problemas.tex:1, validacion_modelo.tex:51/139, valores_optimos.tex:91/109)

5. **Housekeeping de bajo impacto** (comentarios obsoletos, tipografía menor, figuras sin caption) — puede posponerse.

---

## Verificación de Cobertura

- **Archivos auditados:** 39 de 39 (100% del contenido de teoría)
- **Capítulos cubiertos:** 1-9 (distribución de lotes: Cap. 1-2 / Cap. 3-5 / Cap. 6-8 / Cap. 9)
- **Categorías auditadas:** 6 (Sintaxis LaTeX, Referencias cruzadas, Etiquetado, Diseño visual, Prosa, Markdown)
- **Sin correcciones aplicadas:** Documento de inventario solo, listo para decisión del usuario sobre priorización.

