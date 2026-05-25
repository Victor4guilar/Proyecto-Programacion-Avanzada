#---IMPORTACIONES---
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math
import numpy as np

#---CLASE PRINCIPAL---
class MetodosNumericosApp:
    VERSION = "v1.13.0"
    
    def __init__(
        self,
        root
    ):
        self.root = root
        
        self.root.title(
            f"Suite de Métodos Numéricos {self.VERSION}"
        )
        
        self.root.geometry(
            "950x650"
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
            "Método de Integración de Simpson"
        ]
        
        self.crear_layout()
        
        self.crear_statusbar()

    #---INTERFAZ---
    def crear_layout(
        self
    ):
        self.main_frame = ttk.Frame(
            self.root
        )
        
        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
        
        #Panel izquierdo
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
        
        # 1. SE CAMBIÓ A state="normal" PARA PERMITIR ESCRITURA
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
            "Método de Integración de Simpson"
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
        
        # 2. AGREGE OPCIÓN PARA EL TIPO DE ERROR
        ttk.Label(
            self.panel_control,
            text="Tipo de Error para Gráficas:"
        ).pack(
            pady=5
        )
        
        self.tipo_error_var = tk.StringVar(value="Relativo")
        
        self.combo_error = ttk.Combobox(
            self.panel_control,
            textvariable=self.tipo_error_var,
            state="readonly",
            values=["Absoluto", "Relativo", "Porcentual"],
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

        #Panel derecho
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
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )
        
        self.text_resultados = tk.Text(
            self.frame_resultados,
            height=10
        )
        
        self.text_resultados.pack(
            fill="both",
            expand=True
        )

    #---STATUSBAR---
    def crear_statusbar(
        self
    ):
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
        texto_busqueda = self.metodo_var.get().lower()
        if texto_busqueda == "":
            self.combo_metodos['values'] = self.opciones_completas
        else:
            filtrados = [m for m in self.lista_metodos_original if texto_busqueda in m.lower()]
            self.combo_metodos['values'] = filtrados
            self.combo_metodos.event_generate('<Down>')

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
        ejex, ejey = [], []
        n = 0
        pi_anterior = a
        error = 100
        
        while error > erra and n < 500:
            pi = (
                a + b
            ) / 2
            
            if n > 0:
                error = self.calcular_error(pi, pi_anterior, tipo_error)
            else:
                error = abs(b - a) if tipo_error == "Absoluto" else 100
            
            fa = self.evaluar_funcion(
                expr,
                a
            )
            
            fpi = self.evaluar_funcion(
                expr,
                pi
            )
            
            if fa * fpi <= 0:
                b = pi
            else:
                a = pi
                
            pi_anterior = pi
            n += 1
            
            ejex.append(
                n
            )
            ejey.append(
                error
            )
            
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
        ejex, ejey = [], []
        iteracion = 0
        xr_anterior = a
        error = 100
        
        while error > erra and iteracion < 500:
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
                error = self.calcular_error(xr, xr_anterior, tipo_error)
                
            if fa * fxr < 0:
                b = xr
            else:
                a = xr
                
            xr_anterior = xr
            iteracion += 1
            
            ejex.append(
                iteracion
            )
            ejey.append(
                error
            )
            
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
        ejex, ejey = [], []
        error = 100
        n = 0
        
        while error > erra and n < 500:
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
                error = self.calcular_error(Xn, Xi, tipo_error)
            else:
                error = 100
            
            Xi = Xn
            n += 1
            
            ejex.append(
                n
            )
            ejey.append(
                error
            )
            
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
        ejex, ejey = [], []
        error = 100
        n = 0
        
        while error > erra and n < 100:
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
            
            error = self.calcular_error(x2, x1, tipo_error)
            
            x0, x1 = x1, x2
            n += 1
            
            ejex.append(
                n
            )
            ejey.append(
                error
            )
            
        return x1, error, ejex, ejey

    #---PUNTO FIJO---
    def metodo_punto_fijo(
        self,
        gx,
        x0,
        erra,
        tipo_error
    ):
        ejex, ejey = [], []
        error = 100
        n = 0
        
        while error > erra and n < 100:
            x1 = self.evaluar_funcion(
                gx,
                x0
            )
            
            error = self.calcular_error(x1, x0, tipo_error)
            
            x0 = x1
            n += 1
            
            ejex.append(
                n
            )
            ejey.append(
                error
            )
            
        return x1, error, ejex, ejey

    #---BÚSQUEDA POR INCREMENTOS---
    def metodo_busqueda_incrementos(
        self,
        expr,
        xi,
        xf,
        incremento
    ):
        ejex, ejey = [], []
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
        
        eje_y = []
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
            eje_y.append(
                funcion
            )
            
        return a, b, eje_y

    #---MÍNIMOS CUADRADOS POLINOMIALES---
    def metodo_minimos_cuadrados_polinomiales(
        self,
        arreglo_x,
        arreglo_y,
        grado
    ):
        coeficientes = np.polyfit(
            arreglo_x,
            arreglo_y,
            grado
        )
        
        polinomio = np.poly1d(
            coeficientes
        )
        
        eje_y = polinomio(
            arreglo_x
        )
        
        return coeficientes, eje_y

    #---INTERPOLACIÓN LINEAL DE NEWTON---
    def metodo_interpolacion_newton(
        self,
        x0,
        y0,
        x1,
        y1,
        x_interp
    ):
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

        # Primera derivada
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

        # Segunda derivada
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
        h = (b - a) / n

        suma = 0
        x_vals = []
        y_vals = []

        for i in range(n + 1):
            x = a + (i * h)
            fx = self.evaluar_funcion(expr, x)

            x_vals.append(x)
            y_vals.append(fx)

            if i == 0 or i == n:
                suma += fx
            else:
                suma += 2 * fx

        integral = (h / 2) * suma

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
    
        error = 0
    
        if tipo=="1/3 Simple":
    
            h=(b-a)/2
    
            integral=(h/3)*(
    
                self.evaluar_funcion(expr,a)
                +
                4*self.evaluar_funcion(expr,a+h)
                +
                self.evaluar_funcion(expr,b)
    
            )
    
        elif tipo=="1/3 Múltiple":
    
            if n%2!=0:
    
                raise ValueError(
                    "n debe ser par"
                )
    
            h=(b-a)/n
    
            suma=0
    
            for i in range(1,n):
    
                fx=self.evaluar_funcion(
                    expr,
                    a+i*h
                )
    
                if i%2:
    
                    suma+=4*fx
    
                else:
    
                    suma+=2*fx
    
            integral=(h/3)*(
    
                self.evaluar_funcion(expr,a)
                +
                suma
                +
                self.evaluar_funcion(expr,b)
    
            )
    
        elif tipo=="3/8 Simple":
    
            h=(b-a)/3
    
            integral=(3*h/8)*(
    
                self.evaluar_funcion(expr,a)
                +
                3*self.evaluar_funcion(expr,a+h)
                +
                3*self.evaluar_funcion(expr,a+2*h)
                +
                self.evaluar_funcion(expr,b)
    
            )
    
        elif tipo=="3/8 Compuesta":
    
            if n%3!=0:
    
                raise ValueError(
                    "n múltiplo de 3"
                )
    
            h=(b-a)/n
    
            suma=0
    
            for i in range(1,n):
    
                fx=self.evaluar_funcion(
                    expr,
                    a+i*h
                )
    
                if i%3==0:
    
                    suma+=2*fx
    
                else:
    
                    suma+=3*fx
    
            integral=(3*h/8)*(
    
                self.evaluar_funcion(expr,a)
                +
                suma
                +
                self.evaluar_funcion(expr,b)
    
            )
    
        error=abs(
    
            (
                integral_real
                -
                integral
            )
    
            /
    
            integral_real
    
        )*100
    
        return (
    
            integral,
            integral_real,
            error
    
        )
    
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
        self.status.set("")

        #---INTERPOLACIÓN LINEAL---
        if metodo == "Interpolación Lineal de Newton":
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(row=0, column=0)
        
            self.entry_x=ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x.grid(row=0, column=1)
        
            ttk.Label(
                self.frame_inputs,
                text="Valores f(x):"
            ).grid(row=1, column=0)
        
            self.entry_y=ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_y.grid(row=1, column=1)
        
            ttk.Label(
                self.frame_inputs,
                text="Incremento:"
            ).grid(row=2, column=0)
        
            self.entry_incremento=ttk.Entry(
                self.frame_inputs
            )
            self.entry_incremento.grid(row=2, column=1)
            self.entry_incremento.insert(0, "0.5")
        #---POLINOMIOS DE NEWTON---
        elif metodo == "Polinomios de Interpolación de Newton":
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(row=0, column=0)
            
            self.entry_x = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x.grid(row=0, column=1)
            
            ttk.Label(
                self.frame_inputs,
                text="Valores Y:"
            ).grid(row=1, column=0)
            
            self.entry_y = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_y.grid(row=1, column=1)
            
            ttk.Label(
                self.frame_inputs,
                text="x a interpolar:"
            ).grid(row=2, column=0)
            
            self.entry_xinterp = ttk.Entry(
                self.frame_inputs
            )
            self.entry_xinterp.grid(row=2, column=1)


        #---LAGRANGE---
        elif metodo == "Interpolación de Lagrange":
            ttk.Label(
                self.frame_inputs,
                text="Valores X:"
            ).grid(row=0, column=0)

            self.entry_x = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x.grid(row=0, column=1)

            ttk.Label(
                self.frame_inputs,
                text="Valores Y:"
            ).grid(row=1, column=0)

            self.entry_y = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_y.grid(row=1, column=1)

            ttk.Label(
                self.frame_inputs,
                text="Valor de x a interpolar:"
            ).grid(row=2, column=0)

            self.entry_xinterp = ttk.Entry(
                self.frame_inputs
            )
            self.entry_xinterp.grid(row=2, column=1)

        #---DIFERENCIAS FINITAS (DERIVACIÓN NUMÉRICA)---
        elif metodo == "Diferencias Finitas":
            ttk.Label(
                self.frame_inputs,
                text="Función f(x):"
            ).grid(row=0, column=0)

            self.entry_func = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_func.grid(row=0, column=1)

            ttk.Label(
                self.frame_inputs,
                text="Valor de x:"
            ).grid(row=1, column=0)

            self.entry_x_dif = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_x_dif.grid(row=1, column=1)

            ttk.Label(
                self.frame_inputs,
                text="Tamaño de paso (h):"
            ).grid(row=2, column=0)

            self.entry_h_dif = ttk.Entry(
                self.frame_inputs,
                width=40
            )
            self.entry_h_dif.grid(row=2, column=1)
            
        #---TRAPECIOS---
        elif metodo == "Método de Trapecios":
            for widget in self.frame_inputs.winfo_children():
                widget.destroy()

            ttk.Label(self.frame_inputs, text="Función f(x):").grid(row=0, column=0, sticky="w", padx=5, pady=2)
            self.entry_func = ttk.Entry(self.frame_inputs, width=40)
            self.entry_func.grid(row=0, column=1, padx=5, pady=2)

            ttk.Label(self.frame_inputs, text="Límite inferior (a):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=1, column=1, padx=5, pady=2)

            ttk.Label(self.frame_inputs, text="Límite superior (b):").grid(row=2, column=0, sticky="w", padx=5, pady=2)
            self.entry_b = ttk.Entry(self.frame_inputs)
            self.entry_b.grid(row=2, column=1, padx=5, pady=2)

            ttk.Label(self.frame_inputs, text="Número de trapecios (n):").grid(row=3, column=0, sticky="w", padx=5, pady=2)
            self.entry_n = ttk.Entry(self.frame_inputs)
            self.entry_n.grid(row=3, column=1, padx=5, pady=2)
            self.entry_n.insert(0, "4")

            self.status.set("Método de Trapecios cargado correctamente")
            return
            
        #---INTEGRACIÓN DE SIMPSON---
        elif metodo=="Método de Integración de Simpson":
            for widget in self.frame_inputs.winfo_children():
                widget.destroy()
        
            ttk.Label(self.frame_inputs, text="Función:").grid(row=0, column=0)
            self.entry_func = ttk.Entry(self.frame_inputs, width=35)
            self.entry_func.grid(row=0, column=1)
        
            ttk.Label(self.frame_inputs, text="a:").grid(row=1, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=1, column=1)
        
            ttk.Label(self.frame_inputs, text="b:").grid(row=2, column=0)
            self.entry_b = ttk.Entry(self.frame_inputs)
            self.entry_b.grid(row=2, column=1)
        
            ttk.Label(self.frame_inputs, text="Tipo:").grid(row=3, column=0)
        
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
            ).grid(row=3, column=1)
        
            ttk.Label(self.frame_inputs, text="n:").grid(row=4, column=0)
        
            self.entry_n = ttk.Entry(self.frame_inputs)
            self.entry_n.grid(row=4, column=1)
            self.entry_n.insert(0, "6")
        
            self.status.set("Simpson cargado correctamente")
            return

        
        #---FUNCIONES GENERALES---
        if metodo not in [
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            "Diferencias Finitas",
            "método de Trapecios",
            "Método de Integración de Simpson",
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
            

        #---TOLERANCIA---self.frame_inputs
        if metodo not in [
            "Búsqueda por Incrementos",
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            "Diferencias Finitas",
            "Método de Trapecios"
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
        

    #---EJECUTAR---
    def ejecutar_metodo(
        self
    ):
        try:
            metodo = self.metodo_var.get()
            tipo_error_sel = self.tipo_error_var.get()

            #---INTERPOLACIÓN LINEAL---
            if metodo == "Interpolación Lineal de Newton":
                x_tabla=list(
                    map(
                        float,
                        self.entry_x.get().split(",")
                    )
            
                )
            
                y_tabla=list(
            
                    map(
                        float,
                        self.entry_y.get().split(",")
                    )
            
                )
            
                incremento=float(
                    self.entry_incremento.get()
                )
            
                x0=x_tabla[0]
                y0=y_tabla[0]
            
                x1=x_tabla[-1]
                y1=y_tabla[-1]
            
                pendiente=(
            
                    y1-y0
            
                )/(
            
                    x1-x0
            
                )
            
                x=x0
            
                ex=[]
                ey=[]
            
                texto=""
            
                while x<=x1:
            
                    interp=y0+pendiente*(x-x0)
            
                    real=np.interp(
            
                        x,
                        x_tabla,
                        y_tabla
            
                    )
            
                    error=abs(
            
                        real-interp
            
                    )
            
                    texto+=(
                        f"x={x:.3f}"
                        f" interp={interp:.4f}"
                        f" error={error:.5f}\n"
                    )
            
                    ex.append(x)
                    ey.append(error)
            
                    x+=incremento
            
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
            
                self.text_resultados.insert(
                    tk.END,
                    texto
                )
            
                plt.figure(
                    "Error Interpolación"
                )
            
                plt.plot(
                    ex,
                    ey,
                    marker='o'
                )
            
                plt.grid(True)
            
                plt.xlabel("x")
            
                plt.ylabel(
                    "Error"
                )
            
                plt.show()

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
                
                plt.figure(
                    "Polinomios de Newton"
                )
                
                plt.scatter(
                    arreglo_x,
                    arreglo_y,
                    color='blue',
                    label='Puntos'
                )
                
                plt.plot(
                    x_interp,
                    resultado,
                    marker='o',
                    color='red',
                    label='Interpolación'
                )
                
                plt.title(
                    "Interpolación mediante Polinomios de Newton"
                )
                
                plt.xlabel(
                    "Eje X"
                )
                
                plt.ylabel(
                    "Eje Y"
                )
                
                plt.grid(
                    True
                )
                
                plt.legend()
                
                plt.show()

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

                plt.figure(
                    "Interpolación de Lagrange"
                )
                
                plt.scatter(
                    arreglo_x,
                    arreglo_y,
                    color='black',
                    label='Puntos Iniciales'
                )
                
                plt.plot(
                    valor,
                    resultado,
                    marker='*',
                    markersize=15,
                    color='magenta',
                    label='Punto Lagrange'
                )
                
                plt.title(
                    "Interpolación de Lagrange"
                )
                
                plt.xlabel(
                    "Valores X"
                )
                
                plt.ylabel(
                    "Valores Y"
                )
                
                plt.grid(
                    True,
                    linestyle='--'
                )
                
                plt.legend()
                
                plt.show()

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

                
                plt.figure(
                    "Derivación Numérica - Diferencias Finitas"
                )
                
                x_vals = np.linspace(
                    x - 2, 
                    x + 2, 
                    100
                )
                
                y_vals = [
                    self.evaluar_funcion(
                        expr, 
                        v
                    ) 
                    for v in x_vals
                ]
                
                punto_y = self.evaluar_funcion(
                    expr,
                    x
                )

                plt.plot(
                    x_vals,
                    y_vals,
                    color='blue',
                    label=f"f(x) = {expr}"
                )
                
                plt.plot(
                    x,
                    punto_y,
                    marker='o',
                    color='red',
                    label='Punto Evaluado'
                )

                plt.title(
                    "Función para Diferencias Finitas"
                )
                
                plt.xlabel(
                    "x"
                )
                
                plt.ylabel(
                    "f(x)"
                )
                
                plt.grid(
                    True,
                    alpha=0.5
                )
                
                plt.legend()
                
                plt.show()
            #---TRAPECIOS---
            elif metodo == "Método de Trapecios":
                try:
                    expr = self.entry_func.get()
                    a = float(self.entry_a.get())
                    b = float(self.entry_b.get())
                    n = int(self.entry_n.get())
  
                    resultado, x_vals, y_vals = self.metodo_trapecios(expr, a, b, n)
    
                    self.status.set("Cálculo completado exitosamente.")
                    
                    self.text_resultados.config(state="normal") # Desbloqueamos caja
                    self.text_resultados.delete("1.0", tk.END)  # Limpiamos contenido
                    
                    texto = (
                        f"--- RESULTADOS MÉTODO DE TRAPECIOS ---\n"
                        f"MÉTODO: {metodo}\n"
                        f"------------------------------\n"
                        f"Integral aproximada = {resultado:.8f}\n"
                        f"Intervalo: [{a}, {b}]\n"
                        f"Número de trapecios: {n}\n"
                    )
                    self.text_resultados.insert(tk.END, texto)
                    self.text_resultados.config(state="disabled") # Bloqueamos de nuevo
    
                    print(f"Resultado: {resultado}")
    
                    plt.figure("Método de Trapecios")
                    x_cont = np.linspace(a, b, 200)
                    y_cont = [self.evaluar_funcion(expr, x) for x in x_cont]
    
                    plt.plot(x_cont, y_cont, label='f(x)')
                    plt.plot(x_vals, y_vals, marker='o', linestyle='-', label='Trapecios')
    
                    for i in range(len(x_vals)-1):
                        plt.fill(
                            [x_vals[i], x_vals[i], x_vals[i+1], x_vals[i+1]],
                            [0, y_vals[i], y_vals[i+1], 0],
                            alpha=0.2
                        )
    
                    plt.title("Integración Numérica - Método de Trapecios")
                    plt.xlabel("x")
                    plt.ylabel("f(x)")
                    plt.grid(True)
                    plt.legend()
                    plt.show()
    
                except Exception as e:
                    self.status.set(f"Error en los datos de Trapecios: {str(e)}")

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

                plt.figure(
                    f"Convergencia - {metodo}"
                )
                
                plt.plot(
                    ex,
                    ey,
                    marker='s',
                    color='green',
                    linestyle='-.',
                    label=f'Error {tipo_error_sel}'
                )
                
                plt.title(
                    f"Gráfica de Error {tipo_error_sel}: {metodo}"
                )
                
                plt.xlabel(
                    "Número de Iteración"
                )
                
                plt.ylabel(
                    f"Magnitud de Error {tipo_error_sel}"
                )
                
                # ADAPTACIÓN DINÁMICA DEL EJE Y SÓLO PARA ERROR PORCENTUAL
                if tipo_error_sel == "Porcentual":
                    plt.yscale('log')
                
                plt.grid(
                    True,
                    which="both"
                )
                
                plt.legend()
                
                plt.show()
                
            #---INTEGRACIÓN DE SIMPSON---
            elif metodo == "Método de Integración de Simpson":
                try:
                    expr = self.entry_func.get()
                    a = float(self.entry_a.get())
                    b = float(self.entry_b.get())
                    tipo = self.tipo_simpson.get()
                    n = int(self.entry_n.get())
        
                    integral, integral_real, error = self.metodo_simpson(expr, a, b, tipo, n)
        
                    self.status.set("Cálculo completado exitosamente.")
                    
                    self.text_resultados.config(state="normal") 
                    self.text_resultados.delete("1.0", tk.END)
                    
                    texto_final = (
                        f"--- RESULTADOS MÉTODO DE SIMPSON ---\n"
                        f"Tipo seleccionado: {tipo}\n"
                        f"Valor de la Integral: {integral:.8f}\n"
                        f"Integral Real (Aprox.): {integral_real:.8f}\n"
                        f"Error Relativo: {error:.6f}%\n"
                    )
                    self.text_resultados.insert(tk.END, texto_final)
                    self.text_resultados.config(state="disabled")
                    
                    #---GRÁFICA SIMPSON---
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
                    
                    plt.figure(
                        "Método de Simpson"
                    )
                    
                    # Curva real
                    plt.plot(
                        x_func,
                        y_func,
                        color="blue",
                        linewidth=2,
                        label="f(x)"
                    )
                    
                    # Crear puntos según el tipo
                    if tipo=="1/3 Simple":
                    
                        x_pts=np.linspace(
                            a,
                            b,
                            3
                        )
                    
                    elif tipo=="3/8 Simple":
                    
                        x_pts=np.linspace(
                            a,
                            b,
                            4
                        )
                    
                    else:
                    
                        x_pts=np.linspace(
                            a,
                            b,
                            n+1
                        )
                    
                    y_pts=[
                    
                        self.evaluar_funcion(
                            expr,
                            x
                        )
                    
                        for x in x_pts
                    
                    ]
                    
                    # Puntos Simpson
                    plt.plot(
                    
                        x_pts,
                        y_pts,
                    
                        marker='o',
                        linewidth=2,
                    
                        label=tipo
                    
                    )
                    
                    # Líneas divisorias
                    for x in x_pts:
                    
                        plt.axvline(
                    
                            x,
                    
                            linestyle="--",
                    
                            alpha=0.4,
                    
                            color="gray"
                    
                        )
                    
                    # Área aproximada
                    plt.fill_between(
                    
                        x_func,
                        y_func,
                    
                        alpha=0.2
                    
                    )
                    
                    plt.xlabel("x")
                    
                    plt.ylabel("f(x)")
                    
                    plt.title(
                        f"Integración Simpson {tipo}"
                    )
                    
                    plt.grid(True)
                    
                    plt.legend()
                    
                    plt.show()
                    
                    print(f"Resultado: {integral}, Error: {error}") 
                                        
                except Exception as e:
                    self.status.set(f"Error en los datos: {str(e)}")

            #---MÉTODOS RESTANTES (Ajuste y Búsqueda)---
            else:
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                self.text_resultados.insert(
                    tk.END,
                    f"Método {metodo} en construcción o sin interfaz de ploteo extendida configurada."
                )

        except Exception as e:
            messagebox.showerror(
                "Error en la Ejecución",
                f"Ha ocurrido un problema:\n{str(e)}"
            )

#---INICIO DE LA APLICACIÓN---
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    
    app = MetodosNumericosApp(
        ventana_principal
    )
    
    ventana_principal.mainloop()