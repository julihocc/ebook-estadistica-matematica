# Plan: Renumeración de `latex/*.tex` (Caps. 2-8) para correspondencia 1:1 con el temario MA1001B

**Fecha:** 2026-07-18
**Estado:** Ejecutado el 2026-07-20 (ver `CHANGELOG.md`, entradas 2026-07-20). La numeración 1:1 con el temario está completa y verificada para los caps. 2-8; los 5 bloques de contenido nuevo que este plan pedía (1.2, 6.2, 6.4, 7.5 ampliado, 7.6) ya fueron redactados en la continuación del 2026-07-20 y no quedan comentarios `% TODO(contenido-nuevo)` vivos en `latex/`. La mecánica del Cap. 7 se ejecutó de forma distinta a como la describe la tabla de este documento (fue necesario partir `pruebas_hipotesis_avanzadas.tex` en dos archivos para lograr la numeración 6.1-6.11 en el orden real del temario; ver detalle en el changelog) — el resto de las tablas de este plan se siguió tal cual. Este documento es histórico, no una lista de pendientes activa.
**Alcance:** Capítulos 2 a 8 del libro maestro en español (`latex/*.tex`)

---

## Contexto

El temario oficial (`docs/MA1001B-plan-de-estudios.md`) define 7 unidades con subtemas numerados (1.1-1.4, 2.1-2.7, ..., 7.1-7.6) que mapean 1:1 a los capítulos 2-8 del libro maestro (`latex/[Modelación Estadística].tex`). Hoy esa correspondencia no es exacta: algunos capítulos tienen más secciones `\section` que subtemas (contenido repetido o fuera de tema), otros menos (varios subtemas viven como `\subsection` dentro de una sola sección "paraguas"), el orden interno de algunas secciones no sigue el orden del temario, y 3 subtemas no tienen contenido en ningún lado.

**Objetivo:** que cada capítulo 2-8 tenga exactamente una `\section` numerada por cada subtema de su unidad correspondiente, con el título del subtema y en el orden del temario.

**Alcance estricto (nada más que esto):**
- Se tocan únicamente los archivos de teoría en español bajo `latex/*.tex` de los capítulos 2 a 8, y el bloque `\input` correspondiente en `latex/[Modelación Estadística].tex`.
- **No se tocan**: `latex/en_*.tex` (espejo en inglés), nada bajo `presentaciones/`, los archivos `(p).tex` de problemas (quedan intactos, sin renumerar sus encabezados internos), el Capítulo 1 (Estadística Descriptiva) ni el Capítulo 9 (Regresiones) — ambos fuera del temario oficial.
- No se corrigen errores preexistentes no relacionados (typos matemáticos, negritas markdown, etc.) aunque se toquen los mismos archivos.

**Regla operativa:** contenido que no corresponde a ningún subtema (introducciones de capítulo, material duplicado, guías prácticas) no se borra — se convierte en `\section*` (no numerada) para que no compita con la numeración de subtemas. Reordenamientos de contenido se hacen *dentro* del mismo archivo cuando sea posible; se evita reordenar la lista `\input` del archivo maestro salvo que sea imprescindible.

---

## Capítulo 2 → Unidad 1: Teoría de Probabilidad (1.1-1.4)

| Archivo | Acción |
|---|---|
| `introduccion_probabilidad.tex` | `\section` → `\section*` (introducción sin número) |
| `conjuntos.tex` | Retitular a **"1.1 Teoría de conjuntos y su relación con cálculo de probabilidades"** |
| `fundamentos_de_probabilidad.tex` | Su `\section` baja a `\subsection`, anidado bajo 1.1 (contenido de espacio muestral/eventos/axiomas es parte natural de 1.1); sus 8 `\subsection` actuales bajan a `\subsubsection` |
| *(nuevo)* `tecnicas_de_conteo.tex` | **Contenido nuevo** — sección **"1.2 Técnicas de conteo"**: principio de multiplicación, permutaciones, combinaciones, coeficiente binomial, un ejemplo resuelto de probabilidad clásica. Se agrega su `\input` al maestro entre `fundamentos_de_probabilidad` y `probabilidad_condicional` |
| `probabilidad_condicional.tex` | Retitular a **"1.3 Probabilidad condicional y regla de Bayes"** |
| `teorema_de_bayes.tex` | Su `\section` baja a `\subsection` anidado bajo 1.3; `Generalizaciones` baja a `\subsubsection` |
| `muestreo_aleatorio.tex` | Retitular a **"1.4 Muestreo aleatorio"**; contenido intacto (incluye TLC introductorio, se deja como está) |

Resultado: 4 secciones numeradas (1.1-1.4) + 1 introducción sin numerar.

## Capítulo 3 → Unidad 2: Variables Aleatorias Discretas (2.1-2.7)

| Archivo | Acción |
|---|---|
| `variables_aleatorias_discretas.tex` | Sus 3 `\section` (PMF, CDF, Esperanza y varianza) se fusionan en una sola: **"2.1 Distribución de probabilidad discreta"**, con esas 3 como `\subsection` |
| `distribuciones_especiales.tex` | Ver desglose abajo |

Dentro de `distribuciones_especiales.tex`:
- "Distribución Binomial y Bernoulli" → **"2.2 Experimento Bernoulli y distribución binomial"**
- Bloque de **Multinomial** (hoy ubicado después de Poisson) se **mueve físicamente** justo después de 2.2 → **"2.3 Distribución multinomial"**
- "Distribuciones Geométrica y Binomial Negativa" → **"2.4 Distribución geométrica y binomial negativa"**
- "Distribución Hipergeométrica" → **"2.5 Distribución hipergeométrica"**
- "Distribución de Poisson" → **"2.6 Distribución Poisson"**
- "Distribución Normal y aproximación continua" (no es subtema de la Unidad 2) baja a `\subsection` dentro de 2.6, como "Aproximación normal a distribuciones discretas"
- "Distribuciones discretas en ciencia de datos" → **"2.7 Variables aleatorias discretas y su relación con ciencia de datos"**

Resultado: 7 secciones numeradas (2.1-2.7), sin contenido extra.

## Capítulo 4 → Unidad 3: Variables Aleatorias Continuas (3.1-3.6)

| Archivo | Acción |
|---|---|
| `variables_aleatorias_continuas.tex` | Sus 2 `\section` (PDF; CDF+conjunta+independencia+condicional) se fusionan en **"3.1 Función de densidad"**, con esos temas como `\subsection` |
| `esperanza_matematica.tex` | Retitular a **"3.2 Valor esperado"** |
| `variables_aleatorias_continuas_avanzado.tex` | Ver desglose abajo |

Dentro de `variables_aleatorias_continuas_avanzado.tex`:
- "Distribución Uniforme Continua" → **"3.3 Distribución uniforme"**
- "Distribución Exponencial" (no es subtema propio) baja a `\subsection` dentro de 3.5, fusionando con la subsubsección duplicada "Caso particular: distribución exponencial (revisitada)" que ya existe ahí (se deja una sola versión, no duplicada)
- "Distribución Normal" → **"3.4 Distribución normal"**
- "Distribuciones Gamma, Beta y Weibull" → **"3.5 Distribuciones de tipo gamma"** (Beta y Weibull quedan como `\subsection` existentes, más la Exponencial fusionada)
- "Función Generadora de Momentos (FGM)" → **"3.6 Función generadora de momentos"**

Resultado: 6 secciones numeradas (3.1-3.6).

## Capítulo 5 → Unidad 4: Distribuciones de Muestreo (4.1-4.7)

| Archivo | Acción |
|---|---|
| `introduccion_estadistica_inferencial.tex` | `\section` → `\section*` |
| `distribuciones_muestreo_avanzado.tex` | Ver desglose abajo |
| `conceptos_estadisticos.tex` | `\section` → `\section*` (contenido se solapa con 4.3; se deja como repaso no numerado, sin borrar) |
| `estadisticos_z_t.tex` | `\section` → `\section*` (se solapa con 4.5; se deja como repaso no numerado, sin borrar) |

Dentro de `distribuciones_muestreo_avanzado.tex`:
- "Transformación de Variables Aleatorias y Distribuciones Derivadas" (hoy 1 sección con 2 subsecciones) se **divide en 2 secciones**: **"4.1 Transformación de variables"** y **"4.2 Distribuciones de probabilidad de funciones de variable aleatoria"**
- "Distribuciones Muestrales de la Media y Varianza Insesgada" → **"4.3 Distribuciones muestrales de medias"**; la sección separada "Teorema del Límite Central: Convergencia Asintótica" baja a `\subsection` dentro de 4.3
- "Distribución χ² (Chi-Cuadrada)" → **"4.4 Distribución χ²"**
- "Distribución t de Student" → **"4.5 Distribución t"**
- "Distribución F de Snedecor" → **"4.6 Distribución F"**
- "Distribuciones de Muestreo y Ciencia de Datos" → **"4.7 Distribuciones de muestreo y su relación con ciencia de datos"**

Resultado: 7 secciones numeradas (4.1-4.7) + 3 bloques sin numerar (1 intro + 2 repaso).

## Capítulo 6 → Unidad 5: Estimación (5.1-5.7)

Capítulo más simple — mayormente mecánico.

| Archivo | Acción |
|---|---|
| `estimacion_puntual.tex` | Retitular a **"5.1 Métodos de estimación puntual"** (ya casi coincide) |
| `intervalos_de_confianza.tex` | Retitular a **"5.2 Estimación por intervalo"** |
| `estimacion_intervalos_avanzado.tex` | Sus 5 `\subsection` actuales se **promueven** directamente a `\section`, en el mismo orden en que ya están: **"5.3 Estimación de la media y diferencia entre dos medias"**, **"5.4 Errores estándar"**, **"5.5 Estimación de una proporción y diferencia entre dos proporciones"**, **"5.6 Estimación de la varianza y razón de dos varianzas"**, **"5.7 Estimación del tamaño de una muestra"** |

Resultado: 7 secciones numeradas (5.1-5.7), sin contenido extra.

## Capítulo 7 → Unidad 6: Docimasia (6.1-6.11)

Capítulo con más reorganización de subsecciones.

| Archivo | Acción |
|---|---|
| `pruebas_de_hipotesis.tex` | Sus 12 `\subsection` se reparten en 3 secciones nuevas (ver abajo) |
| `guia_prueba_hipotesis.tex` | `\section` → `\section*` (es un ejemplo de prueba $Z$ con varianza *conocida*; no corresponde a 6.4, que pide varianza desconocida — se deja como ejemplo introductorio de apoyo, sin numerar) |
| `pruebas_hipotesis_avanzadas.tex` | Sus 5 `\subsection` se promueven a `\section` (ver abajo) |
| `chi_cuadrada.tex` | Su única `\section` se **divide en 2** (ver abajo) |

Dentro de `pruebas_de_hipotesis.tex`:
- **"6.1 Elementos de prueba de hipótesis"** ← Hipótesis nula vs alternativa, Notación formal, Tipos de pruebas, Errores, Potencia y tamaño de muestra
- **"6.2 Relación entre intervalos de confianza y pruebas de hipótesis"** ← se redacta un puente breve (pocas líneas) a partir de "Regla de decisión", explicitando la equivalencia IC↔prueba de dos colas
- **"6.3 Uso de los valores P para la toma de decisiones"** ← Nivel de significación, Valor p, Ejemplo completo, Interpretación, Consideraciones, Resumen

Nueva sección (contenido nuevo, pequeño): **"6.4 Pruebas relacionadas con una media (varianza desconocida)"** — prueba $t$ para una media con $\sigma$ desconocida, reutilizando la distribución $t$ ya presentada en 4.5; se agrega como archivo nuevo `prueba_media_varianza_desconocida.tex` o como sección adicional en `pruebas_de_hipotesis.tex` (a decidir al ejecutar, según extensión).

Dentro de `pruebas_hipotesis_avanzadas.tex`:
- "Pruebas de hipótesis sobre dos medias" → **"6.5 Pruebas sobre dos medias"**
- "Pruebas relacionadas con proporciones" → **"6.6 Pruebas relacionadas con proporciones"**
- "Pruebas relacionadas con varianzas" → **"6.7 Pruebas relacionadas con varianzas"**
- "Pruebas de homogeneidad vs Pruebas de independencia" → se recorta a solo homogeneidad (la parte de independencia ya vive en 6.9, ver abajo) → **"6.10 Pruebas de homogeneidad"**
- "Pruebas de varias proporciones y procedimiento de Marascuilo" → **"6.11 Pruebas de varias proporciones"**

Dentro de `chi_cuadrada.tex` (dividir la única `\section` en 2, cada una con su propio `\label`, y repuntar las 3 referencias externas que hoy usan `\label{sec:3.9}`):
- **"6.8 Pruebas de bondad de ajuste"** ← Aplicaciones, Ejemplo, La Distribución χ², Propiedades, Prueba formal de bondad de ajuste
- **"6.9 Pruebas de independencia"** ← "Regresando a nuestro ejemplo..." (tabla de contingencia género/materias) + Conclusiones

Resultado: 11 secciones numeradas (6.1-6.11) + 1 sin numerar (guía introductoria).

## Capítulo 8 → Unidad 7: Diseño de Experimentos (7.1-7.6)

Archivo único: `diseno_experimentos_anova.tex`.

- "Fundamentos del Diseño de Experimentos (DoE)" → **"7.1 Estrategias de experimentación"**
- "Análisis de Varianza de un factor (One-Way ANOVA)" → **"7.2 Experimentos con un factor: análisis de varianza"**; su subsección "Cuadrados medios, valores esperados y estadístico F" se **promueve** a sección nueva → **"7.3 Análisis de efectos de modelo fijo"**
- "Comparaciones múltiples y pruebas post-hoc" → `\section*` (material de apoyo, no es subtema propio)
- "Verificación de supuestos en ANOVA..." se **mueve** (reordenamiento interno del archivo) para quedar antes de bloques → **"7.4 Adecuación del modelo: análisis de residuos"**
- "Diseño en Bloques Completos al Azar (DBCA)" → **"7.5 Bloques completamente aleatorizados, cuadrados latinos y grecolatinos"**; **contenido nuevo** agregado como subsecciones: cuadrados latinos y cuadrados grecolatinos (hoy el archivo solo cubre bloques aleatorizados)
- **Contenido nuevo, sección completa**: **"7.6 Introducción a diseños factoriales"**, agregada al final del archivo

Resultado: 6 secciones numeradas (7.1-7.6) + 1 sin numerar (comparaciones múltiples).

---

## Contenido nuevo requerido (resumen)

1. **1.2 Técnicas de conteo** — sección completa nueva (archivo nuevo).
2. **6.2** — puente breve IC ↔ pruebas de hipótesis (pocas líneas, reutilizando material existente).
3. **6.4 Pruebas sobre una media, varianza desconocida** — sección nueva (prueba $t$), reutiliza la distribución $t$ de 4.5.
4. **7.5** — subsecciones nuevas de cuadrados latinos y grecolatinos.
5. **7.6 Diseños factoriales** — sección completa nueva.

Todo el contenido nuevo sigue el estilo ya establecido en el libro (definición → teorema/propiedad → ejemplo resuelto), sin código Python nuevo (eso es competencia de `presentaciones/`, fuera de alcance).

## Orden de ejecución

Capítulo por capítulo, en este orden (de menor a mayor complejidad): **6 → 3 → 4 → 5 → 2 → 8 → 7**. Después de cada capítulo: compilar `pdflatex "[Modelación Estadística].tex"` dos veces y confirmar 0 errores, 0 referencias indefinidas, y que la tabla de contenido muestre exactamente las secciones esperadas para ese capítulo.

## Verificación final

- Compilar el libro completo dos veces.
- Revisar el `.toc` generado: cada capítulo 2-8 debe listar exactamente el número de secciones numeradas de su unidad (4,7,6,7,7,11,6 respectivamente), más las secciones `\section*` esperadas.
- Confirmar que ningún `\ref` quedó roto (0 "??" en el PDF).
