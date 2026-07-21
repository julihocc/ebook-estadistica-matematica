# Manual Normativo de Requerimientos y Especificaciones Técnicas para Presentaciones Beamer y Laboratorios en Python

## 1. Objetivo y Alcance Normativo

Este documento establece el **Estándar de Oro Institucional (*Institutional Gold Standard*)** para la creación, refactorización, verificación y certificación de las presentaciones interactivas en **LaTeX Beamer** (`presentaciones/es/` y `presentaciones/en/`) y sus respectivos **laboratorios de simulación computacional en Python** (`presentaciones/code/`) dentro del proyecto curricular *Modelación Estadística*.

El objetivo primordial es garantizar una **excelencia académica, estética rigurosa y simetría pedagógica bilingüe**, asegurando que cada presentación sea un instrumento didáctico interactivo que enganche de manera activa al estudiante y que compile con precisión absoluta en cualquier entorno LaTeX moderno.

---

## 2. Las 5 Reglas de Oro Curriculares e Institucionales

### Regla de Oro 1: Arquitectura Modular Estándar (22 Diapositivas)
Toda presentación curricular del libro debe estructurarse obligatoriamente de forma modular en **5 bloques temáticos claramente diferenciados**, abarcando un estándar de **22 diapositivas de contenido (que generan entre 28 y 32 páginas en el PDF tras el revelado progresivo)**:

1. **Bloque I: Identidad y Hoja de Ruta (Diapositivas 01–02)**
   - **Slide 01 (Portada):** Membrete institucional completo (`\titlepage`) dentro de un entorno limpio `\begin{frame}[plain] \vspace{-0.5cm} \titlepage \end{frame}` para compensar el espaciado vertical del tema Metropolis.
   - **Slide 02 (Hoja de Ruta):** Ubicación curricular de la sección actual dentro de su capítulo (en rojo institucional `TecRojo`) y declaración explícita del **Objetivo Didáctico** particular de la sesión con revelado progresivo (`\pause`).

2. **Bloque II: Desarrollo Teórico Riguroso e Interactivo (Diapositivas 03–08)**
   - **Slide 03 (Motivación y Fenómeno Físico):** Comparación conceptual entre el enfoque intuitivo/empírico y la formalización matemática del tema.
   - **Slides 04–06 (Teoría Fundamental y Teoremas):** Deducciones analíticas, definiciones y teoremas clave presentados con revelado progresivo (`\pause`). Los pasos intermedios no deben amontonarse; deben fluir armónicamente entre cajas tipográficas (`block`, `alertblock`, `exampleblock`).
   - **Slides 07–08 (Conexiones de Ingeniería y Casos Límite):** Aplicaciones prácticas en ciencia de datos, manufactura, robótica o diagnósticos técnicos, junto con el análisis asintótico o comportamiento bajo condiciones extremas.

3. **Bloque III: Puente Computacional y Laboratorio en Python (Diapositivas 09A–09D)**
   - El laboratorio se divide estrictamente en **4 diapositivas seriadas (`1/4`, `2/4`, `3/4`, `4/4`)**:
     - **Slides 09A–09C (Código Fuente 1/4 a 3/4):** Importación de bloques exactos y completos de funciones matemáticas desde el script en inglés mediante `\lstinputlisting[firstline=X, lastline=Y]`. **Queda estrictamente prohibido truncar encabezados de funciones o sentencias `return`**.
     - **Slide 09D (Verificación en Consola 4/4):** Exhibición de los resultados numéricos reales de la terminal en dos columnas equitativas (`\begin{columns}[T]`), verificando el emparejamiento exacto con la teoría analítica sin ningún tipo de desbordamiento.

4. **Bloque IV: Ejemplos Resueltos de Refuerzo (Diapositivas 10A–13B)**
   - **[Actualizado 2026-07-18]** Se reemplazó el patrón anterior de "Ejercicio en Clase" (citar problemas del cuaderno `(p).tex`) por la **reutilización de ejemplos resueltos (`\ejemplo`/`\solucion`) que ya existen en la sección de teoría correspondiente del libro maestro**. No se crea contenido de ejemplo nuevo: se seleccionan los ejemplos ya presentes, en orden de dificultad creciente, priorizando variedad de ángulos sobre alcanzar un conteo fijo (típicamente 2-4 ejemplos por mazo, según cuántos existan realmente en esa sección).
   - **División Didáctica Obligatoria (Enunciado $\to$ Resolución):** Cada ejemplo se desarrolla con el mismo nivel de detalle que el patrón anterior, en **exactamente dos diapositivas consecutivas**:
     - **Diapositiva A (`1/2` - Enunciado):** Planteamiento del ejemplo con su contexto, y formulación clara de los incisos a resolver.
     - **Diapositiva B (`2/2` - Resolución):** Desarrollo algebraico completo paso a paso (igual de detallado que la solución ya presente en el libro), en dos columnas algebraicas equilibradas o bloques seriados con `\pause`, rematando con un **cuadro de interpretación pedagógica** (`exampleblock` o `alertblock`) que responda al "por qué" práctico del resultado.
   - **Motivo del cambio:** con la reorganización de los cuadernos de problemas en archivos por sección (ver Regla de Oro 4 actualizada), el cuaderno de problemas queda como material de práctica autónoma del lector, separado del contenido demostrado en clase — los mazos ahora refuerzan la teoría con ejemplos ya demostrados en vez de plantear ejercicios sin resolver en pantalla.

5. **Bloque V: Síntesis y Transición Curricular (Diapositivas 14–15)**
   - **Slide 14 (Síntesis y Conclusiones):** Resumen ejecutivo de los pilares conceptuales aprendidos en la sesión.
   - **Slide 15 (Transición Curricular):** Conexión lógica hacia atrás (lo que ya dominamos) y hacia adelante (el reto o puente conceptual con la siguiente sección del plan de estudios).

---

### Regla de Oro 2: Estética Rigurosa, Revelado Progresivo y Tolerancia Cero al Markdown Informal
- **Revelado Progresivo (`\pause`):** La presentación no debe ser un muro estático de texto. Se requiere el uso dinámico de `\pause` en las diapositivas de teoría y ejercicios para revelar las deducciones e interpretaciones al ritmo de la explicación docente, enganchando activamente al estudiante.
- **Prohibición de Marcado Informal Markdown:** Los archivos `.tex` son código fuente profesional de LaTeX. **Queda terminantemente prohibido utilizar sintaxis informal de Markdown dentro del texto visible de las diapositivas** (tales como asteriscos `**texto**`, guiones informales `---` en lugar de guiones largos de LaTeX, o subrayados informales).
- **Énfasis Institucional:** Todo resaltado tipográfico debe realizarse exclusivamente mediante comandos nativos:
  - `\textbf{texto principal}` para negritas en conceptos clave.
  - `\emph{término definido}` o `\textit{...}` para cursivas técnicas.
  - `\textcolor{TecRojo}{texto o ecuación importante}` para acentos visuales con la paleta oficial del Tecnológico de Monterrey.

---

### Regla de Oro 3: Única Fuente de la Verdad en Inglés para Código (`Single Source of Truth`)
- **Centralización en Inglés:** Todo código de simulación y cálculo numérico debe residir **única y exclusivamente** en el directorio `presentaciones/code/<unidad>/<ID>_<nombre_en_ingles>.py`.
- **Estándar de Redacción de Código:** Los scripts `.py` deben estar escritos 100% en inglés (variables, docstrings, comentarios y mensajes por consola `print(...)`). Esto garantiza la portabilidad internacional del código y su alineación con el estado del arte en ciencia de datos.
- **Librerías Permitidas:** Se limitan estrictamente a Python estándar, `numpy` y `scipy`. No se permiten dependencias gráficas (`matplotlib`, `seaborn`) ni librerías pesadas que impidan la ejecución instantánea en terminal o en servidores de CI.
- **Importación Bilingüe Simétrica:** Tanto el mazo en español (`es/`) como el mazo en inglés (`en/`) importan exactamente las mismas líneas del mismo archivo `.py` en inglés mediante `\lstinputlisting`. Queda prohibido crear scripts duplicados en español (`*.es.py`).

---

### Regla de Oro 4: Cuadernos de Problemas por Sección y Coherencia Curricular

**[Actualizado 2026-07-18]** Reemplaza la taxonomía fija anterior (10 problemas, 3-3-2-2, niveles visibles). **[Refinado 2026-07-20]** Reemplaza la categorización por dificultad y el esquema de etiquetado por nombre significativo/numérico. Ver `CHANGELOG.md` para el registro de ambas decisiones.

- Cada `\section` real de teoría del libro maestro debe tener su **propio archivo de problemas individual** (`latex/<seccion>(p).tex`), ubicado inmediatamente después de esa sección en el `\input` del libro — no un archivo compartido por capítulo cubriendo varias secciones.
- La cantidad de problemas por sección **no se fija por una cifra aproximada**: el requisito es que haya **al menos un problema por cada uno de los 6 niveles de la Taxonomía de Bloom** (Recordar, Comprender, Aplicar, Analizar, Evaluar, Crear) — típicamente 6 problemas en total, uno por nivel, pero puede haber más de uno en un mismo nivel si la sección lo amerita (varios ángulos/aplicaciones distintos). No se rellena con problemas redundantes solo para alcanzar un conteo; el mínimo es de cobertura (los 6 niveles presentes), no de cantidad.
- Los problemas se ordenan de **menor a mayor nivel cognitivo** dentro del archivo, usando los **6 niveles de la Taxonomía de Bloom** (Recordar → Comprender → Aplicar → Analizar → Evaluar → Crear) en vez de una escala de dificultad (Fundamental/Operativo/Analítico/Desafiante, convención anterior ya retirada). El nivel se documenta como **comentario interno de LaTeX** (`% Recordar`, `% Comprender`, etc.) — **no como encabezado visible** (`\subsection*{Nivel...}`) en el PDF compilado del libro.
- Las etiquetas `\label` de cada problema usan un **tag hasheado corto y determinista**, no un nombre numérico (`prob:X.Y.Z`) ni semántico (`prob:nombre-descriptivo`). Formato: `prob:<7 caracteres hexadecimales>`, calculados con `sha1sum` sobre una cadena semilla determinista (`"<archivo>-p-<índice>"`, ej. `"tecnicas_de_conteo-p-3"`), verificando contra el `.aux` compilado que el hash no colisiona con ninguna etiqueta `prob:` ya existente en el libro antes de usarlo. Motivo: los nombres numéricos generan expectativas de numeración de sección que casi nunca se cumplen (ver `docs/diagnostico-cuadernos-problemas-2026-07-20.md`, desfase de Fase D), y los nombres semánticos son propensos a colisión accidental entre archivos (caso real: `prob:3.9.1`-`.5` duplicados entre `distribuciones_especiales(p).tex` y `chi_cuadrada(p).tex`) además de costar esfuerzo de mantenimiento. Un hash corto es intrínsecamente único y no promete nada sobre numeración ni contenido.
- El cuaderno de problemas queda como material de **práctica autónoma para el lector**, independiente del contenido que se presenta en clase (ver Regla de Oro 1, Bloque IV — los mazos ahora citan ejemplos resueltos de la teoría, no problemas de este cuaderno).
- **Migración de archivos existentes**: esta convención (incluido el refinamiento del 2026-07-20) rige el trabajo nuevo hacia adelante. Los 19 archivos `(p).tex` de los capítulos 2-8 que aún usan la convención anterior (10 fijos, dificultad visible, etiquetas numéricas/semánticas) no se migran automáticamente — quedan pendientes de una tarea de reorganización aparte (ver `docs/diagnostico-cuadernos-problemas-2026-07-20.md`, sección de recomendaciones).

---

### Regla de Oro 5: Política Innegociable de Cero Desbordamientos (*Zero Overfull Policy*)
- **Doble Compilación Obligatoria:** Toda presentación Beamer debe ser compilada por duplicado en la terminal (`pdflatex -interaction=nonstopmode <archivo>.tex`) para estabilizar referencias cruzadas, numeración de diapositivas y métricas del archivo de navegación (`.nav`).
- **Certificación Cero Overfulls:** Ninguna diapositiva de contenido (páginas 2 hasta N) puede generar advertencias en el registro (`.log`). **Se exige un conteo absoluto de `0 Overfull \vbox` (desbordamiento vertical) y `0 Overfull \hbox` (desbordamiento horizontal)**.
- **Técnicas Oficiales de Remediación Tipográfica:**
  1. **Disposición en Dos Columnas:** Utilizar `\begin{columns}[T] \begin{column}{0.48\textwidth} ... \end{column} ... \end{columns}` para distribuir fórmulas algebraicas y textos paralelos sin saturar el margen inferior.
  2. **Control Granular de Fuentes Beamer:** Escalar el texto con `\small`, `\footnotesize` o `\scriptsize` en listados densos.
  3. **Ajuste Micro-Vertical:** Aplicar compensaciones finas entre bloques o antes de entornos matemáticos: `\vspace{-0.05cm}`, `\vspace{-0.1cm}` o `\vspace{-0.15cm}`.
  4. **Escalado de Listados de Código (`\lstset`):** Para bloques de código Python en `lstinputlisting`, ajustar dinámicamente la fuente y el interlineado:
     ```latex
     basicstyle=\fontsize{4.6pt}{5.4pt}\selectfont\ttfamily, aboveskip=0.1em, belowskip=0.1em
     ```
  5. **Escapado Estricto en Títulos LaTeX:** Escapar siempre los ampersands (`&` $\to$ `\&`) y porcentajes (`%` $\to$ `\%`) en títulos de diapositiva (`\frametitle`) y títulos de bloque (`\blocktitle`) para evitar errores de alineación en tablas de LaTeX.

---

## 3. Especificaciones Técnicas y de Diseño Visual

| Parámetro | Especificación Institucional |
| :--- | :--- |
| **Motor LaTeX** | `pdflatex` con opción de interacción por lotes (`-interaction=nonstopmode`). |
| **Clase Documento** | `\documentclass[10pt, aspectratio=169, xcolor={dvipsnames,table}]{beamer}` |
| **Preámbulos ES** | `\input{../../_preambulo_beamer}` y `\input{../../_comandos_beamer}` |
| **Preámbulos EN** | Preámbulos y comandos compartidos adaptados en la carpeta `en/`. |
| **Tema Beamer** | `Metropolis` (moderno, tipografía limpia, barras de título sólidas). |
| **Paleta Cromática** | • **TecRojo (`#EC2661`):** Color institucional principal, alertas y énfasis curricular.<br>• **TecAzul (`#1A2E51`):** Color secundario corporativo y bloques estándar.<br>• **Gris Neutro (`#666666`):** Texto secundario y desvanecimiento en hoja de ruta. |
| **Entornos de Bloque** | • `\begin{block}{Título}`: Definiciones, teoremas y código fuente.<br>• `\begin{alertblock}{Título}`: Conceptos críticos, fórmulas de momios y conclusiones.<br>• `\begin{exampleblock}{Título}`: Interpretaciones pedagógicas y justificaciones de ingeniería. |

---

## 4. Protocolo Reproducible de Auditoría y Remediación (6 Pasos)

Cualquier agente, subagente o ingeniero de software que intervenga en el repositorio para añadir o refactorizar una sección debe cumplir estrictamente con este flujo de trabajo auditable de 6 pasos:

1. **Paso 1 --- Auditoría Teórica del Capítulo en LaTeX Maestro:**
   Inspeccionar `latex/<seccion>.tex` para alinear notación, fórmulas y teoremas con el texto del libro.

2. **Paso 2 --- Verificación de Problemas 3-3-2-2 en `(p).tex`:**
   Comprobar que `latex/<seccion>(p).tex` contenga exactamente 10 problemas bajo la taxonomía institucional y que el archivo maestro compile sin errores (`pdflatex "[Modelación Estadística].tex"`).

3. **Paso 3 --- Certificación del Laboratorio Python en Inglés:**
   Verificar o construir `presentaciones/code/<unidad>/<ID>_<nombre>.py`. Ejecutar por terminal (`python <script>.py`) para certificar que el código es autocontenido, no produce errores computacionales y genera salidas exactas por consola.

4. **Paso 4 --- Redacción Simétrica de Presentaciones Beamer (ES y EN):**
   Redactar las 22 diapositivas en `presentaciones/es/<unidad>/<seccion>.tex` e inmediatamente construir la versión espejo en inglés `presentaciones/en/<unidad>/<section>.tex`, garantizando simetría pedagógica y estética total.

5. **Paso 5 --- Compilación Doble y Certificación `Zero Overfull`:**
   Ejecutar una doble compilación por terminal para ambos idiomas:
   ```bash
   pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
   ```
   Auditar el archivo `.log` resultante (o mediante herramientas de búsqueda algorítmica `grep_search` / `Select-String`) para certificar que no existan `Overfull \vbox` ni `Overfull \hbox`.

6. **Paso 6 --- Actualización del Registro en el Mapa de Ruta (`ROADMAP.md`):**
   Registrar la conclusión de la sección en `presentaciones/ROADMAP.md` detallando el cumplimiento de la estructura de 22 diapositivas, el cuaderno de problemas 3-3-2-2, el script de Python en inglés y la certificación de 0 desbordamientos.
