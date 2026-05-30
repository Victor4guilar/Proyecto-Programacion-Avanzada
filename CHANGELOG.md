# CHANGELOG

## v1.0.0 - 17-04-2026 - Jonathan Sánchez Pérez - Perez-png2

### Agregado
- Interfaz gráfica básica desarrollada con Tkinter
- Implementación del Método de Bisección
- Entrada de función matemática como texto
- Validación de intervalo (cambio de signo)
- Visualización de resultados en interfaz
- Gráfica del error vs iteraciones

### Mejoras
- Organización inicial del repositorio
- Separación de lógica y visualización en la interfaz

### Pruebas
- Pruebas manuales con funciones polinomiales
- Validación de convergencia del método

---

## v1.1.0 - 05-05-2026 - Axel de Jesús Ronzón Pérez - IAtevoy

### Agregado
- Implementación del Método de Falsa Posición
- Integración del método en la interfaz gráfica existente
- Selección dinámica entre métodos (Bisección y Falsa Posición)

### Mejoras
- Reutilización de los mismos campos de entrada para múltiples métodos
- Mejora en la estructura del código para soportar nuevos métodos
- Visualización del método seleccionado en los resultados

### Pruebas
- Pruebas manuales con funciones exponenciales y polinomiales
- Validación de convergencia del método de Falsa Posición
- Comparación básica entre Bisección y Falsa Posición

---

## v1.2.0 - 06-05-2026 - Víctor Aguilar Ortiz - Victor4guilar

### Agregado
- Implementación del Método de Newton-Raphson
- Entrada dinámica para la derivada de la función \(f'(x)\)
- Integración del método de Newton-Raphson en la interfaz gráfica
- Soporte para métodos abiertos dentro de la misma estructura del programa
- Cálculo iterativo de raíces mediante aproximaciones sucesivas
- Visualización gráfica del error vs iteraciones para Newton-Raphson

### Mejoras
- Adaptación dinámica de los campos de entrada según el método seleccionado
- Reutilización de la lógica de evaluación de funciones para derivadas
- Mejora en la escalabilidad del programa para agregar nuevos métodos numéricos
- Optimización de la estructura condicional en la carga y ejecución de métodos
- Mejor organización del manejo de resultados y validaciones

### Pruebas
- Pruebas manuales con funciones polinomiales y trascendentales
- Validación de convergencia del método de Newton-Raphson
- Comparación básica de velocidad de convergencia entre métodos cerrados y abiertos
- Verificación de funcionamiento correcto de las derivadas ingresadas por el usuario

---

## v1.3.0 - 07-05-2026 - Gabriel Beltrán Amezcua - Th3PapaY0ch1S08

### Agregado
- Implementación del Método de la Secante
- Integración del método de la Secante en la interfaz gráfica
- Inclusión de dos puntos iniciales \(x_0\) y \(x_1\) para métodos abiertos
- Cálculo iterativo de raíces mediante aproximaciones secantes sucesivas
- Límite máximo de iteraciones para evitar ciclos infinitos
- Validación para evitar divisiones entre cero en el método de la Secante
- Visualización gráfica de la convergencia del error para el método de la Secante

### Mejoras
- Reestructuración de la interfaz para soportar métodos cerrados y abiertos de forma más organizada
- Optimización del sistema dinámico de carga de entradas según el método seleccionado
- Mejora en el manejo de excepciones mostrando detalles específicos del error
- Actualización de la ventana principal y dimensiones de la interfaz
- Mejora en la presentación de resultados incluyendo raíz estimada, error final e iteraciones
- Optimización de la función de evaluación matemática reutilizable entre métodos
- Mejora visual en las gráficas de convergencia agregando cuadrícula y marcadores

### Pruebas
- Pruebas manuales con funciones polinomiales, exponenciales y logarítmicas
- Validación de convergencia del método de la Secante
- Comparación básica de rapidez de convergencia entre Newton-Raphson y Secante
- Verificación de estabilidad ante posibles divisiones entre cero
- Pruebas de funcionamiento dinámico de la interfaz para los cuatro métodos implementados

---

## v1.4.0 - 08-05-2026 - Jonathan Sánchez Pérez - Perez-png2

### Agregado
- Implementación del Método de Punto Fijo
- Integración del método de Punto Fijo en la interfaz gráfica principal
- Inclusión de entrada dinámica para valor inicial \(x_0\)
- Cálculo iterativo mediante funciones de iteración \(g(x)\)
- Visualización gráfica de la convergencia del error para el método de Punto Fijo
- Inclusión del método en el selector dinámico de métodos numéricos
- Control de iteraciones máximas para evitar ciclos infinitos

### Mejoras
- Optimización de la estructura de carga dinámica de entradas según el método seleccionado
- Reutilización completa del sistema de evaluación matemática para funciones iterativas
- Mejora en la estabilidad de cálculo evitando errores por división entre cero
- Consolidación de la arquitectura modular para soportar más métodos abiertos
- Mejora en la interfaz gráfica manteniendo compatibilidad entre todos los métodos implementados
- Optimización del flujo de ejecución y visualización de resultados
- Actualización del sistema de estado dinámico de la aplicación

### Pruebas
- Pruebas manuales con funciones iterativas algebraicas y trascendentales
- Validación de convergencia del método de Punto Fijo
- Comparación básica de convergencia entre Punto Fijo, Newton-Raphson y Secante
- Verificación de estabilidad numérica en distintas tolerancias
- Pruebas dinámicas de funcionamiento conjunto de los cinco métodos implementados

---

## v1.5.0 - 09-05-2026 - Axel de Jesús Ronzón Pérez - IAtevoy

### Agregado
- Implementación del Método de Búsqueda por Incrementos
- Integración del método de Búsqueda por Incrementos en la interfaz gráfica
- Detección automática de intervalos con cambio de signo
- Inclusión de parámetros dinámicos para intervalo inicial, intervalo final e incremento
- Visualización de posibles raíces mediante intervalos detectados
- Gráfica de la función evaluada durante la búsqueda por incrementos
- Clasificación visual de métodos en "Raíces Cerradas" y "Raíces Abiertas" dentro del selector de métodos
- Sistema de validación para impedir la selección de encabezados de categorías en el ComboBox

### Mejoras
- Reestructuración visual del menú de selección de métodos para una navegación más intuitiva
- Mejora en la organización de métodos numéricos según su clasificación teórica
- Adaptación dinámica de entradas dependiendo del método seleccionado
- Optimización del controlador de eventos del ComboBox mediante validación automática
- Mejora en la presentación de resultados para métodos de detección de intervalos
- Separación más clara entre métodos iterativos y métodos de búsqueda de raíces por intervalo
- Optimización del flujo gráfico para soportar distintos tipos de visualización matemática

### Pruebas
- Pruebas manuales con funciones trigonométricas, polinomiales y exponenciales
- Validación de detección correcta de cambios de signo en distintos intervalos
- Verificación de estabilidad del incremento en búsquedas amplias y pequeñas
- Comparación visual entre intervalos detectados y raíces reales de funciones
- Pruebas de funcionamiento dinámico del selector categorizado de métodos
- Verificación del bloqueo correcto de selección en encabezados del ComboBox
- Pruebas integrales de compatibilidad entre los seis métodos implementados

---

## v1.6.0 - 12-05-2026 - Víctor Aguilar Ortiz - Victor4guilar

### Agregado
- Implementación del Método de Mínimos Cuadrados Lineales
- Integración del método de ajuste de curvas en la interfaz gráfica principal
- Inclusión de una nueva categoría visual llamada "Ajuste de Curvas" dentro del selector de métodos
- Entrada dinámica de arreglos de datos \(X\) y \(Y\) separados por comas
- Cálculo automático de la pendiente \(a\) e intercepto \(b\) de la recta ajustada
- Generación de la función ajustada en la forma \(y = ax + b\)
- Visualización gráfica de la recta de ajuste obtenida mediante mínimos cuadrados
- Validación de igualdad de tamaño entre los arreglos de datos ingresados

### Mejoras
- Adaptación de la interfaz para soportar métodos de ajuste de datos además de métodos de búsqueda de raíces
- Optimización de la carga dinámica de entradas dependiendo del tipo de método seleccionado
- Reutilización de la estructura gráfica existente para mostrar resultados de regresión lineal
- Mejora en la organización del selector de métodos agregando separación temática entre categorías
- Optimización del sistema de resultados para mostrar parámetros matemáticos del ajuste lineal
- Consolidación de la arquitectura modular permitiendo integrar futuros métodos estadísticos y de interpolación
- Mejora en la compatibilidad entre visualización gráfica y métodos no iterativos

### Pruebas
- Pruebas manuales con conjuntos de datos lineales y semi-lineales
- Validación del cálculo correcto de pendiente e intercepto
- Verificación gráfica de la recta ajustada respecto a los datos ingresados
- Comparación básica de resultados con cálculos manuales de regresión lineal
- Pruebas de manejo de errores en arreglos de distinto tamaño
- Verificación del correcto funcionamiento dinámico de la interfaz para métodos de ajuste de curvas
- Pruebas integrales de compatibilidad entre los siete métodos implementados

---

## v1.7.0 - 13-05-2026 - Gabriel Beltrán Amezcua - Th3PapaY0ch1S08

### Agregado
- Implementación del Método de Interpolación Lineal de Newton
- Integración del método de interpolación dentro de la categoría "Ajuste de Curvas"
- Inclusión de entradas dinámicas para los puntos \((x_0, y_0)\) y \((x_1, y_1)\)
- Entrada para el valor \(x\) a interpolar
- Cálculo automático de los coeficientes de interpolación lineal de Newton
- Obtención del valor interpolado mediante la fórmula de Newton de primer grado
- Visualización gráfica de los puntos conocidos y del punto interpolado
- Inclusión del coeficiente \(b_1\) (pendiente) dentro de los resultados mostrados
- Compatibilidad completa del método con la arquitectura modular existente

### Mejoras
- Reestructuración de la interfaz para soportar métodos de interpolación además de ajuste de curvas y búsqueda de raíces
- Optimización de la carga dinámica de entradas específicas para métodos de interpolación
- Separación lógica del flujo de ejecución para métodos no iterativos
- Mejora en la presentación gráfica diferenciando puntos conocidos y valores interpolados
- Optimización del sistema de resultados para mostrar parámetros matemáticos relevantes del proceso de interpolación
- Consolidación de la categoría "Ajuste de Curvas" incorporando métodos de regresión e interpolación
- Mejora en la organización interna del controlador de ejecución para soportar distintos tipos de métodos numéricos
- Adaptación del sistema de validación para excluir métodos de interpolación del uso de tolerancias iterativas

### Pruebas
- Pruebas manuales con conjuntos de datos lineales simples
- Verificación del cálculo correcto del coeficiente \(b_1\)
- Validación del valor interpolado comparándolo con cálculos manuales
- Pruebas gráficas del comportamiento de la recta interpolada
- Verificación de funcionamiento correcto de entradas dinámicas para interpolación
- Pruebas de estabilidad en distintos intervalos de interpolación
- Validación de compatibilidad entre métodos iterativos, ajuste de curvas e interpolación
- Pruebas integrales de funcionamiento conjunto de los ocho métodos implementados

---

## v1.8.0 - 15-05-2026 - Jonathan Sánchez Pérez - Perez-png2

### Agregado
- Implementación del Método de Mínimos Cuadrados Polinomiales
- Integración del ajuste polinomial dentro de la categoría "Ajuste de Curvas"
- Inclusión de soporte para regresión polinomial de distintos grados
- Entrada dinámica para el grado del polinomio ajustado
- Uso de la librería NumPy para el cálculo automático de coeficientes polinomiales
- Generación automática del polinomio ajustado a partir de los datos ingresados
- Visualización gráfica del ajuste polinomial mediante curvas suavizadas
- Representación gráfica simultánea de los puntos experimentales y la curva ajustada
- Inclusión de los coeficientes del polinomio dentro de los resultados mostrados
- Construcción dinámica de la ecuación polinomial ajustada en formato legible

### Mejoras
- Optimización de la arquitectura de ajuste de curvas para soportar regresiones de orden superior
- Reestructuración de la interfaz para incorporar métodos estadísticos más avanzados
- Mejora en la organización de entradas dinámicas reutilizando componentes para métodos de regresión
- Actualización del tamaño de la ventana principal para mejorar la visualización de resultados y gráficas
- Optimización del flujo de generación de gráficas utilizando curvas suavizadas con NumPy
- Consolidación de la categoría "Ajuste de Curvas" integrando regresión lineal, polinomial e interpolación
- Mejora en la presentación matemática de resultados mostrando funciones polinomiales completas
- Adaptación del sistema gráfico para representar funciones no lineales de manera más precisa
- Optimización del código interno mediante uso de funciones vectorizadas de NumPy

### Pruebas
- Pruebas manuales con conjuntos de datos cuadráticos y cúbicos
- Verificación del cálculo correcto de coeficientes polinomiales para distintos grados
- Validación visual del ajuste de curvas respecto a los datos experimentales
- Comparación básica entre regresión lineal y regresión polinomial
- Verificación de estabilidad gráfica utilizando diferentes cantidades de puntos
- Pruebas de funcionamiento correcto para polinomios de segundo y tercer grado
- Validación de construcción correcta de la ecuación polinomial mostrada en resultados
- Pruebas integrales de compatibilidad entre métodos iterativos, interpolación y ajuste de curvas
- Verificación de integración correcta de NumPy dentro de la arquitectura de la aplicación

---

## v1.9.0 - 16-05-2026 - Axel de Jesús Ronzón Pérez - IAtevoy

### Agregado
- Implementación del Método de Polinomios de Interpolación de Newton
- Integración del método dentro de la categoría "Ajuste de Curvas"
- Inclusión de soporte para interpolación polinomial de orden arbitrario mediante diferencias divididas
- Entrada dinámica de arreglos de datos \(X\) y \(Y\) separados por comas
- Inclusión de entrada para el valor \(x\) a interpolar
- Construcción automática de la tabla de diferencias divididas
- Obtención automática de coeficientes \(b_0, b_1, b_2, ...\) del polinomio de Newton
- Evaluación automática del polinomio interpolante en cualquier punto ingresado
- Visualización de la tabla completa de diferencias divididas dentro de los resultados
- Representación gráfica de la curva interpolada generada mediante el polinomio de Newton
- Visualización del punto interpolado sobre la gráfica
- Uso de NumPy para generación de curvas suavizadas en la representación gráfica
- Compatibilidad del método con interpolaciones de orden superior utilizando múltiples puntos

### Mejoras
- Reestructuración de la arquitectura de interpolación para soportar métodos polinomiales avanzados
- Optimización del sistema dinámico de entradas para métodos basados en tablas de datos
- Consolidación de la categoría "Ajuste de Curvas" incorporando interpolación lineal y polinomial de Newton
- Mejora en la visualización matemática mostrando coeficientes y tabla de diferencias divididas
- Adaptación del flujo de ejecución para soportar métodos de interpolación no iterativos de orden superior
- Optimización del sistema gráfico para representar curvas interpoladas suaves utilizando múltiples evaluaciones
- Mejora en la organización interna de métodos de interpolación separando interpolación lineal y polinomial
- Reutilización de estructuras gráficas y de visualización existentes para mantener compatibilidad entre métodos
- Optimización del manejo dinámico de resultados para métodos basados en tablas matemáticas
- Consolidación de la arquitectura modular permitiendo futuras expansiones de métodos de interpolación

### Pruebas
- Pruebas manuales con interpolaciones polinomiales de tercer y quinto orden
- Verificación del cálculo correcto de diferencias divididas
- Validación de coeficientes del polinomio de Newton comparados con cálculos manuales
- Pruebas de interpolación utilizando funciones polinomiales y logarítmicas
- Verificación gráfica de la curva interpolada respecto a los puntos originales
- Validación del cálculo correcto del valor interpolado en distintos puntos
- Pruebas de estabilidad utilizando diferentes cantidades de datos
- Comparación básica entre interpolación lineal y polinomial de Newton
- Verificación de funcionamiento correcto de gráficas suavizadas utilizando NumPy
- Pruebas integrales de compatibilidad entre métodos iterativos, regresión e interpolación
- Validación del funcionamiento correcto de la tabla de diferencias divididas en la interfaz
- Pruebas conjuntas de los nueve métodos implementados en la aplicación

---

## v1.10.0 - 19-05-2026 - Víctor Aguilar Ortiz - Victor4guilar

### Agregado
- Implementación del Método de Interpolación de Lagrange
- Integración del método dentro de la categoría "Ajuste de Curvas"
- Inclusión de soporte para interpolación polinomial utilizando la formulación clásica de Lagrange
- Entrada dinámica de arreglos de datos \(X\) y \(Y\) separados por comas
- Inclusión de entrada para el valor \(x\) a interpolar
- Cálculo automático de los polinomios base \(L_i(x)\)
- Evaluación automática del polinomio interpolante para cualquier punto ingresado
- Validación para impedir valores repetidos en los datos de entrada \(X\)
- Representación gráfica de la curva interpolada generada mediante el método de Lagrange
- Visualización simultánea de puntos experimentales y curva interpolada
- Visualización del punto interpolado directamente sobre la gráfica
- Uso de NumPy para generar curvas suavizadas en la representación visual
- Compatibilidad del método con interpolaciones polinomiales de orden superior utilizando múltiples puntos

### Mejoras
- Reestructuración de la arquitectura interna de interpolación para soportar múltiples técnicas polinomiales
- Consolidación de la categoría "Ajuste de Curvas" incorporando Interpolación Lineal de Newton, Polinomios de Newton e Interpolación de Lagrange
- Optimización del sistema dinámico de entradas reutilizando estructuras existentes
- Mejora en la organización del flujo de ejecución para métodos de interpolación no iterativos
- Adaptación del sistema gráfico para representar funciones interpoladas mediante múltiples evaluaciones sucesivas
- Reutilización de la infraestructura gráfica existente para mantener compatibilidad entre métodos
- Optimización del manejo dinámico de resultados dentro de la interfaz
- Consolidación de la arquitectura modular permitiendo futuras expansiones de métodos numéricos
- Integración completa del método con el sistema de carga automática y ejecución dinámica de la aplicación

### Pruebas
- Pruebas manuales con conjuntos de datos polinomiales de distintos órdenes
- Validación del cálculo correcto de interpolación utilizando múltiples puntos
- Comparación básica entre Interpolación de Newton y Lagrange
- Verificación del valor interpolado mediante cálculos manuales
- Validación gráfica de la curva interpolada respecto a los datos originales
- Verificación del correcto funcionamiento para distintos tamaños de arreglos de datos
- Pruebas de estabilidad ante diferentes distribuciones de puntos experimentales
- Validación del sistema de detección de valores repetidos en \(X\)
- Verificación del funcionamiento correcto de gráficas suavizadas utilizando NumPy
- Pruebas integrales de compatibilidad entre métodos iterativos, regresión e interpolación
- Validación del correcto funcionamiento dinámico de entradas y resultados
- Pruebas conjuntas de los diez métodos implementados en la aplicación

---

## v1.11.0 - 19-05-2026 - Gabriel Beltrán Amezcua - Th3PapaY0ch1S08

### Agregado
- Implementación del Método de Diferencias Finitas para Derivación Numérica
- Integración de una nueva categoría visual llamada "Derivación Numérica" dentro del selector de métodos
- Inclusión del método "Diferencias Finitas" dentro de la arquitectura principal de la aplicación
- Entrada dinámica de función matemática \(f(x)\)
- Inclusión de parámetro dinámico para valor de evaluación \(x\)
- Inclusión de parámetro dinámico para tamaño de paso \(h\)
- Implementación de aproximación de Primera Derivada mediante Diferencias Finitas Hacia Adelante
- Implementación de aproximación de Primera Derivada mediante Diferencias Finitas Hacia Atrás
- Implementación de aproximación de Primera Derivada mediante Diferencias Finitas Centrales
- Implementación de aproximación de Segunda Derivada mediante Diferencias Finitas Hacia Adelante
- Implementación de aproximación de Segunda Derivada mediante Diferencias Finitas Hacia Atrás
- Implementación de aproximación de Segunda Derivada mediante Diferencias Finitas Centrales
- Visualización simultánea de resultados de derivación numérica dentro del panel de resultados
- Representación gráfica de la función original utilizada para el cálculo de derivadas
- Visualización gráfica del punto evaluado sobre la función
- Compatibilidad con funciones algebraicas, trigonométricas, exponenciales y logarítmicas
- Integración completa con el sistema de evaluación matemática reutilizable existente

### Mejoras
- Expansión de la arquitectura modular para soportar métodos de derivación numérica
- Reestructuración del selector de métodos incorporando una nueva clasificación temática
- Optimización del sistema dinámico de entradas permitiendo configuración específica para métodos de derivación
- Mejora en la organización interna separando métodos de raíces, ajuste de curvas y derivación numérica
- Optimización del flujo de ejecución para soportar cálculos numéricos no iterativos adicionales
- Consolidación del sistema gráfico reutilizando infraestructura existente de visualización matemática
- Mejora en la presentación de resultados agrupando derivadas de primer y segundo orden
- Optimización del manejo de funciones evaluadas mediante reutilización del motor matemático interno
- Adaptación de la interfaz para soportar futuras expansiones relacionadas con cálculo numérico
- Fortalecimiento de la arquitectura modular permitiendo integración de nuevos métodos avanzados

### Pruebas
- Pruebas manuales utilizando funciones polinomiales
- Pruebas de derivación con funciones trigonométricas
- Validación numérica utilizando funciones exponenciales y logarítmicas
- Comparación básica entre aproximaciones hacia adelante, hacia atrás y centrales
- Verificación del comportamiento utilizando distintos tamaños de paso \(h\)
- Validación del cálculo correcto de primera y segunda derivada
- Verificación gráfica de la función evaluada respecto al punto seleccionado
- Pruebas de estabilidad numérica con diferentes valores de entrada
- Validación del funcionamiento dinámico de entradas específicas para derivación numérica
- Pruebas integrales de compatibilidad entre métodos de raíces, interpolación, regresión y derivación
- Verificación de integración correcta dentro de la arquitectura general de la aplicación
- Pruebas conjuntas de los once métodos implementados en la Suite de Métodos Numéricos

---

## v1.12.0 - 20-05-2026 - Jonathan Sánchez Pérez - Perez-png2

### Agregado
- Implementación del Método del Trapecio para Integración Numérica
- Creación de la nueva categoría "Integración Numérica" dentro del selector de métodos
- Inclusión del método "Trapecio" dentro de la Suite de Métodos Numéricos
- Entrada dinámica para función matemática f(x)
- Inclusión de límite inferior de integración
- Inclusión de límite superior de integración
- Implementación de cálculo automático de integral definida mediante la Regla del Trapecio
- Evaluación automática de extremos del intervalo de integración
- Visualización del resultado numérico dentro del panel de resultados
- Representación gráfica de la función evaluada
- Visualización geométrica del área aproximada mediante trapecios
- Compatibilidad con funciones algebraicas
- Compatibilidad con funciones trigonométricas
- Compatibilidad con funciones exponenciales
- Compatibilidad con funciones logarítmicas
- Integración con el motor matemático reutilizable existente

### Mejoras
- Expansión de la arquitectura modular para soportar métodos de integración numérica
- Reorganización estructural del selector de métodos incorporando una nueva categoría temática
- Optimización del sistema dinámico de entradas para cálculos de integración
- Consolidación de separación conceptual entre raíces, interpolación, derivación e integración numérica
- Adaptación del sistema gráfico para representar aproximaciones geométricas de áreas
- Reutilización del sistema interno de evaluación matemática
- Optimización del flujo de ejecución para métodos de integración
- Fortalecimiento de la arquitectura modular permitiendo futuras expansiones relacionadas con integración numérica avanzada
- Mejora de compatibilidad entre módulos previamente implementados

### Pruebas
- Pruebas manuales utilizando funciones polinomiales
- Validación utilizando funciones trigonométricas
- Verificación utilizando funciones exponenciales
- Verificación utilizando funciones logarítmicas
- Comparación básica entre resultado numérico y solución analítica conocida
- Validación del comportamiento utilizando distintos intervalos de integración
- Verificación gráfica de aproximación geométrica mediante trapecios
- Validación del funcionamiento dinámico de entradas específicas para integración numérica
- Pruebas de compatibilidad con métodos previamente implementados
- Validación integral de funcionamiento de los doce métodos disponibles en la aplicación

---

## v1.13.0 - 22-05-2026 - Axel de Jesús Ronzón Pérez - IAtevoy

### Agregado
- Método de Integración de Simpson.
- Implementación de Simpson 1/3 Simple.
- Implementación de Simpson 1/3 Múltiple.
- Implementación de Simpson 3/8 Simple.
- Implementación de Simpson 3/8 Compuesta.
- Cálculo automático de error porcentual relativo.
- Gráfica del Método de Simpson mostrando:
  - Curva de la función.
  - División de subintervalos.
  - Puntos usados por Simpson.
- Organización visual de métodos por categorías:
  - Raíces Cerradas.
  - Raíces Abiertas.
  - Regresión e Interpolación.
  - Derivación Numérica.
  - Integración Numérica.

### Mejorado
- Interfaz de Interpolación Lineal de Newton simplificada.
- Entrada de datos más intuitiva usando:
  - Valores X.
  - Valores Y.
  - Incremento.
- Organización interna del selector de métodos.
- Experiencia visual general de la interfaz.
- Compatibilidad mejorada para funciones matemáticas.
- Integración visual del Método de Simpson.

### Corregido
- Eliminado bloque duplicado de "Función" en Diferencias Finitas.
- Eliminado bloque duplicado de "Función" en Método de Trapecios.
- Corregido conflicto visual entre Tolerancia y Simpson.
- Corregido posicionamiento de controles del Método de Simpson.
- Corregida reconstrucción dinámica de widgets.
- Corregidos problemas visuales al cambiar entre métodos.
- Corregida selección de métodos agrupados.

---

## v2.0.0 - 24-05-2026 - Jonathan Sánchez Pérez - Perez-png2

### Agregado
- Implementación de búsqueda dinámica de métodos mediante escritura directa dentro del selector "Método"
- Integración de filtrado automático de métodos conforme el usuario escribe
- Conservación del sistema de selección tradicional mediante ComboBox desplegable
- Inclusión de nueva opción "Tipo de Error para Gráficas"
- Implementación de selección entre:
  - Error Absoluto
  - Error Relativo
  - Error Porcentual
- Incorporación de cálculo dinámico del error seleccionado durante las iteraciones
- Generación automática de gráficas utilizando el tipo de error elegido por el usuario
- Integración del nuevo sistema de errores en:
  - Método de Bisección
  - Método de Falsa Posición
  - Método de Newton-Raphson
  - Método de Punto Fijo
- Sustitución de gráficas tradicionales de convergencia por gráficas dinámicas basadas en el error seleccionado
- Centralización del cálculo de errores mediante función reutilizable interna

### Mejoras
- Optimización de experiencia de usuario permitiendo búsqueda rápida de métodos numéricos
- Mejora en la navegación del selector de métodos reduciendo tiempo de localización
- Reestructuración interna del sistema gráfico para soportar múltiples tipos de error
- Adaptación modular de métodos iterativos para compartir la misma lógica de cálculo de error
- Mejora en la arquitectura interna permitiendo futuras expansiones de métricas numéricas
- Optimización del flujo de visualización de convergencia matemática
- Consolidación del manejo dinámico de gráficas dentro de métodos iterativos
- Mejora en la flexibilidad del análisis numérico permitiendo distintas métricas de precisión

### Pruebas
- Pruebas manuales de escritura dinámica en selector de métodos
- Verificación de filtrado automático utilizando nombres parciales de métodos
- Validación de cálculo de Error Absoluto
- Validación de cálculo de Error Relativo
- Verificación de generación gráfica utilizando distintos tipos de error
- Pruebas de funcionamiento en Bisección
- Pruebas de funcionamiento en Falsa Posición
- Pruebas de funcionamiento en Newton-Raphson
- Pruebas de funcionamiento en Punto Fijo
- Validación integral de compatibilidad entre las nuevas funciones y los métodos implementados

---

## v3.0.0 - 25-05-2026 - Gabriel Beltrán Amezcua - Th3PapaY0ch1S08

### Agregado
- Integración completa de gráficas dentro de la interfaz principal
- Implementación de visualización embebida de gráficos sin ventanas externas
- Incorporación de sistema gráfico dual para métodos numéricos avanzados
- Generación automática de segunda gráfica basada en el tipo de error seleccionado
- Compatibilidad del sistema dual de gráficas con:
  - Métodos de regresión e interpolación
  - Derivación numérica
  - Integración numérica
  - Métodos implementados posteriormente a Punto Fijo
- Conservación de comportamiento especializado para:
  - Método de Bisección
  - Método de Falsa Posición
  - Método de Newton-Raphson
  - Método de Punto Fijo
- Integración del tipo de error seleccionado dentro del flujo completo de visualización matemática
- Consolidación visual del entorno de trabajo dentro de una única interfaz

### Mejoras
- Optimización del selector "Tipo de Método" permitiendo escritura continua del nombre del método
- Mejora de experiencia de usuario durante búsqueda dinámica de métodos
- Reestructuración del sistema gráfico para soportar múltiples visualizaciones simultáneas
- Mejora de organización visual de resultados y análisis numérico
- Adaptación de métodos numéricos al nuevo sistema gráfico unificado
- Optimización interna de generación y actualización de gráficos
- Mejora del análisis de convergencia mediante visualización complementaria de errores
- Refactorización parcial del flujo de trabajo de la interfaz

### Correcciones
- Corrección del problema de escritura letra por letra dentro del selector de métodos
- Corrección del cálculo de Error Absoluto
- Corrección del cálculo de Error Relativo
- Corrección del cálculo de Error Porcentual
- Corrección de generación de gráficas asociadas al tipo de error seleccionado
- Ajuste de coherencia entre resultados numéricos obtenidos en interfaz y resultados validados mediante implementaciones independientes
- Corrección de inconsistencias entre cálculos iterativos y representación gráfica
- Corrección de sincronización entre datos obtenidos y visualización matemática
- Corrección de comportamiento interno del sistema de errores dinámicos

### Pruebas
- Validación de escritura dinámica del selector de métodos
- Comparación de resultados obtenidos contra implementaciones individuales independientes
- Validación de Error Absoluto
- Validación de Error Relativo
- Validación de Error Porcentual
- Verificación de concordancia entre resultados numéricos y representación gráfica
- Pruebas de generación de doble gráfica en métodos compatibles
- Pruebas de generación de gráfica única en:
  - Método de Bisección
  - Método de Falsa Posición
  - Método de Newton-Raphson
  - Método de Punto Fijo
- Verificación de estabilidad visual con gráficas integradas dentro de la interfaz
- Validación integral de compatibilidad entre interfaz, cálculos numéricos y sistema gráfico

---

## v3.1.0 - 28-05-2026 - Víctor Aguilar Ortiz - Victor4guilar

### Agregado
- Implementación del Método de Euler para la solución numérica de Ecuaciones Diferenciales Ordinarias (EDO)
- Creación de la nueva categoría "Ecuaciones Diferenciales Ordinarias" dentro del selector de métodos
- Integración del Método de Euler dentro de la arquitectura principal de la aplicación
- Entrada dinámica para la ecuación diferencial en la forma \(dy/dx = f(x,y)\)
- Inclusión de parámetros de entrada para valor inicial \(x_0\), condición inicial \(y_0\), valor final \(x_f\) y número de iteraciones \(n\)
- Cálculo automático del tamaño de paso \(h\)
- Generación iterativa de aproximaciones mediante el método de Euler
- Almacenamiento de los valores calculados de \(x\) y \(y\) durante cada iteración
- Compatibilidad con funciones algebraicas, trigonométricas, exponenciales y logarítmicas
- Integración completa con el motor matemático reutilizable existente

### Mejoras
- Expansión de la arquitectura modular para soportar métodos de resolución de ecuaciones diferenciales ordinarias
- Reestructuración del selector de métodos incorporando una nueva clasificación temática
- Adaptación del sistema dinámico de entradas para parámetros específicos de EDO
- Consolidación de la organización interna entre métodos de raíces, interpolación, derivación, integración y ecuaciones diferenciales
- Reutilización del sistema de evaluación matemática para el cálculo de pendientes \(f(x,y)\)
- Optimización del flujo de ejecución para soportar métodos de aproximación de soluciones numéricas
- Fortalecimiento de la escalabilidad de la aplicación para futuras implementaciones de métodos como Heun, Ralston y Runge-Kutta
- Integración del Método de Euler con el sistema general de resultados y visualización de la aplicación

### Pruebas
- Pruebas manuales con ecuaciones diferenciales de primer orden
- Validación de resultados utilizando ejemplos académicos conocidos
- Verificación del cálculo correcto del tamaño de paso \(h\)
- Comparación básica entre resultados numéricos y soluciones analíticas disponibles
- Validación del comportamiento utilizando diferentes cantidades de iteraciones
- Verificación de estabilidad para distintos valores iniciales
- Pruebas de compatibilidad con funciones algebraicas, trigonométricas y exponenciales
- Validación del funcionamiento dinámico de las entradas específicas para EDO
- Pruebas integrales de compatibilidad con los métodos previamente implementados
- Verificación del correcto funcionamiento del Método de Euler dentro de la Suite de Métodos Numéricos

---

## v3.2.0 - 30-05-2026 - Gabriel Beltrán Amezcua - Th3PapaY0ch1S08

### Agregado

* Implementación del Método de Runge-Kutta de Segundo Orden para la resolución numérica de Ecuaciones Diferenciales Ordinarias (EDO)
* Integración del Método de Runge-Kutta dentro de la categoría "Ecuaciones Diferenciales Ordinarias"
* Inclusión de las variantes:

  * Euler Modificado (Punto Medio)
  * Heun
  * Ralston
* Selección dinámica del tipo de Runge-Kutta mediante menú desplegable
* Entrada opcional para solución analítica (y(x))
* Comparación automática entre solución numérica y solución analítica
* Cálculo de aproximaciones utilizando coeficientes ponderados (k_1) y (k_2)
* Generación automática de nodos numéricos durante la integración
* Visualización gráfica de la solución aproximada obtenida mediante Runge-Kutta
* Visualización simultánea de la curva analítica cuando es proporcionada por el usuario
* Representación gráfica de los puntos analíticos correspondientes a cada iteración
* Cálculo automático del error utilizando el tipo de error seleccionado en la interfaz
* Generación de gráfica de evolución del error durante el proceso iterativo
* Compatibilidad con funciones algebraicas, trigonométricas, exponenciales y logarítmicas

### Mejoras

* Expansión del módulo de Ecuaciones Diferenciales Ordinarias incorporando métodos de mayor precisión que Euler
* Reutilización de la arquitectura matemática desarrollada para EDOs
* Optimización del sistema de evaluación de funciones para trabajar simultáneamente con soluciones numéricas y analíticas
* Adaptación de la interfaz para soportar múltiples variantes de Runge-Kutta desde un único módulo
* Mejora en la visualización de resultados mediante comparación gráfica directa entre aproximación y solución real
* Integración completa con el sistema de errores dinámicos de la aplicación
* Optimización de la generación de gráficas para mostrar simultáneamente comportamiento de la solución y evolución del error
* Consolidación de la arquitectura modular para futuras implementaciones de métodos de orden superior

### Pruebas

* Pruebas manuales utilizando las variantes Euler Modificado, Heun y Ralston
* Validación de resultados mediante comparación con soluciones analíticas conocidas
* Verificación del cálculo correcto de los coeficientes ponderados de Runge-Kutta
* Comparación de precisión entre Euler, Heun y Ralston
* Validación del cálculo de Error Absoluto
* Validación del cálculo de Error Relativo
* Validación del cálculo de Error Porcentual
* Verificación de generación correcta de gráficas numéricas y analíticas
* Pruebas de estabilidad utilizando diferentes tamaños de paso e iteraciones
* Validación de compatibilidad con el resto de métodos implementados en la Suite de Métodos Numéricos

---
