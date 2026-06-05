Titulo del proyecto: INTERFAZ PARA MÉTODOS NUMÉRICOS

Programa Educativo: Ingeniería en Intrumentación Electrónica

Experiencia Educativa: Programación Avanzada

Facilitador: José Alfonso Dominguez Chávez

Fecha: 04 de junio del 2026 

Semestre: 4to 

Descripción del proyecto: En este proyecto vamos a crear una interfaz en la cual se puedan resolver diferentes tipos de funciones como ecuaciones aritméticas, integrales y ecuaciones diferenciales; en la interfaz se encontrará un buscador para los métodos numéricos, así como un menú, el cual estará dividido en los tipos de funciones que se manejarán en la interfaz, y al seleccionar un tipo de función se desplegarán los tipos de métodos numéricos que estén integrados para ese tipo de función; asimismo, cuando se seleccione un método se abrirá una pestaña o formulario adaptativo en el cual ya se podrá utilizar el método, ingresando la función o arreglos de datos, los intervalos y el error permitido, obteniendo ahí mismo los resultados.

Estado del Proyecto: 

Versión actual: `v3. 2. 1`

Avances técnicos:

    -Estructura de la Interfaz: Se ha optimizado la ventana principal (`1200x800`) segmentada en paneles de configuración lateral y zonas de trabajo interactivas. Se incorporó con éxito un sistema de búsqueda predictiva por escritura con filtrado automático en tiempo real y la selección dinámica del tipo de error iterativo.
    
    -Análisis de Funciones y Datos: Se ha posibilitado la interpretación de expresiones matemáticas elaboradas (como seno, coseno, logaritmo, exponencial, entre otros) a partir de texto, así como el procesamiento secuencial de arreglos numéricos discretos separados por comas para los métodos de análisis de datos.
   
    -Métodos Incorporados:

      --Raíces de Ecuaciones: Bisección (con validación de cambio de signo), Falsa Posición, Búsqueda por Incrementos, Newton-Raphson, Secante y Punto Fijo.
      
      --Ajuste e Interpolación: Mínimos Cuadrados Lineales, Mínimos Cuadrados Polinomiales, Interpolación Lineal de Newton, Polinomios de Interpolación de Newton e Interpolación de Lagrange.

      --Cálculo Numérico y EDO:Diferencias Finitas, Método de Trapecios, Método de Integración de Simpson (simple y múltiple / compuesta), Método de Euler y Método de Runge-Kutta (4to Orden). 

      --Gráficas: Se realiza la generación automática de gráficos interactivos utilizando la biblioteca Matplotlib insertada de forma nativa dentro de los paneles de la interfaz, mostrando de manera integrada las curvas de caída del error elegido, el comportamiento de las funciones, los intervalos de raíces detectadas, o el trazado de rectas y curvas de ajuste junto a sus puntos muestreados. 
