# INTERFAZ PARA MÉTODOS NUMÉRICOS

## Descripción del Proyecto

El presente proyecto consiste en el desarrollo de una **interfaz gráfica en Python** que permita al usuario explorar y aplicar distintos **métodos numéricos** para la resolución de problemas matemáticos.

Al iniciar la aplicación, se mostrará una ventana principal con el título **“Métodos Numéricos”**, acompañada de un buscador y un menú de navegación. En este menú el usuario podrá seleccionar entre tres categorías principales de métodos:

* Métodos para resolver ecuaciones algebraicas
* Métodos de integración numérica
* Métodos para ecuaciones diferenciales

Al seleccionar una de estas categorías, se desplegará una lista de los métodos numéricos disponibles para ese tipo de problema. Una vez elegido el método, el sistema abrirá una nueva ventana donde el usuario podrá ingresar los datos necesarios para realizar el cálculo, tales como:

* la función matemática
* el intervalo de análisis
* el error aproximado permitido

Finalmente, el sistema ejecutará el algoritmo correspondiente, mostrará el **resultado obtenido** y presentará **gráficas del comportamiento del error durante las iteraciones**.

Este proyecto tiene como objetivo facilitar el **aprendizaje y visualización de los métodos numéricos** mediante una herramienta interactiva.

---

# Objetivo General

Desarrollar una **interfaz interactiva en Python** que permita aplicar distintos métodos numéricos para la resolución de funciones matemáticas, facilitando su uso y comprensión mediante una interacción sencilla y una visualización clara de los resultados.

---

# Objetivos Específicos

* Implementar distintos **métodos numéricos** como Bisección y Falsa Posición.
* Diseñar una **interfaz gráfica amigable** que permita seleccionar los métodos disponibles.
* Integrar un **buscador de métodos numéricos** dentro de la interfaz.
* Permitir al usuario ingresar **funciones, intervalos y errores aproximados**.
* Mostrar los **resultados del cálculo** obtenido mediante el método seleccionado.
* Generar **gráficas del error de aproximación** para analizar el comportamiento del método.

---

# MVP (Producto Mínimo Viable)

El MVP del proyecto consistirá en una aplicación funcional que incluya:

* Interfaz gráfica básica.
* Implementación de al menos **dos métodos numéricos**:

  * Método de Bisección
  * Método de Falsa Posición
* Entrada de datos por parte del usuario:

  * función
  * intervalo
  * error aproximado
* Cálculo de la solución mediante el método seleccionado.
* Visualización del **resultado y gráfica del error**.

---

# Diagrama de Bloques del Sistema

```
Usuario
   │
   ▼
Interfaz Gráfica
   │
   ▼
Selección de Tipo de Método
(Ecuaciones | Integrales | Ecuaciones Diferenciales)
   │
   ▼
Selección de Método Numérico
(Bisección, Falsa Posición, etc.)
   │
   ▼
Ingreso de Datos
(Función, intervalo, error)
   │
   ▼
Algoritmo Numérico
   │
   ▼
Resultados y Gráficas
```

---

# Componentes de Hardware

* Computadora personal
* Procesador compatible con Python
* Monitor
* Teclado
* Mouse

---

# Componentes de Software

* Python
* Spyder
* GitHub
* GitHub Desktop
* Visual Studio Code

---

## Roles del Equipo

| Integrante                    | Rol                      | Responsabilidad                     |
|-------------------------------|--------------------------|-------------------------------------|
| Aguilar Ortiz Víctor          | Desarrollo de algoritmos | Implementación de métodos numéricos |
| Beltrán Amezcua Gabriel       | Interfaz gráfica         | Diseño de la GUI                    |
| Ronzón Pérez Axel de Jesús    | Integración y pruebas    | Validación del funcionamiento       |
| Sánchez Pérez Jonathan        | Documentación            | Redacción de README y PROJECT       |

---

## Cronograma del Proyecto

| Semana   | Actividad                                                   | Fecha importante |
|----------|-------------------------------------------------------------|------------------|
| Semana 1 | Planeación del proyecto, definición de objetivos y creación del repositorio | |
| Semana 2 | Organización del repositorio y estructura del proyecto | |
| Semana 3 | Diseño inicial de la interfaz y planteamiento de los algoritmos | |
| Semana 4 | Implementación del primer método numérico (Bisección) | |
| Semana 5 | Integración del método en la interfaz | **17 de abril — Primera entrega de avances** |
| Semana 6 | Implementación del método de Falsa Posición | |
| Semana 7 | Pruebas y corrección de errores en los métodos implementados | |
| Semana 8 | Mejora de la interfaz gráfica y funcionalidad del programa | **15 de mayo — Segunda entrega de avances** |
| Semana 9 | Implementación de gráficas de resultados y error | |
| Semana 10 | Integración completa del sistema | |
| Semana 11 | Pruebas generales del programa | |
| Semana 12 | Corrección de errores y optimización del código | |
| Semana 13 | Preparación de documentación y ajustes finales | |
| Semana 14 | Revisión final del proyecto | |
| Semana 15 | Entrega final del proyecto | **31 de julio — Entrega final** |
