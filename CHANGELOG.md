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

