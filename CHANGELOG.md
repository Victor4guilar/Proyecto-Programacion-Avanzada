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
