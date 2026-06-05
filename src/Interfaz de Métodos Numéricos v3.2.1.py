#---IMPORTACIONES---
import tkinter as tk
from tkinter import ttk, messagebox
import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#---CLASE PRINCIPAL---
class MetodosNumericosApp:
    
    VERSION = "v3.2.1"
    
    def __init__(
        self,
        root
    ):
        """
        Inicialización de la aplicación principal de Métodos Numéricos.
        Configura la ventana, el título y los métodos base disponibles.
        """
        
        self.root = root
        
        self.root.title(
            f"Suite de Métodos Numéricos {self.VERSION}"
        )
        
        self.root.geometry(
            "1200x800"
        )
        
        self.lista_metodos_original = [
            "Bisección",
            "Falsa Posición",
            "Búsqueda por Incrementos",
            "Newton Raphson",
            "Secante",
            "Punto Fijo",
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            "Diferencias Finitas",
            "Método de Trapecios",
            "Método de Integración de Simpson",
            "Método de Euler",
            "Método de Runge-Kutta"
        ]
        
        self.crear_layout()
        
        self.crear_statusbar()

    #---INTERFAZ---
    def crear_layout(
        self
    ):
        """
        Crea y posiciona todos los elementos visuales de la aplicación,
        incluyendo los paneles de configuración, entradas, resultados
        y el área dedicada a las gráficas de matplotlib.
        """
        self.main_frame = ttk.Frame(
            self.root
        )
        
        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        
        # Panel izquierdo
        self.panel_control = ttk.LabelFrame(
            self.main_frame,
            text="Configuración"
        )
        
        self.panel_control.pack(
            side="left",
            fill="y",
            padx=5,
            pady=5
        )
        
        ttk.Label(
            self.panel_control,
            text="Método:"
        ).pack(
            pady=5
        )
        
        self.metodo_var = tk.StringVar()
        
        self.combo_metodos = ttk.Combobox(
            self.panel_control,
            textvariable=self.metodo_var,
            state="normal",
            width=35
        )

        #---MÉTODOS DISPONIBLES---
        self.opciones_completas = [
        
            "───── Raíces Cerradas ─────",
            "Bisección",
            "Falsa Posición",
            "Búsqueda por Incrementos",
        
            "───── Raíces Abiertas ─────",
            "Newton Raphson",
            "Secante",
            "Punto Fijo",
        
            "───── Regresión e Interpolación ─────",
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
        
            "───── Derivación Numérica ─────",
            "Diferencias Finitas",
        
            "───── Integración Numérica ─────",
            "Método de Trapecios",
            "Método de Integración de Simpson",
            
            "─── Ec. Diferenciales Ordinarias ───",
            "Método de Euler",
            "Método de Runge-Kutta"

        ]
        
        self.combo_metodos['values'] = self.opciones_completas
        
        self.combo_metodos.pack(
            pady=5
        )
        
        self.combo_metodos.bind(
            "<<ComboboxSelected>>",
            self.validar_metodo
        )
        
        self.combo_metodos.bind(
            "<KeyRelease>",
            self.filtrar_metodos
        )
        
        ttk.Label(
            self.panel_control,
            text="Tipo de Error:"
        ).pack(
            pady=5
        )
        
        self.tipo_error_var = tk.StringVar(
            value="Relativo"
        )
        
        self.combo_error = ttk.Combobox(
            self.panel_control,
            textvariable=self.tipo_error_var,
            state="readonly",
            values=[
                "Absoluto", 
                "Relativo", 
                "Porcentual"
            ],
            width=35
        )
        
        self.combo_error.pack(
            pady=5
        )
        
        ttk.Button(
            self.panel_control,
            text="Cargar Método",
            command=self.cargar_metodo
        ).pack(
            pady=10
        )
        
        ttk.Button(
            self.panel_control,
            text="Ejecutar",
            command=self.ejecutar_metodo
        ).pack(
            pady=5
        )

        # Panel derecho
        self.panel_trabajo = ttk.Frame(
            self.main_frame
        )
        
        self.panel_trabajo.pack(
            side="right",
            fill="both",
            expand=True
        )
        
        self.frame_inputs = ttk.LabelFrame(
            self.panel_trabajo,
            text="Entradas"
        )
        
        self.frame_inputs.pack(
            fill="x",
            padx=5,
            pady=5
        )
        
        self.frame_resultados = ttk.LabelFrame(
            self.panel_trabajo,
            text="Resultados"
        )
        
        self.frame_resultados.pack(
            fill="x",
            padx=5,
            pady=5
        )
        
        self.text_resultados = tk.Text(
            self.frame_resultados,
            height=8
        )
        
        self.text_resultados.pack(
            fill="both",
            expand=True
        )
        
        self.frame_graficas = ttk.LabelFrame(
            self.panel_trabajo,
            text="Gráficas"
        )
        
        self.frame_graficas.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

    #---STATUSBAR---
    def crear_statusbar(
        self
    ):
        """
        Barra de estado inferior para mostrar mensajes informativos 
        al usuario sobre la carga y ejecución de los métodos.
        """
        self.status = tk.StringVar(
            value="Listo"
        )
        
        ttk.Label(
            self.root,
            textvariable=self.status,
            relief="sunken"
        ).pack(
            fill="x",
            side="bottom"
        )

    #---FILTRAR MÉTODOS AL ESCRIBIR---
    def filtrar_metodos(
        self,
        event
    ):
        
        teclas_ignoradas = [
            'Up', 
            'Down', 
            'Left', 
            'Right', 
            'Return', 
            'Tab', 
            'Shift_L', 
            'Shift_R',
            'Control_L',
            'Control_R',
            'Alt_L',
            'Alt_R'
        ]
        
        if event.keysym in teclas_ignoradas:
            return
            
        texto_busqueda = self.metodo_var.get().lower()
        
        posicion_cursor = self.combo_metodos.index(tk.INSERT)
        
        if texto_busqueda == "":
            self.combo_metodos['values'] = self.opciones_completas
        else:
            filtrados = [
                m for m in self.opciones_completas 
                if texto_busqueda in m.lower() or "──" in m
            ]
            self.combo_metodos['values'] = filtrados
            
        self.combo_metodos.icursor(posicion_cursor)

    #---VALIDAR MÉTODO---
    def validar_metodo(
        self,
        event=None
    ):
        
        metodo = self.metodo_var.get()
        
        if "────" in metodo:
            self.combo_metodos.set(
                ""
            )
            
            self.status.set(
                "Seleccione un método válido"
            )

    #---EVALUAR FUNCIONES---
    def evaluar_funcion(
        self,
        expr,
        x
    ):
        """
        Evalúa una expresión matemática en formato string de manera segura
        y le pasa los valores de X y las funciones trigonométricas/logarítmicas.
        """
        try:
            permitido = {
                "x": x,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,
                "exp": math.exp,
                "sqrt": math.sqrt,
                "pi": math.pi,
                "e": math.e
            }
            
            return eval(
                expr,
                {"__builtins__": {}},
                permitido
            )
            
        except Exception as e:
            raise ValueError(
                f"Error en la expresión: {e}"
            )

    #---CALCULAR ERROR---
    def calcular_error(
        self,
        actual,
        anterior,
        tipo
    ):
        """
        Calcula el tipo de error seleccionado por el usuario en la interfaz.
        """
        if tipo == "Absoluto":
            return abs(
                actual - anterior
            )

        elif tipo == "Relativo":
            if actual != 0:
                return abs(
                    (
                        actual - anterior
                    ) / actual
                )
            return 0

        elif tipo == "Porcentual":
            if actual != 0:
                return abs(
                    (
                        actual - anterior
                    ) / actual
                ) * 100
            return 0

        return abs(
            actual - anterior
        )

    #---BISECCIÓN---
    def metodo_biseccion(
        self,
        expr,
        a,
        b,
        erra,
        tipo_error
    ):
        """
        MÉTODO DE BISECCIÓN:
        Es un método cerrado que divide a la mitad un intervalo [a, b] 
        donde se garantiza un cambio de signo en f(x), es decir, f(a)*f(b) < 0.
        Se evalúa la función en el punto medio (pi) y se redefine el intervalo
        basado en la ubicación de la raíz.
        """
        ejex = []
        ejey = []
        n = 0
        pi_anterior = a
        error = 100 
        
        fa = self.evaluar_funcion(
            expr,
            a
        )
        fb = self.evaluar_funcion(
            expr,
            b
        )
        
        if fa * fb > 0:
            raise ValueError(
                "La función debe tener signos opuestos en a y b."
            )
        
        while n < 500:
            pi = (
                a + b
            ) / 2
            
            if n > 0:
                error = self.calcular_error(
                    pi, 
                    pi_anterior, 
                    tipo_error
                )
            else:
                if tipo_error == "Absoluto":
                    error = abs(b - a)
                else:
                    error = 100
            
            ejex.append(
                n + 1
            )
            
            ejey.append(
                error
            )
            
            if error < erra and n > 0:
                break
            
            fpi = self.evaluar_funcion(
                expr,
                pi
            )
            
            if fa * fpi < 0:
                b = pi
            elif fa * fpi > 0:
                a = pi
                fa = fpi
            else:
                break
                
            pi_anterior = pi
            n += 1
            
        return pi, error, ejex, ejey

    #---FALSA POSICIÓN---
    def metodo_falsa_posicion(
        self,
        expr,
        a,
        b,
        erra,
        tipo_error
    ):
        """
        MÉTODO DE LA FALSA POSICIÓN:
        Al igual que bisección, es un método cerrado que requiere [a, b] con
        cambio de signo. A diferencia de bisección, usa una recta secante 
        entre los dos puntos de los extremos para encontrar la nueva aproximación.
        """
        ejex = []
        ejey = []
        iteracion = 0
        xr_anterior = a
        error = 100
        
        fa_inicial = self.evaluar_funcion(expr, a)
        fb_inicial = self.evaluar_funcion(expr, b)
        
        if fa_inicial * fb_inicial > 0:
            raise ValueError("La función debe tener signos opuestos en a y b.")
        
        while iteracion < 500:
            fa = self.evaluar_funcion(
                expr,
                a
            )
            fb = self.evaluar_funcion(
                expr,
                b
            )
            
            if (fb - fa) == 0:
                break
                
            xr = a - (
                fa * (
                    b - a
                )
            ) / (
                fb - fa
            )
            
            fxr = self.evaluar_funcion(
                expr,
                xr
            )
            
            if iteracion > 0:
                error = self.calcular_error(
                    xr, 
                    xr_anterior, 
                    tipo_error
                )
            else:
                if tipo_error == "Absoluto":
                    error = abs(b - a)
                else:
                    error = 100
            
            ejex.append(
                iteracion + 1
            )
            
            ejey.append(
                error
            )
            
            if error < erra and iteracion > 0:
                break
                
            if fa * fxr < 0:
                b = xr
            elif fa * fxr > 0:
                a = xr
            else:
                break
                
            xr_anterior = xr
            iteracion += 1
            
        return xr, error, ejex, ejey

    #---NEWTON RAPHSON---
    def metodo_newton_raphson(
        self,
        fun,
        fprima,
        Xi,
        erra,
        tipo_error
    ):
        """
        MÉTODO DE NEWTON RAPHSON:
        Es un método abierto que requiere un solo punto inicial (Xi).
        Utiliza la derivada de la función para trazar la recta tangente 
        y ubicar su intersección con el eje X como la nueva aproximación a la raíz.
        """
        ejex = []
        ejey = []
        error = 100
        n = 0
        
        while n < 500:
            fxi = self.evaluar_funcion(
                fun,
                Xi
            )
            fpxi = self.evaluar_funcion(
                fprima,
                Xi
            )
            
            if fpxi == 0:
                break
                
            Xn = Xi - (
                fxi / fpxi
            )
            
            if n > 0:
                error = self.calcular_error(
                    Xn, 
                    Xi, 
                    tipo_error
                )
            else:
                if tipo_error == "Absoluto":
                    error = abs(Xn - Xi)
                else:
                    error = 100
            
            ejex.append(
                n + 1
            )
            
            ejey.append(
                error
            )
            
            if error < erra and n > 0:
                Xi = Xn
                break
            
            Xi = Xn
            n += 1
            
        return Xi, error, ejex, ejey

    #---SECANTE---
    def metodo_secante(
        self,
        expr,
        x0,
        x1,
        erra,
        tipo_error
    ):
        """
        MÉTODO DE LA SECANTE:
        Aproxima el método de Newton sustituyendo la evaluación analítica 
        de la derivada por una aproximación en diferencias finitas usando 
        dos valores iniciales x0 y x1.
        """
        ejex = []
        ejey = []
        error = 100
        n = 0
        
        while n < 100:
            fx0 = self.evaluar_funcion(
                expr,
                x0
            )
            fx1 = self.evaluar_funcion(
                expr,
                x1
            )
            
            if (fx1 - fx0) == 0:
                break
                
            x2 = x1 - (
                fx1 * (
                    x1 - x0
                )
            ) / (
                fx1 - fx0
            )
            
            if n > 0:
                error = self.calcular_error(
                    x2, 
                    x1, 
                    tipo_error
                )
            else:
                if tipo_error == "Absoluto":
                    error = abs(x2 - x1)
                else:
                    error = 100
                    
            ejex.append(
                n + 1
            )
            
            ejey.append(
                error
            )
            
            if error < erra and n > 0:
                x1 = x2
                break
            
            x0 = x1
            x1 = x2
            n += 1
            
        return x1, error, ejex, ejey

    #---PUNTO FIJO---
    def metodo_punto_fijo(
        self,
        gx,
        x0,
        erra,
        tipo_error
    ):
        """
        MÉTODO DE ITERACIÓN DEL PUNTO FIJO:
        Método abierto en el que se reorganiza la función f(x)=0 
        de la forma x = g(x). A partir de x0, se calcula recursivamente 
        x_{i+1} = g(x_i) hasta alcanzar la tolerancia.
        """
        ejex = []
        ejey = []
        error = 100
        n = 0
        
        while n < 100:
            x1 = self.evaluar_funcion(
                gx,
                x0
            )
            
            if n > 0:
                error = self.calcular_error(
                    x1, 
                    x0, 
                    tipo_error
                )
            else:
                if tipo_error == "Absoluto":
                    error = abs(x1 - x0)
                else:
                    error = 100
                    
            ejex.append(
                n + 1
            )
            
            ejey.append(
                error
            )
            
            if error < erra and n > 0:
                break
            
            x0 = x1
            n += 1
            
        return x1, error, ejex, ejey

    #---BÚSQUEDA POR INCREMENTOS---
    def metodo_busqueda_incrementos(
        self,
        expr,
        xi,
        xf,
        incremento
    ):
        """
        MÉTODO DE BÚSQUEDA POR INCREMENTOS:
        Avanza a lo largo del dominio evaluando saltos pequeños en X. 
        Si se detecta un cambio de signo entre un paso y el siguiente, 
        se registra un intervalo en el que yace una raíz.
        """
        ejex = []
        ejey = []
        x = xi
        intervalos = []
        
        while x <= xf:
            fx = self.evaluar_funcion(
                expr,
                x
            )
            
            x_sig = x + incremento
            
            fx_sig = self.evaluar_funcion(
                expr,
                x_sig
            )
            
            ejex.append(
                x
            )
            ejey.append(
                fx
            )
            
            if fx * fx_sig < 0:
                intervalos.append(
                    (
                        x, 
                        x_sig
                    )
                )
                
            x = x_sig
            
        return intervalos, ejex, ejey

    #---MÍNIMOS CUADRADOS LINEALES---
    def metodo_minimos_cuadrados(
        self,
        arreglo_x,
        arreglo_y
    ):
        """
        REGRESIÓN POR MÍNIMOS CUADRADOS LINEALES:
        Encuentra la mejor recta (y = a*x + b) que se ajuste a un conjunto de puntos,
        minimizando la suma de los errores cuadrados entre los datos y la línea calculada.
        """
        suma_X = sum(
            arreglo_x
        )
        
        suma_Y = sum(
            arreglo_y
        )
        
        suma_XY = sum(
            arreglo_x[i] * arreglo_y[i]
            for i in range(
                len(
                    arreglo_x
                )
            )
        )
        
        suma_X2 = sum(
            arreglo_x[i] ** 2
            for i in range(
                len(
                    arreglo_x
                )
            )
        )
        
        n = len(
            arreglo_x
        )
        
        a = (
            (
                n * suma_XY
            )
            - (
                suma_X * suma_Y
            )
        ) / (
            (
                n * suma_X2
            )
            - (
                suma_X ** 2
            )
        )
        
        b = (
            (
                suma_X * suma_XY
            )
            - (
                suma_Y * suma_X2
            )
        ) / (
            (
                suma_X ** 2
            )
            - (
                n * suma_X2
            )
        )
        
        eje_y_calc = []
        for i in range(
            len(
                arreglo_x
            )
        ):
            funcion = (
                (
                    a * arreglo_x[i]
                ) + b
            )
            eje_y_calc.append(
                funcion
            )
            
        return a, b, eje_y_calc

    #---MÍNIMOS CUADRADOS POLINOMIALES---
    def metodo_minimos_cuadrados_polinomiales(
        self,
        arreglo_x,
        arreglo_y,
        grado
    ):
        """
        REGRESIÓN POR MÍNIMOS CUADRADOS POLINOMIALES:
        Ajusta una curva polinomial de cualquier grado deseado a los puntos de datos 
        discretos dados, de modo que la suma de residuos al cuadrado sea mínima.
        """
        coeficientes = np.polyfit(
            arreglo_x,
            arreglo_y,
            grado
        )
        
        polinomio = np.poly1d(
            coeficientes
        )
        
        eje_y_calc = polinomio(
            arreglo_x
        )
        
        return coeficientes, eje_y_calc, polinomio

    #---INTERPOLACIÓN LINEAL DE NEWTON---
    def metodo_interpolacion_newton(
        self,
        x0,
        y0,
        x1,
        y1,
        x_interp
    ):
        """
        INTERPOLACIÓN LINEAL DE NEWTON:
        Conecta dos puntos de datos (x0, y0) y (x1, y1) con una línea recta
        para estimar valores de y intermedios.
        """
        b0 = y0
        
        b1 = (
            y1 - y0
        ) / (
            x1 - x0
        )
        
        resultado = b0 + (
            b1 * (
                x_interp - x0
            )
        )
        
        return resultado, b1

    #---POLINOMIOS DE INTERPOLACIÓN DE NEWTON---
    def metodo_polinomios_newton(
        self,
        arreglo_x,
        arreglo_y,
        x_interp
    ):
        """
        POLINOMIOS DE INTERPOLACIÓN DE NEWTON (Diferencias Divididas):
        Construye un polinomio que pasa exactamente por los puntos dados,
        generando una matriz de diferencias divididas para extraer los coeficientes.
        """
        n = len(
            arreglo_x
        )
        
        tabla = [
            [
                0 for j in range(
                    n
                )
            ]
            for i in range(
                n
            )
        ]
        
        for i in range(
            n
        ):
            tabla[i][0] = arreglo_y[i]
            
        for j in range(
            1, 
            n
        ):
            for i in range(
                n - j
            ):
                tabla[i][j] = (
                    tabla[i + 1][j - 1]
                    - tabla[i][j - 1]
                ) / (
                    arreglo_x[i + j]
                    - arreglo_x[i]
                )
                
        coeficientes = [
            tabla[0][i]
            for i in range(
                n
            )
        ]
        
        resultado = coeficientes[0]
        producto = 1
        
        for i in range(
            1, 
            n
        ):
            producto *= (
                x_interp
                - arreglo_x[i - 1]
            )
            
            resultado += (
                coeficientes[i]
                * producto
            )
            
        return resultado, coeficientes, tabla

    #---INTERPOLACIÓN DE LAGRANGE---
    def metodo_lagrange(
        self,
        arreglo_x,
        arreglo_y,
        valor
    ):
        """
        INTERPOLACIÓN DE LAGRANGE:
        Técnica alternativa para generar un polinomio de interpolación
        sin usar diferencias divididas, útil para datos no uniformes.
        """
        n = len(
            arreglo_x
        )
        resultado = 0

        for i in range(
            n
        ):
            L = 1
            for j in range(
                n
            ):
                if i != j:
                    if arreglo_x[i] == arreglo_x[j]:
                        raise ValueError(
                            "No puede haber valores X repetidos"
                        )
                        
                    L = L * (
                        (
                            valor - arreglo_x[j]
                        )
                        / (
                            arreglo_x[i] - arreglo_x[j]
                        )
                    )

            resultado = resultado + (
                arreglo_y[i] * L
            )

        return resultado

    #---DIFERENCIAS FINITAS (DERIVACIÓN NUMÉRICA)---
    def metodo_diferencias_finitas(
        self,
        expr,
        x,
        h
    ):
        """
        DERIVACIÓN POR DIFERENCIAS FINITAS:
        Estima la primera y segunda derivada evaluando la función
        en valores ligeramente desplazados (+h, -h) desde el punto X de interés.
        """
        fx = self.evaluar_funcion(
            expr,
            x
        )
        
        fx_mas_h = self.evaluar_funcion(
            expr,
            x + h
        )
        
        fx_menos_h = self.evaluar_funcion(
            expr,
            x - h
        )
        
        fx_mas_2h = self.evaluar_funcion(
            expr,
            x + (
                2 * h
            )
        )
        
        fx_menos_2h = self.evaluar_funcion(
            expr,
            x - (
                2 * h
            )
        )

        d1_adelante = (
            fx_mas_h - fx
        ) / h
        
        d1_atras = (
            fx - fx_menos_h
        ) / h
        
        d1_central = (
            fx_mas_h - fx_menos_h
        ) / (
            2 * h
        )

        d2_adelante = (
            fx_mas_2h 
            - (
                2 * fx_mas_h
            ) 
            + fx
        ) / (
            h ** 2
        )
        
        d2_atras = (
            fx 
            - (
                2 * fx_menos_h
            ) 
            + fx_menos_2h
        ) / (
            h ** 2
        )
        
        d2_central = (
            fx_mas_h 
            - (
                2 * fx
            ) 
            + fx_menos_h
        ) / (
            h ** 2
        )

        return (
            d1_adelante,
            d1_atras,
            d1_central,
            d2_adelante,
            d2_atras,
            d2_central
        )

    #---MÉTODO DE TRAPECIOS---
    def metodo_trapecios(
        self,
        expr,
        a,
        b,
        n
    ):
        """
        MÉTODO DE INTEGRACIÓN NUMÉRICA DE TRAPECIOS:
        Aproxima el área bajo la curva calculando el área de varios trapecios
        debidamente formados al subdividir el dominio de [a, b] en 'n' intervalos.
        """
        h = (
            b - a
        ) / n

        suma = 0
        x_vals = []
        y_vals = []

        for i in range(
            n + 1
        ):
            x = a + (
                i * h
            )
            
            fx = self.evaluar_funcion(
                expr, 
                x
            )

            x_vals.append(
                x
            )
            y_vals.append(
                fx
            )

            if i == 0 or i == n:
                suma += fx
            else:
                suma += 2 * fx

        integral = (
            h / 2
        ) * suma

        return integral, x_vals, y_vals

    #---INTEGRACIÓN DE SIMPSON---
    def metodo_simpson(
        self,
        expr,
        a,
        b,
        tipo,
        n
    ):
        """
        MÉTODOS DE INTEGRACIÓN DE SIMPSON:
        Técnicas avanzadas que utilizan polinomios de 2do (Regla de 1/3) 
        y 3er grado (Regla de 3/8) para aproximar la integración numérica 
        mucho mejor que el método de trapecios.
        """
        x_real = np.linspace(
            a,
            b,
            5000
        )
    
        y_real = [
            self.evaluar_funcion(
                expr,
                x
            )
            for x in x_real
        ]
    
        integral_real = np.trapezoid(
            y_real,
            x_real
        )
    
        
    
        if tipo == "1/3 Simple":
    
            h = (
                b - a
            ) / 2
    
            integral = (
                h / 3
            ) * (
                self.evaluar_funcion(expr, a)
                + 4 * self.evaluar_funcion(expr, a + h)
                + self.evaluar_funcion(expr, b)
            )
    
        elif tipo == "1/3 Múltiple":
    
            if n % 2 != 0:
                raise ValueError(
                    "n debe ser par"
                )
    
            h = (
                b - a
            ) / n
    
            suma = 0
    
            for i in range(
                1, 
                n
            ):
                fx = self.evaluar_funcion(
                    expr,
                    a + i * h
                )
                if i % 2:
                    suma += 4 * fx
                else:
                    suma += 2 * fx
                    
            integral = (
                h / 3
            ) * (
                self.evaluar_funcion(expr, a)
                + suma
                + self.evaluar_funcion(expr, b)
            )
    
        elif tipo == "3/8 Simple":
    
            h = (
                b - a
            ) / 3
    
            integral = (
                3 * h / 8
            ) * (
                self.evaluar_funcion(expr, a)
                + 3 * self.evaluar_funcion(expr, a + h)
                + 3 * self.evaluar_funcion(expr, a + 2 * h)
                + self.evaluar_funcion(expr, b)
            )
    
        elif tipo == "3/8 Compuesta":
    
            if n % 3 != 0:
                raise ValueError(
                    "n múltiplo de 3"
                )
    
            h = (
                b - a
            ) / n
    
            suma = 0
    
            for i in range(
                1, 
                n
            ):
                fx = self.evaluar_funcion(
                    expr,
                    a + i * h
                )
                if i % 3 == 0:
                    suma += 2 * fx
                else:
                    suma += 3 * fx
                    
            integral = (
                3 * h / 8
            ) * (
                self.evaluar_funcion(expr, a)
                + suma
                + self.evaluar_funcion(expr, b)
            )
    
        return integral, integral_real
    
    #---MÉTODO DE EULER---
    def metodo_euler(
        self,
        expr,
        x0,
        y0,
        xf,
        n
    ):
        """
        MÉTODO DE EULER (Primer Orden):
        Técnica base para resolver ecuaciones diferenciales ordinarias (EDO) 
        dada una condición inicial. Estima la solución avanzando pequeños
        pasos asumiendo comportamiento lineal local dictado por la derivada.
        """
        ejex = []
        ejey = []

        h = (
            xf - x0
        ) / n

        x = x0
        y = y0

        ejex.append(
            x
        )

        ejey.append(
            y
        )

        while x < xf:

            pendiente = eval(
                expr,
                {"__builtins__": {}},
                {
                    "x": x,
                    "y": y,
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "log": math.log,
                    "exp": math.exp,
                    "sqrt": math.sqrt,
                    "pi": math.pi,
                    "e": math.e
                }
            )

            y = y + (
                h * pendiente
            )

            x = x + h

            ejex.append(
                x
            )

            ejey.append(
                y
            )

        return ejex, ejey
    
    #---NUEVO MÉTODO RUNGE-KUTTA V3.2.0---
    def metodo_runge_kutta(
        self,
        expr,
        sol_expr,
        x0,
        y0,
        xf,
        n,
        tipo
    ):
        """
        MÉTODO DE RUNGE-KUTTA (Segundo Orden):
        Técnica avanzada para integrar EDOs con mayor precisión que Euler.
        Calcula derivadas ponderadas en el intervalo (k1 y k2).
        Integra las variantes: Euler (Punto medio), Heun y Ralston.
        """
        ejex = []
        ejey_num = []
        ejey_ana = []

        # Configuración de Constantes según la variante elegida
        if "Euler" in tipo:
            # Variante de Punto Medio o Modified Euler
            a1 = 0.0
            a2 = 1.0
            q = 0.5
        elif "Heun" in tipo:
            # Variante Matemática Estándar para Heun de 2do Orden
            a1 = 0.5
            a2 = 0.5
            q = 1.0
        elif "Ralston" in tipo:
            # Método de Ralston
            a1 = 1.0 / 3.0
            a2 = 2.0 / 3.0
            q = 0.75
        else:
            # Base general ante contingencias
            a1 = 0.0
            a2 = 1.0
            q = 0.5

        h = (
            xf - x0
        ) / n

        x = x0
        y = y0

        ejex.append(
            x
        )

        ejey_num.append(
            y
        )
        
        permitido = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "exp": math.exp,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e
        }

        # Calculo Analítico en Nodo Inicial
        if sol_expr:
            entorno_ana = permitido.copy()
            entorno_ana["x"] = x
            y_ana = eval(
                sol_expr,
                {"__builtins__": {}},
                entorno_ana
            )
            ejey_ana.append(
                y_ana
            )
        else:
            # Si no hay analítica, se mapea la Y numérica original
            ejey_ana.append(
                y
            )

        for i in range(
            n
        ):
            # Paso 1: Computar K1
            entorno_k1 = permitido.copy()
            entorno_k1["x"] = x
            entorno_k1["y"] = y
            
            k1 = eval(
                expr,
                {"__builtins__": {}},
                entorno_k1
            )
            
            # Paso 2: Computar K2 usando los parámetros "q" seleccionados
            x_k2 = x + (
                q * h
            )
            
            y_k2 = y + (
                q * k1 * h
            )
            
            entorno_k2 = permitido.copy()
            entorno_k2["x"] = x_k2
            entorno_k2["y"] = y_k2
            
            k2 = eval(
                expr,
                {"__builtins__": {}},
                entorno_k2
            )
            
            # Paso 3: Calcular el Y(i+1) sumando componentes Ponderadas y avanzar X
            y = y + (
                (
                    (
                        a1 * k1
                    ) + (
                        a2 * k2
                    )
                ) * h
            )
            
            x = x + h
            
            ejex.append(
                x
            )
            
            ejey_num.append(
                y
            )
            
            # Evaluación de solución real analítica si existe en este iterador
            if sol_expr:
                entorno_ana_loop = permitido.copy()
                entorno_ana_loop["x"] = x
                y_ana = eval(
                    sol_expr,
                    {"__builtins__": {}},
                    entorno_ana_loop
                )
                ejey_ana.append(
                    y_ana
                )
            else:
                ejey_ana.append(
                    y
                )

        return ejex, ejey_num, ejey_ana

    #---CARGAR MÉTODO---
    def cargar_metodo(
        self
    ):
        
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()
            
        metodo = self.metodo_var.get()
        
        if not metodo:
            return
            
        if "────" in metodo:
            self.status.set(
                "Seleccione un método válido"
            )
            return
            
        self.status.set(
            ""
        )

        #---INTERPOLACIÓN LINEAL---
        if metodo == "Interpolación Lineal de Newton":
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(
                row=0, 
                column=0
            )
        
            self.entry_x = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x.grid(
                row=0, 
                column=1
            )
        
            ttk.Label(
                self.frame_inputs,
                text="Valores f(x):"
            ).grid(
                row=1, 
                column=0
            )
        
            self.entry_y = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_y.grid(
                row=1, 
                column=1
            )
        
            ttk.Label(
                self.frame_inputs,
                text="Incremento:"
            ).grid(
                row=2, 
                column=0
            )
        
            self.entry_incremento = ttk.Entry(
                self.frame_inputs
            )
            self.entry_incremento.grid(
                row=2, 
                column=1
            )
            
            self.entry_incremento.insert(
                0, 
                "0.5"
            )
            
        #---POLINOMIOS DE NEWTON---
        elif metodo == "Polinomios de Interpolación de Newton":
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(
                row=0, 
                column=0
            )
            
            self.entry_x = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x.grid(
                row=0, 
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="Valores Y:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_y = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_y.grid(
                row=1, 
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="x a interpolar:"
            ).grid(
                row=2, 
                column=0
            )
            
            self.entry_xinterp = ttk.Entry(
                self.frame_inputs
            )
            self.entry_xinterp.grid(
                row=2, 
                column=1
            )

        #---LAGRANGE---
        elif metodo == "Interpolación de Lagrange":
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(
                row=0, 
                column=0
            )

            self.entry_x = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x.grid(
                row=0, 
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="Valores Y:"
            ).grid(
                row=1, 
                column=0
            )

            self.entry_y = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_y.grid(
                row=1, 
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="Valor de x a interpolar:"
            ).grid(
                row=2, 
                column=0
            )

            self.entry_xinterp = ttk.Entry(
                self.frame_inputs
            )
            self.entry_xinterp.grid(
                row=2, 
                column=1
            )

        #---DIFERENCIAS FINITAS (DERIVACIÓN NUMÉRICA)---
        elif metodo == "Diferencias Finitas":
            ttk.Label(
                self.frame_inputs,
                text="Función f(x):"
            ).grid(
                row=0, 
                column=0
            )

            self.entry_func = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_func.grid(
                row=0, 
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="Valor de x:"
            ).grid(
                row=1, 
                column=0
            )

            self.entry_x_dif = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x_dif.grid(
                row=1, 
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="Tamaño de paso (h):"
            ).grid(
                row=2, 
                column=0
            )

            self.entry_h_dif = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_h_dif.grid(
                row=2, 
                column=1
            )
            
        #---TRAPECIOS---
        elif metodo == "Método de Trapecios":
            for widget in self.frame_inputs.winfo_children():
                widget.destroy()

            ttk.Label(
                self.frame_inputs, 
                text="Función f(x):"
            ).grid(
                row=0, 
                column=0, 
                sticky="w", 
                padx=5, 
                pady=2
            )
            
            self.entry_func = ttk.Entry(
                self.frame_inputs, 
                width=40
            )
            self.entry_func.grid(
                row=0, 
                column=1, 
                padx=5, 
                pady=2
            )

            ttk.Label(
                self.frame_inputs, 
                text="Límite inferior (a):"
            ).grid(
                row=1, 
                column=0, 
                sticky="w", 
                padx=5, 
                pady=2
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            self.entry_a.grid(
                row=1, 
                column=1, 
                padx=5, 
                pady=2
            )

            ttk.Label(
                self.frame_inputs, 
                text="Límite superior (b):"
            ).grid(
                row=2, 
                column=0, 
                sticky="w", 
                padx=5, 
                pady=2
            )
            
            self.entry_b = ttk.Entry(
                self.frame_inputs
            )
            self.entry_b.grid(
                row=2, 
                column=1, 
                padx=5, 
                pady=2
            )

            ttk.Label(
                self.frame_inputs, 
                text="Número de trapecios (n):"
            ).grid(
                row=3, 
                column=0, 
                sticky="w", 
                padx=5, 
                pady=2
            )
            
            self.entry_n = ttk.Entry(
                self.frame_inputs
            )
            self.entry_n.grid(
                row=3, 
                column=1, 
                padx=5, 
                pady=2
            )
            
            self.entry_n.insert(
                0, 
                "4"
            )

            self.status.set(
                "Método de Trapecios cargado correctamente"
            )
            return
            
        #---INTEGRACIÓN DE SIMPSON---
        elif metodo == "Método de Integración de Simpson":
            for widget in self.frame_inputs.winfo_children():
                widget.destroy()
        
            ttk.Label(
                self.frame_inputs, 
                text="Función:"
            ).grid(
                row=0, 
                column=0
            )
            
            self.entry_func = ttk.Entry(
                self.frame_inputs, 
                width=35
            )
            self.entry_func.grid(
                row=0, 
                column=1
            )
        
            ttk.Label(
                self.frame_inputs, 
                text="a:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            self.entry_a.grid(
                row=1, 
                column=1
            )
        
            ttk.Label(
                self.frame_inputs, 
                text="b:"
            ).grid(
                row=2, 
                column=0
            )
            
            self.entry_b = ttk.Entry(
                self.frame_inputs
            )
            self.entry_b.grid(
                row=2, 
                column=1
            )
        
            ttk.Label(
                self.frame_inputs, 
                text="Tipo:"
            ).grid(
                row=3, 
                column=0
            )
        
            self.tipo_simpson = tk.StringVar()
        
            ttk.Combobox(
                self.frame_inputs,
                textvariable=self.tipo_simpson,
                state="readonly",
                values=[
                    "1/3 Simple",
                    "1/3 Múltiple",
                    "3/8 Simple",
                    "3/8 Compuesta"
                ]
            ).grid(
                row=3, 
                column=1
            )
        
            ttk.Label(
                self.frame_inputs, 
                text="n:"
            ).grid(
                row=4, 
                column=0
            )
        
            self.entry_n = ttk.Entry(
                self.frame_inputs
            )
            self.entry_n.grid(
                row=4, 
                column=1
            )
            self.entry_n.insert(
                0, 
                "6"
            )
        
            self.status.set(
                "Simpson cargado correctamente"
            )
            return

        #---MÉTODO DE RUNGE-KUTTA (V3.2.0)---
        elif metodo == "Método de Runge-Kutta":
            
            for widget in self.frame_inputs.winfo_children():
                widget.destroy()

            ttk.Label(
                self.frame_inputs,
                text="dy/dx = f(x,y):"
            ).grid(
                row=0,
                column=0
            )

            self.entry_func = ttk.Entry(
                self.frame_inputs,
                width=40
            )

            self.entry_func.grid(
                row=0,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="Solución Analítica y(x)\n(Opcional, para gráfica/error):"
            ).grid(
                row=1,
                column=0
            )

            self.entry_sol = ttk.Entry(
                self.frame_inputs,
                width=40
            )

            self.entry_sol.grid(
                row=1,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="x0:"
            ).grid(
                row=2,
                column=0
            )

            self.entry_x0 = ttk.Entry(
                self.frame_inputs
            )

            self.entry_x0.grid(
                row=2,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="y0:"
            ).grid(
                row=3,
                column=0
            )

            self.entry_y0 = ttk.Entry(
                self.frame_inputs
            )

            self.entry_y0.grid(
                row=3,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="xf:"
            ).grid(
                row=4,
                column=0
            )

            self.entry_xf = ttk.Entry(
                self.frame_inputs
            )

            self.entry_xf.grid(
                row=4,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="Iteraciones (n):"
            ).grid(
                row=5,
                column=0
            )

            self.entry_n = ttk.Entry(
                self.frame_inputs
            )

            self.entry_n.grid(
                row=5,
                column=1
            )

            self.entry_n.insert(
                0,
                "10"
            )

            ttk.Label(
                self.frame_inputs,
                text="Tipo de Runge-Kutta:"
            ).grid(
                row=6,
                column=0
            )

            self.tipo_rk = tk.StringVar()

            ttk.Combobox(
                self.frame_inputs,
                textvariable=self.tipo_rk,
                state="readonly",
                values=[
                    "Euler (a1=0, a2=1, q=1/2)",
                    "Heun (a1=1/2, a2=1/2, q=1)",
                    "Ralston (a1=1/3, a2=2/3, q=3/4)"
                ],
                width=37
            ).grid(
                row=6,
                column=1
            )

            self.status.set(
                "Método de Runge-Kutta cargado exitosamente."
            )

            return
        
        #---MÉTODO DE EULER---
        elif metodo == "Método de Euler":

            ttk.Label(
                self.frame_inputs,
                text="dy/dx:"
            ).grid(
                row=0,
                column=0
            )

            self.entry_func = ttk.Entry(
                self.frame_inputs,
                width=40
            )

            self.entry_func.grid(
                row=0,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="x0:"
            ).grid(
                row=1,
                column=0
            )

            self.entry_x0 = ttk.Entry(
                self.frame_inputs
            )

            self.entry_x0.grid(
                row=1,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="y0:"
            ).grid(
                row=2,
                column=0
            )

            self.entry_y0 = ttk.Entry(
                self.frame_inputs
            )

            self.entry_y0.grid(
                row=2,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="xf:"
            ).grid(
                row=3,
                column=0
            )

            self.entry_xf = ttk.Entry(
                self.frame_inputs
            )

            self.entry_xf.grid(
                row=3,
                column=1
            )

            ttk.Label(
                self.frame_inputs,
                text="Iteraciones (n):"
            ).grid(
                row=4,
                column=0
            )

            self.entry_n = ttk.Entry(
                self.frame_inputs
            )

            self.entry_n.grid(
                row=4,
                column=1
            )

            self.entry_n.insert(
                0,
                "10"
            )

            self.status.set(
                "Método de Euler cargado correctamente"
            )

            return

        #---FUNCIONES GENERALES---
        if metodo not in [
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            "Diferencias Finitas",
            "Método de Trapecios",
            "Método de Integración de Simpson",
            "Método de Runge-Kutta",
            "Método de Euler"
        ]:
            ttk.Label(
                self.frame_inputs,
                text="Función:"
            ).grid(
                row=0, 
                column=0
            )
            
            self.entry_func = ttk.Entry(
                self.frame_inputs,
                width=35
            )
            
            self.entry_func.grid(
                row=0,
                column=1
            )

        #---NEWTON---
        if metodo == "Newton Raphson":
            ttk.Label(
                self.frame_inputs,
                text="f'(x):"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_fprima = ttk.Entry(
                self.frame_inputs,
                width=35
            )
            
            self.entry_fprima.grid(
                row=1,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="x0:"
            ).grid(
                row=2, 
                column=0
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_a.grid(
                row=2,
                column=1
            )

        #---SECANTE---
        elif metodo == "Secante":
            ttk.Label(
                self.frame_inputs,
                text="x0:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_a.grid(
                row=1,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="x1:"
            ).grid(
                row=2, 
                column=0
            )
            
            self.entry_b = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_b.grid(
                row=2,
                column=1
            )

        #---PUNTO FIJO---
        elif metodo == "Punto Fijo":
            ttk.Label(
                self.frame_inputs,
                text="x0:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_a.grid(
                row=1,
                column=1
            )

        #---BÚSQUEDA---
        elif metodo == "Búsqueda por Incrementos":
            ttk.Label(
                self.frame_inputs,
                text="x Inicial:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_a.grid(
                row=1,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="x Final:"
            ).grid(
                row=2, 
                column=0
            )

            self.entry_b = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_b.grid(
                row=2,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="Incremento:"
            ).grid(
                row=3, 
                column=0
            )
            
            self.entry_incremento = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_incremento.grid(
                row=3,
                column=1
            )
            
            self.entry_incremento.insert(
                0,
                "0.1"
            )

        #---MÍNIMOS CUADRADOS---
        elif metodo in [
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales"
        ]:
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_x = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            
            self.entry_x.grid(
                row=1,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="Valores Y:"
            ).grid(
                row=2, 
                column=0
            )
            
            self.entry_y = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            
            self.entry_y.grid(
                row=2,
                column=1
            )
            
            if metodo == "Mínimos Cuadrados Polinomiales":
                ttk.Label(
                    self.frame_inputs,
                    text="Grado:"
                ).grid(
                    row=3, 
                    column=0
                )
                
                self.entry_grado = ttk.Entry(
                    self.frame_inputs
                )
                
                self.entry_grado.grid(
                    row=3,
                    column=1
                )
                
                self.entry_grado.insert(
                    0,
                    "2"
                )

        #---BISECCIÓN/FALSA POSICIÓN---
        elif metodo in [
            "Bisección",
            "Falsa Posición"
        ]:
            ttk.Label(
                self.frame_inputs,
                text="Límite a:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_a = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_a.grid(
                row=1,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="Límite b:"
            ).grid(
                row=2, 
                column=0
            )
            
            self.entry_b = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_b.grid(
                row=2,
                column=1
            )
            
        #---TOLERANCIA---
        if metodo not in [
            "Búsqueda por Incrementos",
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            "Diferencias Finitas",
            "Método de Trapecios",
            "Método de Runge-Kutta"
        ]:
            ttk.Label(
                self.frame_inputs,
                text="Tolerancia:"
            ).grid(
                row=3, 
                column=0
            )
            
            self.entry_error = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_error.grid(
                row=3,
                column=1
            )
            
            self.entry_error.insert(
                0,
                "0.0001"
            )
            
        self.status.set(
            f"Configuración para {metodo} cargada"
        )
        
    #---LIMPIAR GRÁFICAS PREVIAS EN TKINTER---
    def preparar_canvas(
        self
    ):
        """
        Destruye y limpia cualquier gráfica renderizada en turnos anteriores
        para proporcionar un canvas fresco y listo.
        """
        for widget in self.frame_graficas.winfo_children():
            widget.destroy()
            
        fig = Figure(
            figsize=(10, 4), 
            dpi=100
        )
        return fig

    #---EJECUTAR---
    def ejecutar_metodo(
        self
    ):
        try:
            metodo = self.metodo_var.get()
            tipo_error_sel = self.tipo_error_var.get()
            
            fig = self.preparar_canvas()

            #---INTERPOLACIÓN LINEAL---
            if metodo == "Interpolación Lineal de Newton":
                x_tabla = list(
                    map(
                        float,
                        self.entry_x.get().split(",")
                    )
                )
            
                y_tabla = list(
                    map(
                        float,
                        self.entry_y.get().split(",")
                    )
                )
            
                incremento = float(
                    self.entry_incremento.get()
                )
            
                x0 = x_tabla[0]
                y0 = y_tabla[0]
            
                x1 = x_tabla[-1]
                y1 = y_tabla[-1]
            
                pendiente = (
                    y1 - y0
                ) / (
                    x1 - x0
                )
            
                x = x0
            
                ex = []
                ey_error = []
                ey_interp = []
            
                texto = ""
            
                while x <= x1:
                    interp = y0 + pendiente * (
                        x - x0
                    )
            
                    real = np.interp(
                        x,
                        x_tabla,
                        y_tabla
                    )
            
                    error = self.calcular_error(real, interp, tipo_error_sel)
            
                    texto += (
                        f"x={x:.3f}"
                        f" interp={interp:.4f}"
                        f" error={error:.5f}\n"
                    )
            
                    ex.append(x)
                    ey_error.append(error)
                    ey_interp.append(interp)
            
                    x += incremento
            
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
            
                self.text_resultados.insert(
                    tk.END,
                    texto
                )
            
                ax1 = fig.add_subplot(121)
                ax1.plot(
                    ex, 
                    ey_interp, 
                    marker='o', 
                    label="Interpolación"
                )
                ax1.scatter(
                    x_tabla, 
                    y_tabla, 
                    color="red", 
                    label="Datos"
                )
                ax1.set_title("Interpolación")
                ax1.set_xlabel("x")
                ax1.set_ylabel("y")
                ax1.legend()
                ax1.grid(True)
                
                ax2 = fig.add_subplot(122)
                ax2.plot(
                    ex, 
                    ey_error, 
                    marker='s', 
                    color='orange', 
                    label=f"Error {tipo_error_sel}"
                )
                ax2.set_title(f"Gráfica de Error ({tipo_error_sel})")
                ax2.set_xlabel("x")
                ax2.set_ylabel("Error")
                ax2.legend()
                ax2.grid(True)
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---POLINOMIOS DE NEWTON---
            elif metodo == "Polinomios de Interpolación de Newton":
                arreglo_x = list(
                    map(
                        float,
                        self.entry_x.get().split(
                            ","
                        )
                    )
                )
                
                arreglo_y = list(
                    map(
                        float,
                        self.entry_y.get().split(
                            ","
                        )
                    )
                )
                
                x_interp = float(
                    self.entry_xinterp.get()
                )
                
                resultado, coeficientes, tabla = self.metodo_polinomios_newton(
                    arreglo_x,
                    arreglo_y,
                    x_interp
                )
                
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + "\nCoeficientes:\n"
                )
                
                for i, coef in enumerate(
                    coeficientes
                ):
                    texto += (
                        f"b{i} = {coef}\n"
                    )
                    
                texto += (
                    f"\nResultado interpolado:"
                    f"\nf({x_interp}) = {resultado}\n"
                )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )
                
                ax1 = fig.add_subplot(121)
                ax1.scatter(
                    arreglo_x,
                    arreglo_y,
                    color='blue',
                    label='Puntos Dados'
                )
                
                x_vals = np.linspace(min(arreglo_x), max(arreglo_x), 100)
                y_vals = [self.metodo_polinomios_newton(arreglo_x, arreglo_y, v)[0] for v in x_vals]
                
                ax1.plot(
                    x_vals,
                    y_vals,
                    color='gray',
                    linestyle='--'
                )
                
                ax1.plot(
                    x_interp,
                    resultado,
                    marker='o',
                    color='red',
                    label='Punto Interpolado'
                )
                ax1.set_title("Polinomios de Newton")
                ax1.legend()
                ax1.grid(True)
                
                errores_nodos = []
                for i in range(len(arreglo_x)):
                    val_calc = self.metodo_polinomios_newton(arreglo_x, arreglo_y, arreglo_x[i])[0]
                    err = self.calcular_error(arreglo_y[i], val_calc, tipo_error_sel)
                    errores_nodos.append(err)
                    
                ax2 = fig.add_subplot(122)
                ax2.bar(
                    [str(x) for x in arreglo_x],
                    errores_nodos,
                    color='orange',
                    label=f"Error {tipo_error_sel} en Nodos"
                )
                ax2.set_title("Error en los nodos")
                ax2.set_ylabel("Error")
                ax2.legend()
                ax2.grid(True)
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---INTERPOLACIÓN DE LAGRANGE---
            elif metodo == "Interpolación de Lagrange":
                arreglo_x = list(
                    map(
                        float,
                        self.entry_x.get().split(
                            ","
                        )
                    )
                )
                
                arreglo_y = list(
                    map(
                        float,
                        self.entry_y.get().split(
                            ","
                        )
                    )
                )
                
                valor = float(
                    self.entry_xinterp.get()
                )

                resultado = self.metodo_lagrange(
                    arreglo_x,
                    arreglo_y,
                    valor
                )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nValor interpolado para x={valor}:\n"
                    + f"f({valor}) = {resultado}\n"
                )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )

                ax1 = fig.add_subplot(121)
                ax1.scatter(
                    arreglo_x,
                    arreglo_y,
                    color='black',
                    label='Puntos Iniciales'
                )
                
                x_vals = np.linspace(min(arreglo_x), max(arreglo_x), 100)
                y_vals = [self.metodo_lagrange(arreglo_x, arreglo_y, v) for v in x_vals]
                ax1.plot(x_vals, y_vals, '--', color="blue")
                
                ax1.plot(
                    valor,
                    resultado,
                    marker='*',
                    markersize=15,
                    color='magenta',
                    label='Punto Lagrange'
                )
                ax1.set_title("Interpolación de Lagrange")
                ax1.grid(True, linestyle='--')
                ax1.legend()
                
                errores_nodos = []
                for i in range(len(arreglo_x)):
                    val_calc = self.metodo_lagrange(arreglo_x, arreglo_y, arreglo_x[i])
                    err = self.calcular_error(arreglo_y[i], val_calc, tipo_error_sel)
                    errores_nodos.append(err)
                    
                ax2 = fig.add_subplot(122)
                ax2.bar(
                    [str(x) for x in arreglo_x],
                    errores_nodos,
                    color='red',
                    label=f"Error {tipo_error_sel} en Nodos"
                )
                ax2.set_title("Error del método de Lagrange")
                ax2.legend()
                ax2.grid(True)
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---MÍNIMOS CUADRADOS LINEALES---
            elif metodo == "Mínimos Cuadrados Lineales":
                arreglo_x = list(map(float, self.entry_x.get().split(",")))
                arreglo_y = list(map(float, self.entry_y.get().split(",")))
                
                a, b, eje_y_calc = self.metodo_minimos_cuadrados(arreglo_x, arreglo_y)
                
                self.text_resultados.delete(1.0, tk.END)
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nEcuación de la recta: y = {a:.4f}x + {b:.4f}\n"
                )
                self.text_resultados.insert(tk.END, texto)
                
                ax1 = fig.add_subplot(121)
                ax1.scatter(arreglo_x, arreglo_y, color='red', label="Datos Reales")
                ax1.plot(arreglo_x, eje_y_calc, color='blue', label="Ajuste Lineal")
                ax1.set_title("Regresión Lineal")
                ax1.grid(True)
                ax1.legend()
                
                errores = [self.calcular_error(arreglo_y[i], eje_y_calc[i], tipo_error_sel) for i in range(len(arreglo_x))]
                
                ax2 = fig.add_subplot(122)
                ax2.plot(arreglo_x, errores, marker='o', color='green', label=f"Error {tipo_error_sel}")
                ax2.set_title(f"Error {tipo_error_sel} de los Residuales")
                ax2.grid(True)
                ax2.legend()
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
                
            #---MÍNIMOS CUADRADOS POLINOMIALES---
            elif metodo == "Mínimos Cuadrados Polinomiales":
                arreglo_x = list(map(float, self.entry_x.get().split(",")))
                arreglo_y = list(map(float, self.entry_y.get().split(",")))
                grado = int(self.entry_grado.get())
                
                coefs, eje_y_calc, pol = self.metodo_minimos_cuadrados_polinomiales(arreglo_x, arreglo_y, grado)
                
                self.text_resultados.delete(1.0, tk.END)
                texto = f"MÉTODO: {metodo} (Grado {grado})\n" + "-" * 30 + "\nPolinomio:\n" + str(pol) + "\n"
                self.text_resultados.insert(tk.END, texto)
                
                x_continuo = np.linspace(min(arreglo_x), max(arreglo_x), 100)
                y_continuo = pol(x_continuo)
                
                ax1 = fig.add_subplot(121)
                ax1.scatter(arreglo_x, arreglo_y, color='black', label="Datos")
                ax1.plot(x_continuo, y_continuo, color='magenta', label=f"Ajuste Pol. Grado {grado}")
                ax1.set_title("Regresión Polinomial")
                ax1.grid(True)
                ax1.legend()
                
                errores = [self.calcular_error(arreglo_y[i], eje_y_calc[i], tipo_error_sel) for i in range(len(arreglo_x))]
                
                ax2 = fig.add_subplot(122)
                ax2.bar([str(x) for x in arreglo_x], errores, color='cyan', label=f"Error {tipo_error_sel}")
                ax2.set_title(f"Error {tipo_error_sel} de Ajuste")
                ax2.grid(True)
                ax2.legend()
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---DIFERENCIAS FINITAS---
            elif metodo == "Diferencias Finitas":
                expr = self.entry_func.get()
                
                x = float(
                    self.entry_x_dif.get()
                )
                
                h = float(
                    self.entry_h_dif.get()
                )

                (
                    d1_ad, d1_at, d1_ce,
                    d2_ad, d2_at, d2_ce
                ) = self.metodo_diferencias_finitas(
                    expr,
                    x,
                    h
                )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nFunción evaluada: {expr}"
                    + f"\nx = {x}, h = {h}\n"
                    + "\n-- Primera Derivada f'(x) --\n"
                    + f"Hacia Adelante: {d1_ad}\n"
                    + f"Hacia Atrás:    {d1_at}\n"
                    + f"Central:        {d1_ce}\n"
                    + "\n-- Segunda Derivada f''(x) --\n"
                    + f"Hacia Adelante: {d2_ad}\n"
                    + f"Hacia Atrás:    {d2_at}\n"
                    + f"Central:        {d2_ce}\n"
                )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )

                ax1 = fig.add_subplot(121)
                x_vals = np.linspace(x - 2, x + 2, 100)
                y_vals = [self.evaluar_funcion(expr, v) for v in x_vals]
                punto_y = self.evaluar_funcion(expr, x)
                
                y_tangente = [punto_y + d1_ce * (v - x) for v in x_vals]

                ax1.plot(x_vals, y_vals, color='blue', label=f"f(x) = {expr}")
                ax1.plot(x_vals, y_tangente, color='green', linestyle='--', label="Tangente Aproximada")
                ax1.plot(x, punto_y, marker='o', color='red', label='Punto Evaluado')
                ax1.set_title("Función y Tangente")
                ax1.grid(True, alpha=0.5)
                ax1.legend()
                
                h_vals = [h, h/2, h/4, h/8, h/16]
                errores_h = []
                derivada_exacta_aprox = self.metodo_diferencias_finitas(expr, x, 1e-5)[2] 
                
                for paso in h_vals:
                    val_aprox = self.metodo_diferencias_finitas(expr, x, paso)[2]
                    err = self.calcular_error(derivada_exacta_aprox, val_aprox, tipo_error_sel)
                    errores_h.append(err)
                    
                ax2 = fig.add_subplot(122)
                ax2.plot(h_vals, errores_h, marker='^', color='red', label=f"Error {tipo_error_sel} vs h")
                ax2.set_xscale('log') 
                ax2.set_title("Análisis de Error")
                ax2.set_xlabel("Tamaño de paso h")
                ax2.set_ylabel("Error")
                ax2.grid(True)
                ax2.legend()
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---TRAPECIOS---
            elif metodo == "Método de Trapecios":
                expr = self.entry_func.get()
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                n = int(self.entry_n.get())

                resultado, x_vals, y_vals = self.metodo_trapecios(expr, a, b, n)

                self.status.set("Cálculo completado exitosamente.")
                
                self.text_resultados.config(state="normal") 
                self.text_resultados.delete("1.0", tk.END)  
                
                texto = (
                    f"--- RESULTADOS MÉTODO DE TRAPECIOS ---\n"
                    f"MÉTODO: {metodo}\n"
                    f"------------------------------\n"
                    f"Integral aproximada = {resultado:.8f}\n"
                    f"Intervalo: [{a}, {b}]\n"
                    f"Número de trapecios: {n}\n"
                )
                self.text_resultados.insert(tk.END, texto)
                self.text_resultados.config(state="disabled") 

                ax1 = fig.add_subplot(121)
                x_cont = np.linspace(a, b, 200)
                y_cont = [self.evaluar_funcion(expr, x) for x in x_cont]

                ax1.plot(x_cont, y_cont, label='f(x)')
                ax1.plot(x_vals, y_vals, marker='o', linestyle='-', label='Trapecios')

                for i in range(len(x_vals)-1):
                    ax1.fill(
                        [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]],
                        [0, y_vals[i], y_vals[i+1], 0],
                        alpha=0.2, color='orange'
                    )

                ax1.set_title("Integración por Trapecios")
                ax1.set_xlabel("x")
                ax1.set_ylabel("f(x)")
                ax1.grid(True)
                ax1.legend()
                
                n_vals = [2, 4, 8, 16, 32]
                errores_n = []
                
                ref_integral, _, _ = self.metodo_trapecios(expr, a, b, 500)
                
                for num_traps in n_vals:
                    val_aprox, _, _ = self.metodo_trapecios(expr, a, b, num_traps)
                    err = self.calcular_error(ref_integral, val_aprox, tipo_error_sel)
                    errores_n.append(err)
                    
                ax2 = fig.add_subplot(122)
                ax2.plot(n_vals, errores_n, marker='s', color='purple', label=f"Error {tipo_error_sel} vs n")
                ax2.set_title("Convergencia del Error")
                ax2.set_xlabel("Número de Trapecios (n)")
                ax2.set_ylabel("Error")
                ax2.grid(True)
                ax2.legend()
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---MÉTODOS DE RAÍCES---
            elif metodo in [
                "Bisección", 
                "Falsa Posición", 
                "Newton Raphson", 
                "Secante", 
                "Punto Fijo"
            ]:
                expr = self.entry_func.get()
                
                erra = float(
                    self.entry_error.get()
                )
                
                raiz = None

                if metodo == "Bisección":
                    a = float(
                        self.entry_a.get()
                    )
                    
                    b = float(
                        self.entry_b.get()
                    )
                    
                    raiz, err, ex, ey = self.metodo_biseccion(
                        expr, 
                        a, 
                        b, 
                        erra,
                        tipo_error_sel
                    )

                elif metodo == "Falsa Posición":
                    a = float(
                        self.entry_a.get()
                    )
                    
                    b = float(
                        self.entry_b.get()
                    )
                    
                    raiz, err, ex, ey = self.metodo_falsa_posicion(
                        expr, 
                        a, 
                        b, 
                        erra,
                        tipo_error_sel
                    )

                elif metodo == "Newton Raphson":
                    fprima = self.entry_fprima.get()
                    
                    xi = float(
                        self.entry_a.get()
                    )
                    
                    raiz, err, ex, ey = self.metodo_newton_raphson(
                        expr, 
                        fprima, 
                        xi, 
                        erra,
                        tipo_error_sel
                    )

                elif metodo == "Secante":
                    x0 = float(
                        self.entry_a.get()
                    )
                    
                    x1 = float(
                        self.entry_b.get()
                    )
                    
                    raiz, err, ex, ey = self.metodo_secante(
                        expr, 
                        x0, 
                        x1, 
                        erra,
                        tipo_error_sel
                    )

                elif metodo == "Punto Fijo":
                    x0 = float(
                        self.entry_a.get()
                    )
                    
                    raiz, err, ex, ey = self.metodo_punto_fijo(
                        expr, 
                        x0, 
                        erra,
                        tipo_error_sel
                    )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nRaíz encontrada: {raiz}\n"
                    + f"Error Final ({tipo_error_sel}): {err}\n"
                    + f"Iteraciones Totales: {len(ex)}\n"
                )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )

                ax = fig.add_subplot(111)
                
                ax.plot(
                    ex,
                    ey,
                    marker='s',
                    color='green',
                    linestyle='-.',
                    label=f'Error {tipo_error_sel}'
                )
                
                ax.set_title(
                    f"Gráfica de Error {tipo_error_sel}: {metodo}"
                )
                
                ax.set_xlabel(
                    "Número de Iteración"
                )
                
                ax.set_ylabel(
                    f"Magnitud de Error {tipo_error_sel}"
                )
                
                if tipo_error_sel == "Porcentual" or max(ey) > 100 * min(ey + [0.0001]):
                    ax.set_yscale('log')
                
                ax.grid(
                    True,
                    which="both"
                )
                
                ax.legend()
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
                
            #---INTEGRACIÓN DE SIMPSON---
            elif metodo == "Método de Integración de Simpson":
                expr = self.entry_func.get()
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                tipo = self.tipo_simpson.get()
                n = int(self.entry_n.get())
    
                integral, integral_real = self.metodo_simpson(expr, a, b, tipo, n)
                
                error_final = self.calcular_error(integral_real, integral, tipo_error_sel)
    
                self.status.set("Cálculo completado exitosamente.")
                
                self.text_resultados.config(state="normal") 
                self.text_resultados.delete("1.0", tk.END)
                
                texto_final = (
                    f"--- RESULTADOS MÉTODO DE SIMPSON ---\n"
                    f"Tipo seleccionado: {tipo}\n"
                    f"Valor de la Integral: {integral:.8f}\n"
                    f"Integral Real (Aprox.): {integral_real:.8f}\n"
                    f"Error {tipo_error_sel}: {error_final:.6f}\n"
                )
                self.text_resultados.insert(tk.END, texto_final)
                self.text_resultados.config(state="disabled")
                
                ax1 = fig.add_subplot(121)
                
                x_func = np.linspace(
                    a,
                    b,
                    500
                )
                
                y_func = [
                    self.evaluar_funcion(
                        expr,
                        x
                    )
                    for x in x_func
                ]
                
                ax1.plot(
                    x_func,
                    y_func,
                    color="blue",
                    linewidth=2,
                    label="f(x)"
                )
                
                if tipo == "1/3 Simple":
                    x_pts = np.linspace(a, b, 3)
                elif tipo == "3/8 Simple":
                    x_pts = np.linspace(a, b, 4)
                else:
                    x_pts = np.linspace(a, b, n + 1)
                
                y_pts = [
                    self.evaluar_funcion(expr, x)
                    for x in x_pts
                ]
                
                ax1.plot(
                    x_pts,
                    y_pts,
                    marker='o',
                    linewidth=2,
                    label=tipo
                )
                
                for x in x_pts:
                    ax1.axvline(
                        x,
                        linestyle="--",
                        alpha=0.4,
                        color="gray"
                    )
                
                ax1.fill_between(
                    x_func,
                    y_func,
                    alpha=0.2,
                    color="cyan"
                )
                
                ax1.set_xlabel("x")
                ax1.set_ylabel("f(x)")
                ax1.set_title(f"Simpson {tipo}")
                ax1.grid(True)
                ax1.legend()
                
                ax2 = fig.add_subplot(122)
                
                if "Múltiple" in tipo or "Compuesta" in tipo:
                    n_vals = [n, n+2, n+4, n+6, n+8] if "Múltiple" in tipo else [n, n+3, n+6, n+9, n+12]
                    errores_n = []
                    
                    for num_int in n_vals:
                        val_aprox, _ = self.metodo_simpson(expr, a, b, tipo, num_int)
                        err = self.calcular_error(integral_real, val_aprox, tipo_error_sel)
                        errores_n.append(err)
                        
                    ax2.plot(n_vals, errores_n, marker='D', color='magenta', label=f"Error {tipo_error_sel} vs n")
                    ax2.set_title("Convergencia del Error (Simpson)")
                    ax2.set_xlabel("Número de intervalos (n)")
                    ax2.set_ylabel("Error")
                else:
                    ax2.bar(["Simpson Simple"], [error_final], color='magenta')
                    ax2.set_title(f"Magnitud del Error {tipo_error_sel}")
                    ax2.set_ylabel("Error")
                    
                ax2.grid(True)
                ax2.legend()

                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            #---MÉTODO DE RUNGE-KUTTA (V3.2.0)---
            elif metodo == "Método de Runge-Kutta":

                expr = self.entry_func.get()
                
                sol_expr = self.entry_sol.get()

                x0 = float(
                    self.entry_x0.get()
                )

                y0 = float(
                    self.entry_y0.get()
                )

                xf = float(
                    self.entry_xf.get()
                )

                n = int(
                    self.entry_n.get()
                )
                
                tipo = self.tipo_rk.get()
                
                if not tipo:
                    raise ValueError(
                        "Por favor, selecciona una variante de Runge-Kutta en el menú desplegable."
                    )

                ejex, ejey_num, ejey_ana = self.metodo_runge_kutta(
                    expr,
                    sol_expr,
                    x0,
                    y0,
                    xf,
                    n,
                    tipo
                )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )

                # Mostramos los resultados del cálculo final
                texto = (
                    f"MÉTODO: Runge-Kutta 2do Orden ({tipo.split(' ')[0]})\n"
                    + "-" * 30
                    + "\nValor final numérico aproximado:\n"
                    + "y({xf}) = {ejey_num[-1]:.6f}\n"
                )
                
                # Si se proveyó solución analítica, mostramos la comparativa directa
                if sol_expr:
                    texto += (
                        f"Valor final real analítico:\n"
                        f"y_real({xf}) = {ejey_ana[-1]:.6f}\n"
                    )
                    error_final = self.calcular_error(
                        ejey_ana[-1],
                        ejey_num[-1],
                        tipo_error_sel
                    )
                    texto += (
                        f"Error {tipo_error_sel} final: {error_final:.6f}\n"
                    )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )

                # --- GRÁFICA 1: Puntos numéricos y curva analítica ---
                ax1 = fig.add_subplot(121)

                # Graficamos la solución obtenida con el método numérico de Kutta
                ax1.plot(
                    ejex,
                    ejey_num,
                    marker='o',
                    color='blue',
                    label=f'Aprox. Kutta ({tipo.split(" ")[0]})'
                )
                
                # Si el usuario metió la analítica, la mostramos en continuo y marcamos los nodos
                if sol_expr:
                    x_cont = np.linspace(
                        x0,
                        xf,
                        300
                    )
                    permitido = {
                        "sin": math.sin,
                        "cos": math.cos,
                        "tan": math.tan,
                        "log": math.log,
                        "exp": math.exp,
                        "sqrt": math.sqrt,
                        "pi": math.pi,
                        "e": math.e
                    }
                    
                    y_cont = []
                    for val in x_cont:
                        entorno_cont = permitido.copy()
                        entorno_cont["x"] = val
                        y_val = eval(
                            sol_expr,
                            {"__builtins__": {}},
                            entorno_cont
                        )
                        y_cont.append(
                            y_val
                        )
                        
                    # Curva suavizada analítica
                    ax1.plot(
                        x_cont,
                        y_cont,
                        color='red',
                        linewidth=1.5,
                        label='Curva Analítica Real'
                    )
                    
                    # Puntos analíticos que corresponden a cada paso calculado
                    ax1.scatter(
                        ejex,
                        ejey_ana,
                        color='black',
                        s=35,
                        label='Puntos Analíticos',
                        zorder=5
                    )

                ax1.set_title(
                    "Evolución EDO: Kutta vs Analítico"
                )

                ax1.set_xlabel(
                    "Eje x"
                )

                ax1.set_ylabel(
                    "Eje y (función evaluada)"
                )

                ax1.grid(True)

                ax1.legend()

                # --- GRÁFICA 2: El error a través de las iteraciones ---
                ax2 = fig.add_subplot(122)
                
                errores = []
                for i in range(
                    len(
                        ejex
                    )
                ):
                    # El error se calcula con el valor analítico si existe
                    if sol_expr:
                        err = self.calcular_error(
                            ejey_ana[i],
                            ejey_num[i],
                            tipo_error_sel
                        )
                    else:
                        # Si no hay analítica, se aproxima el error contra el escalón numérico anterior
                        if i == 0:
                            err = 0
                        else:
                            err = self.calcular_error(
                                ejey_num[i],
                                ejey_num[i-1],
                                tipo_error_sel
                            )
                    errores.append(
                        err
                    )

                ax2.plot(
                    ejex,
                    errores,
                    marker='s',
                    color='orange',
                    label=f'Error {tipo_error_sel}'
                )
                
                ax2.set_title(
                    f"Gráfica de Magnitud de Error ({tipo_error_sel})"
                )
                
                ax2.set_xlabel(
                    "Eje x"
                )
                
                ax2.set_ylabel(
                    "Unidades de Error"
                )
                
                ax2.grid(True)
                
                ax2.legend()

                canvas = FigureCanvasTkAgg(
                    fig,
                    master=self.frame_graficas
                )

                canvas.draw()

                canvas.get_tk_widget().pack(
                    fill=tk.BOTH,
                    expand=True
                )

            #---MÉTODO DE EULER (Primer Orden)---
            elif metodo == "Método de Euler":

                expr = self.entry_func.get()

                x0 = float(
                    self.entry_x0.get()
                )

                y0 = float(
                    self.entry_y0.get()
                )

                xf = float(
                    self.entry_xf.get()
                )

                n = int(
                    self.entry_n.get()
                )

                ejex, ejey = self.metodo_euler(
                    expr,
                    x0,
                    y0,
                    xf,
                    n
                )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )

                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + "\nValor final aproximado:\n"
                    + "y({xf}) = {ejey[-1]}\n"
                )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )

                ax = fig.add_subplot(111)

                ax.plot(
                    ejex,
                    ejey,
                    marker='o',
                    color='blue',
                    label='Euler'
                )

                ax.set_title(
                    "Aproximación por Método de Euler"
                )

                ax.set_xlabel(
                    "x"
                )

                ax.set_ylabel(
                    "y"
                )

                ax.grid(True)

                ax.legend()

                canvas = FigureCanvasTkAgg(
                    fig,
                    master=self.frame_graficas
                )

                canvas.draw()

                canvas.get_tk_widget().pack(
                    fill=tk.BOTH,
                    expand=True
                )
            
            #---BÚSQUEDA POR INCREMENTOS---
            elif metodo == "Búsqueda por Incrementos":
                expr = self.entry_func.get()
                xi = float(self.entry_a.get())
                xf = float(self.entry_b.get())
                incremento = float(self.entry_incremento.get())
                
                intervalos, ejex, ejey = self.metodo_busqueda_incrementos(expr, xi, xf, incremento)
                
                self.text_resultados.delete(1.0, tk.END)
                texto = f"MÉTODO: {metodo}\n" + "-" * 30 + "\nIntervalos con raíces:\n"
                for i in intervalos:
                    texto += f"Raíz entre [{i[0]:.4f}, {i[1]:.4f}]\n"
                self.text_resultados.insert(tk.END, texto)
                
                ax = fig.add_subplot(111)
                ax.plot(ejex, ejey, marker='.', label="Función")
                ax.axhline(0, color="red", linestyle="--")
                for i in intervalos:
                    ax.axvspan(i[0], i[1], color='yellow', alpha=0.3, label="Raíz detectada")
                
                handles, labels = ax.get_legend_handles_labels()
                by_label = dict(zip(labels, handles))
                ax.legend(by_label.values(), by_label.keys())
                
                ax.set_title("Búsqueda de Raíces por Incrementos")
                ax.grid(True)
                
                canvas = FigureCanvasTkAgg(fig, master=self.frame_graficas)
                canvas.draw()
                canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            else:
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                self.text_resultados.insert(
                    tk.END,
                    f"Método {metodo} en construcción."
                )

        except Exception as e:
            messagebox.showerror(
                "Error en la Ejecución",
                f"Ha ocurrido un problema al ejecutar los cálculos numéricos:\n{str(e)}"
            )

#---INICIO DE LA APLICACIÓN---
if __name__ == "__main__":
    
    ventana_principal = tk.Tk()
    
    app = MetodosNumericosApp(
        ventana_principal
    )
    
    ventana_principal.mainloop()
