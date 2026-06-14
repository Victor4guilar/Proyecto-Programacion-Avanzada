#  Uso para la Interfaz de Métodos Numéricos v3.3.0

En este archivo se daran varios ejemplos de ejercicios para todos los metodos de la interfaz. 

## Método de Bisección

**Función f(x):** `8*(x**2)-2*x-3`

**Valor a:** `0`

**Valor b:** `10`

**Tolerancia (Error):** `0.0001`

**Resultado esperado:**

![alt text](image.png)

---

## Método de Falsa Posición

**Función f(x):** `e**(-x)-x`

**Valor a:** `0`

**Valor b:** `1`

**Tolerancia (Error):** `0.0001`

**Resultado esperado:**

![alt text](image-1.png)

---

## Método de Búsqueda por Incrementos

**Función f(x):** `0.95*(x**3)-5.9*(x**2)+10.9*x-6`

**X inicial:** `0.5`

**X final:** `4`

**Incremento:** `0.2`

**Resultado esperado:**

![alt text](image-2.png)

---

## Método de Newton-Raphson

**Función f(x):** `exp(-x**2)-x`

**Derivada de la Función f'(x):** `-2*x*exp(-x**2)-1`

**X inicial:** `0`

**Tolerancia (Error):** `0.0001`

**Resultado esperado:**

![alt text](image-3.png)

---

## Método de la Secante

**Función f(x):** `exp(-x**2)-x`

**X inicial:** `0`

**Segunda X inicial:** `1`

**Tolerancia (Error):** `0.0001`

**Resultado esperado:**

![alt text](image-4.png)

---

## Método de Punto Fijo

**Función f(x):** `2*exp(x**2)/5`

**X inicial:** `0`

**Tolerancia (Error):** `0.0001`

**Resultado esperado:**

![alt text](image-5.png)

---

## Método de Mínimos Cuadrados Lineales

**Valores X:** `7, 1, 10, 5, 4, 3, 13, 10, 2`

**Valores Y:** `2, 9, 2, 5, 7, 11, 2, 5, 14`

**Resultado esperado:**

![alt text](image-6.png)

---

## Método de Mínimos Cuadrados Polinomiales

**Valores X:** `30, 50, 60, 80, 100, 110`

**Valores Y:** `16, 28, 40, 63, 90, 120`

**Grado:** `2`

**Resultado esperado:**

![alt text](image-7.png)

---

## Método de Interpolación Lineal de Newton

**Valores X:** `1, 1.5, 2, 2.5, 3, 3.5`

**Valores f(x):** `0, 0.4054, 0.6931, 0.9162, 1.0986, 1.2527`

**Incremento:** `0.5`

**Resultado esperado:**

![alt text](image-8.png)

---

## Método de Polinomios de Interpolación de Newton

**Valores X:** `1, 2, 3, 4, 5, 6`

**Valores Y:** `1, 3, 6, 8, 9, 4`

**X a interpolar:** `2.5`

**Resultado esperado:**

![alt text](image-9.png)

La gráfica del error no marcara nada, ya que los calculos para calcular cualquier tipo de error sera muy cercano a 0 (apoximadamente 0.00000001), provocando que no se note nada en la gráfica del error.

---

## Método de Interpolación de Lagrange

**Valores X:** `0, 1, 2`

**Valores Y:** `1, 3, 0`

**Valor de X a interpolar:** `0.25`

**Resultado esperado:**

![alt text](image-10.png)

En el método de interpolación de la lagrange no usa error (normalmente), pero aún así la interfaz se encarga de calcular algun tipo de error, oviamente sin mostrar nada en la gráfica.

---

## Método de Diferencias Finitas

**Función de f(x):** `x**3-x`

**Valor X:** `1`

**Tamaño del paso (h):** `0.1`

**Resultado esperado:**

![alt text](image-11.png)

---

## Método del Trapecio

**Función de f(x):** `x**3/sqrt(1+x)`

**Límite inferior (a):** `1`

**Límite superior (b):** `2`

**Número de trapecios (n):** `8`

**Resultado esperado:**

![alt text](image-12.png)

---

## Método de Integración de Simpson

**Función de f(x):** `sqrt(5+x**3)`

**Límite inferior (a):** `0`

**Límite superior (b):** `1`

**Número de trapecios (n):** `4`

**Resultado esperado:**

### Simpson 1/3 simple

![alt text](image-13.png)

### Simpson 1/3 múltiple

![alt text](image-14.png)

### Simpson 3/8 simple

![alt text](image-15.png)

### Simpson 3/8 compuesta

**Función de f(x):** `sqrt(1+x**5)`

**Límite inferior (a):** `1`

**Límite superior (b):** `4`

**Número de trapecios (n):** `6`

![alt text](image-16.png)

---

## Método de Euler

**Ecuación diferencial dy/dx:** `y-x`

**Solución Analítica y(x):** `x+1-0.5*exp(x)`

**Valor inicial x0:** `0`

**Valor inicial y0:** `0.5`

**Valor final xf** `1`

**Iteraciones (h):** `10`

**Resultado esperado:**

![alt text](image-17.png)

---

## Método de Runge-Kutta

**Ecuación diferencial (dy/dx):** `(y+3)*(x-4)`

**Solución Analítica y(x):** `7*exp((x**2)/2-4*x+7/2)-3`

**Valor inicial x0:** `1`

**Valor inicial y0:** `4`

**Valor final xf** `1.6`

**Iteraciones (h):** `10`

**Resultado esperado:**

### Euler Modificado

![alt text](image-18.png)

### Heun

![alt text](image-19.png)

### Raltson

![alt text](image-20.png)

---