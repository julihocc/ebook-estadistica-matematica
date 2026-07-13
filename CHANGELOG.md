# Changelog

Este changelog resume la evolución del repositorio a partir del historial de Git.
Como el proyecto no usa versiones ni tags de lanzamiento, los cambios se agrupan
por fechas e hitos editoriales.

## 2026-07-13

### Cambiado
- Adscripción del autor en la portada (`\publisher`) actualizada de
  `www.optimum.mx` a Tecnológico de Monterrey, Escuela de Ingeniería y
  Ciencias, Campus Ciudad de México, con correo de contacto
  `julihocc@tec.mx`.
- Paleta de colores del libro (encabezados, entornos `solucion` y
  `algoritmo`) ajustada para acercarse a los colores institucionales del
  Tecnológico de Monterrey.

## 2026-07-12

### Cambiado
- Estandarización de la estructura de problemas en los 16 archivos `(p).tex`
  del libro a un esquema de dificultad por niveles ("3-3-2-2"): 3 problemas
  de Nivel Fundamental, 3 de Nivel Operativo, 2 de Nivel Analítico y 2 de
  Nivel Desafiante, en cada tema. Aplicado a:
  - Estadística descriptiva: `medidas_dispersion(p)`,
    `medidas_tendencia_central(p)`.
  - Teoría de probabilidad: `conjuntos(p)`, `fundamentos_de_probabilidad(p)`,
    `probabilidad_condicional(p)`, `teorema_de_bayes(p)`.
  - Estimación e intervalos: `estadisticos_z_t(p)`,
    `estimacion_intervalos_avanzado(p)`, `estimacion_puntual(p)`,
    `intervalos_de_confianza(p)`.
  - Chi-cuadrada, hipótesis y ANOVA: `chi_cuadrada(p)`,
    `diseno_experimentos_anova(p)`, `pruebas_hipotesis_avanzadas(p)`.
  - Regresión lineal, múltiple y validación de modelos:
    `regresion_multiple(p)`, `regresiones_lineales(p)`,
    `validacion_modelo(p)`.
- Actualización de artefactos de compilación con el PDF resultante de 444
  páginas.

## 2026-07-10

### Añadido
- Ejemplos de código en `code/` para los temas de chi-cuadrada, distribuciones
  continuas avanzadas, distribuciones especiales, distribuciones de muestreo,
  estadísticos `z`/`t` y regresión.
- Scripts auxiliares `fix_regresion2.py` y `limpieza_final.py` para limpieza y
  ajuste de contenido.

### Cambiado
- Integración de listados externos de Python dentro del ebook mediante
  `\lstinputlisting`.
- Corrección de referencias internas tras la renumeración del capítulo 3
  (`sec:3.8` → `sec:3.9`).
- Actualización de artefactos de compilación, incluyendo el PDF principal del
  libro.

## 2026-07-09

### Añadido
- `AGENTS.md` con instrucciones de compilación y convenciones editoriales del
  repositorio.
- `docs/MA1001B - Analítico.pdf` como referencia del programa/sílabo.
- Nuevo tema de distribuciones continuas avanzadas: uniforme, normal, gamma y
  familia FGM.
- Nueva sección de distribuciones de muestreo avanzadas.

### Cambiado
- Mejora integral de los capítulos 1 a 4:
  - Capítulo 1: estadística descriptiva.
  - Capítulo 2: probabilidad.
  - Capítulo 3: estadística inferencial.
  - Capítulo 4: regresiones lineales.
- Expansión del capítulo 2 con distribuciones geométrica, binomial negativa,
  hipergeométrica y aplicaciones a ciencia de datos.
- Migración de los capítulos 1 a 4 al sistema unificado de numeración
  `[cap.sec.item]`.
- Migración de archivos huérfanos (`pe-*.tex` y `probabilidad-basica.tex`) al
  mismo esquema de numeración.

### Mantenimiento
- Validación final de compilación limpia sin advertencias por etiquetas
  duplicadas.
- Ajustes en `.gitattributes` para retirar la configuración de Git LFS para
  archivos PDF, después de una configuración transitoria.
- Registro de sesión añadido al repositorio.

## 2021-10-24 a 2021-08-02

### Cambiado
- Corrección del teorema 2.2.6.
- Incorporación de la carpeta de soluciones.
- Ajuste de enlaces o referencia institucional a `optimum.mx`.

### Notas
- Este tramo contiene un commit con mensaje poco descriptivo (`No recuerdo que
  hice`), por lo que el cambio exacto no puede reconstruirse con confianza
  solo a partir del mensaje.

## 2021-07-18 a 2021-07-02

### Fundación del proyecto
- Creación inicial del repositorio y del `README.md`.
- Adopción de la licencia CC BY 4.0.
- Incorporación de la base LaTeX del libro y consolidación del contenido dentro
  de `latex/`.
- Renombrado y normalización temprana de nombres de archivo.
- Cambio editorial del título de la sección de conteo a notación de conjuntos.
- Inclusión del primer ejercicio publicado en YouTube.
- Primeros merges sobre `main` durante la etapa de arranque.

## Lectura general de la historia

La historia del repositorio muestra dos etapas claras:

1. **2021:** arranque del libro, definición de licencia, estructura LaTeX base
   y primeras decisiones editoriales.
2. **2026:** reactivación intensa del proyecto con expansión del contenido,
   unificación de numeración, mejora de capítulos, incorporación de ejemplos de
   código y actualización del PDF final.
