# Presentaciones Beamer & Laboratorios de Simulación en Python

Este directorio (`presentaciones/`) contiene las presentaciones interactivas en **LaTeX Beamer** (español e inglés) y los **laboratorios computacionales en Python** complementarios para las clases del libro digital *Modelación Estadística*.

Esta guía constituye el **manual operativo estándar y 100% reproducible** para cualquier agente de inteligencia artificial (o colaborador humano) que trabaje en la creación, modificación, verificación o mantenimiento de las presentaciones y scripts de este proyecto.

---

## 1. Arquitectura y Estructura del Directorio

```text
presentaciones/
├── _preambulo_beamer.tex           ← Preámbulo compartido en español (tema Metropolis, colores, paquetes)
├── _comandos_beamer.tex            ← Comandos matemáticos e institucionales en español
├── _en_preambulo_beamer.tex        ← Preámbulo compartido en inglés
├── _en_comandos_beamer.tex         ← Comandos matemáticos en inglés
├── README.md                       ← Esta guía y catálogo operativo de presentaciones
├── ROADMAP.md                      ← Hoja de ruta, trabajo pendiente y planificación de capítulos
├── code/                           ← ÚNICA FUENTE DE LA VERDAD para código de simulación (en inglés)
│   ├── 02_teoria_probabilidad/
│   │   ├── 02.01_intro_probability.py
│   │   ├── 02.02_sets_and_partitions.py
│   │   ├── 02.03_probability_fundamentals.py
│   │   ├── 02.04_conditional_probability.py
│   │   ├── 02.05_bayes_theorem.py
│   │   └── 02.06_random_sampling.py
│   └── <proximas_unidades>/
├── es/                             ← Presentaciones en español (p. ej. es/02_teoria_probabilidad/)
│   └── 02_teoria_probabilidad/
│       ├── 02.01_introduccion_probabilidad.tex (.pdf)
│       ├── 02.02_conjuntos_y_particiones.tex (.pdf)
│       ├── 02.03_fundamentos_probabilidad.tex (.pdf)
│       ├── 02.04_probabilidad_condicional.tex (.pdf)
│       ├── 02.05_teorema_bayes.tex (.pdf)
│       └── 02.06_muestreo_aleatorio.tex (.pdf)
└── en/                             ← Presentaciones en inglés (p. ej. en/02_probability_theory/)
    └── 02_probability_theory/
        ├── 02.01_intro_probability.tex (.pdf)
        ├── 02.02_sets_and_partitions.tex (.pdf)
        ├── 02.03_probability_fundamentals.tex (.pdf)
        ├── 02.04_conditional_probability.tex (.pdf)
        ├── 02.05_bayes_theorem.tex (.pdf)
        └── 02.06_random_sampling.tex (.pdf)
```

---

## 2. Las 4 Reglas de Oro del Flujo de Trabajo

### Regla 1: Código de Python Unificado en Inglés (Una Sola Fuente de la Verdad)
- **Prohibido duplicar código:** No se permite crear archivos de simulación independientes en español o por idioma (`*.es.py`, scripts separados en carpetas de idioma, etc.).
- Todo script computacional del proyecto **debe estar redactado exclusivamente en inglés** (comentarios, variables, salidas por consola y docstrings en inglés) y debe ubicarse en `presentaciones/code/<unidad>/<ID>_<nombre_en_ingles>.py`.
- **Librerías permitidas:** Única y exclusivamente `python` estándar y `numpy` / `scipy` (sin dependencias que requieran entornos virtuales complejos o interfaces gráficas como `matplotlib` que bloqueen compilación o terminal).
- **Importación en Beamer:** Tanto la presentación en **español** como la presentación en **inglés** referencian exactamente el mismo script mediante `\lstinputlisting`:
  ```latex
  \lstinputlisting[language=Python, firstline=10, lastline=28, basicstyle=\fontsize{5.2pt}{6.1pt}\ttfamily]{../../code/02_teoria_probabilidad/02.06_random_sampling.py}
  ```

### Regla 2: Política de Cero Advertencias de Desbordamiento (*Zero Overfull Warning Policy*)
- Al compilar cualquier presentación Beamer en PDF mediante `pdflatex`, **ninguna diapositiva de contenido (páginas 2 en adelante) debe generar advertencias `Overfull \vbox` ni `Overfull \hbox`**.
- La portada (página 1) utiliza la convención estándar de Metropolis `\begin{frame}[plain] \titlepage \end{frame}`.
- **Técnicas obligatorias de prevención y corrección:**
  1. Uso del entorno de dos columnas `\begin{columns}[T]` para equilibrar la alineación vertical superior.
  2. Uso de tamaños de fuente compactos en el texto: `\small`, `\footnotesize`, `\scriptsize`.
  3. Control vertical fino entre bloques con `\vspace{-0.1cm}`, `\vspace{-0.15cm}` o `\vspace{-0.2cm}`.
  4. Reducción en la separación de listas: `\begin{itemize} \itemsep=0.03cm ... \end{itemize}`.
  5. En bloques de código largo, usar `\fontsize{5.0pt}{5.8pt}\selectfont` o dividir el laboratorio en múltiples diapositivas (p. ej., *Lab Python 1/4*, *2/4*, *3/4*, *4/4*).

### Regla 3: Identidad Institucional y Metadatos
Toda presentación (`.tex`) debe encabezarse estrictamente con los siguientes metadatos institucionales del autor y los archivos preámbulo compartidos:
```latex
% !TeX program = pdflatex
\documentclass[aspectratio=169,xcolor={dvipsnames,table}]{beamer}

\input{../../_preambulo_beamer}
\input{../../_comandos_beamer}

\title{Título del Tema}
\subtitle{Sección XX.YY --- Subtítulo del Tema}
\author[J. Castillo Colmenares]{Juliho Castillo Colmenares}
\institute[Tec de Monterrey]{Tecnológico de Monterrey}
\date{}
```
*Nota para presentaciones en inglés:* Se utiliza `\input{../../_en_preambulo_beamer}` y `\input{../../_en_comandos_beamer}` si están disponibles en la raíz de `presentaciones/`, o bien los preámbulos generales adaptados en inglés. Los bloques institucionales en `_preambulo_beamer.tex` ya configuran la paleta oficial: **TecRojo (`#EC2661`)** y **TecAzul (`#1A2E51`)**.

### Regla 4: Taxonomía de Problemas del Libro (*"3-3-2-2"*)
Cuando se cree o actualice una presentación, se debe verificar y sincronizar con el cuaderno de ejercicios complementario del libro maestro (`latex/<seccion>(p).tex`).
El estándar curricular exige que cada sección tenga **exactamente 10 problemas** divididos en 4 niveles (taxonomía *"3-3-2-2"*):
1. `\subsubsection*{Nivel 1: Fundamental (Conceptos básicos y directos)}` $\to$ **3 problemas**.
2. `\subsubsection*{Nivel 2: Operativo (Cálculo e implementación técnica)}` $\to$ **3 problemas**.
3. `\subsubsection*{Nivel 3: Analítico (Demostraciones y modelación matemática)}` $\to$ **2 problemas**.
4. `\subsubsection*{Nivel 4: Desafiante (Problemas avanzados o retos de ingeniería)}` $\to$ **2 problemas**.
Las presentaciones Beamer sintetizan la resolución de estos problemas en 4 diapositivas al final del mazo (*Ejercicios Nivel 1* a *Nivel 4*).

---

## 3. Checklist Reproducible de 6 Pasos para Añadir o Actualizar una Sección

Cualquier agente que trabaje en una nueva sección del libro (p. ej. Capítulo 03 en adelante) debe ejecutar y validar los siguientes pasos en orden cronológico exacto:

- [ ] **Paso 1: Auditoría de Teoría en LaTeX Maestro**
  - Abrir y leer `latex/<seccion>.tex` (o el capítulo correspondiente) para entender las fórmulas, definiciones, teoremas y notación exacta utilizada en el texto principal.
- [ ] **Paso 2: Cuaderno de Ejercicios (`(p).tex`) e Integración al Libro**
  - Verificar la existencia de `latex/<seccion>(p).tex`. Si no existe o no sigue la taxonomía 3-3-2-2, redactar/completar los 10 problemas con sus soluciones detalladas en los entornos de color institucional (`\begin{problema}`, `\begin{sugerencia}`, `\begin{solucion}`).
  - Asegurar que `\input{<seccion>(p)}` esté declarado en `latex/[Modelación Estadística].tex`.
  - Compilar el libro principal en la terminal: `cd latex && pdflatex "[Modelación Estadística].tex" && pdflatex "[Modelación Estadística].tex"`.
- [ ] **Paso 3: Desarrollo del Script de Simulación Python en Inglés**
  - Crear el archivo del laboratorio computacional en `presentaciones/code/<unidad>/<XX.YY_nombre>.py`.
  - Estructurar el script con bloques numerados (p. ej., `--- 1. Simulation A ---`, `--- 2. Convergence B ---`) y funciones claras de verificación que arrojen resultados numéricos por consola equivalentes a las demostraciones analíticas.
  - Ejecutar y probar el script en terminal para verificar sintaxis y precisión: `python <script>.py`.
- [ ] **Paso 4: Redacción de Presentaciones Beamer (ES / EN)**
  - Crear o actualizar el archivo en español `presentaciones/es/<unidad>/<seccion>.tex` (objetivo estándar: 20 diapositivas que incluyan portada, hoja de ruta, motivación, teoría, 4 diapositivas del laboratorio de Python importando el código externo, 4 diapositivas de ejercicios 3-3-2-2, síntesis y puente didáctico).
  - Crear o actualizar la versión en inglés `presentaciones/en/<unidad>/<section>.tex` manteniendo simetría total y la misma importación al script `.py` en inglés.
- [ ] **Paso 5: Compilación Doble y Verificación Cero Advertencias (*Zero Overfull Check*)**
  - Compilar ambas presentaciones dos veces desde sus respectivos directorios:
    ```bash
    cd presentaciones/es/<unidad>/ && pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
    cd ../../en/<unidad>/ && pdflatex -interaction=nonstopmode <archivo>.tex && pdflatex -interaction=nonstopmode <archivo>.tex
    ```
  - **Revisar el archivo de registro (`<archivo>.log`)**: Buscar `Overfull \vbox` o `Overfull \hbox`. Si aparecen en las páginas 2 a N, ajustar márgenes verticalmente (`\vspace`), reducir fuente del bloque de código (`\fontsize{..}{..}\selectfont`) o reestructurar columnas hasta obtener 0 advertencias de contenido.
- [ ] **Paso 6: Commit de Cambios y Actualización de Documentación**
  - Hacer un `git status` para comprobar que se generaron los `.tex`, `.pdf`, `.py` y el `(p).tex`.
  - Actualizar el registro en `CHANGELOG.md` y verificar/actualizar el catálogo e índice en este archivo y en `ROADMAP.md`.

---

## 4. Catálogo e Índice de Presentaciones --- Capítulo 02 (100% Completado)

A continuación se presenta el estado finalizado y verificado de las 6 secciones correspondientes a la **Unidad 1 / Capítulo 02: Teoría de la Probabilidad**:

| Sección | Título en Español | Título en Inglés | Script Python (en `code/02_teoria_probabilidad/`) | Estado |
| :---: | :--- | :--- | :--- | :---: |
| **02.01** | [02.01 Introducción a la Probabilidad](es/02_teoria_probabilidad/02.01_introduccion_probabilidad.tex) ([PDF](es/02_teoria_probabilidad/02.01_introduccion_probabilidad.pdf)) | [02.01 Intro to Probability](en/02_probability_theory/02.01_intro_probability.tex) ([PDF](en/02_probability_theory/02.01_intro_probability.pdf)) | `02.01_intro_probability.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.02** | [02.02 Conjuntos y Particiones](es/02_teoria_probabilidad/02.02_conjuntos_y_particiones.tex) ([PDF](es/02_teoria_probabilidad/02.02_conjuntos_y_particiones.pdf)) | [02.02 Sets and Partitions](en/02_probability_theory/02.02_sets_and_partitions.tex) ([PDF](en/02_probability_theory/02.02_sets_and_partitions.pdf)) | `02.02_sets_and_partitions.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.03** | [02.03 Fundamentos y Axiomas](es/02_teoria_probabilidad/02.03_fundamentos_probabilidad.tex) ([PDF](es/02_teoria_probabilidad/02.03_fundamentos_probabilidad.pdf)) | [02.03 Probability Fundamentals](en/02_probability_theory/02.03_probability_fundamentals.tex) ([PDF](en/02_probability_theory/02.03_probability_fundamentals.pdf)) | `02.03_probability_fundamentals.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.04** | [02.04 Probabilidad Condicional](es/02_teoria_probabilidad/02.04_probabilidad_condicional.tex) ([PDF](es/02_teoria_probabilidad/02.04_probabilidad_condicional.pdf)) | [02.04 Conditional Probability](en/02_probability_theory/02.04_conditional_probability.tex) ([PDF](en/02_probability_theory/02.04_conditional_probability.pdf)) | `02.04_conditional_probability.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.05** | [02.05 Teorema de Bayes](es/02_teoria_probabilidad/02.05_teorema_bayes.tex) ([PDF](es/02_teoria_probabilidad/02.05_teorema_bayes.pdf)) | [02.05 Bayes' Theorem](en/02_probability_theory/02.05_bayes_theorem.tex) ([PDF](en/02_probability_theory/02.05_bayes_theorem.pdf)) | `02.05_bayes_theorem.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |
| **02.06** | [02.06 Muestreo y TLC](es/02_teoria_probabilidad/02.06_muestreo_aleatorio.tex) ([PDF](es/02_teoria_probabilidad/02.06_muestreo_aleatorio.pdf)) | [02.06 Random Sampling & CLT](en/02_probability_theory/02.06_random_sampling.tex) ([PDF](en/02_probability_theory/02.06_random_sampling.pdf)) | `02.06_random_sampling.py` | $\checkmark$ **Completado (20 diapositivas, 0 warnings)** |

---

## 5. Próximo Trabajo y Hoja de Ruta (`ROADMAP.md`)

Para ver la planificación del siguiente hito curricular del proyecto (inicio de la **Unidad 2 / Capítulo 03: Variables Aleatorias Discretas y Distribuciones de Probabilidad**), consulta el documento oficial de planificación:
👉 **[presentaciones/ROADMAP.md](ROADMAP.md)**.
