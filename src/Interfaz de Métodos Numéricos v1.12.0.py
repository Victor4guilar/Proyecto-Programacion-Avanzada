#---IMPORTACIONES---
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math
import numpy as np

#---CLASE PRINCIPAL---
class MetodosNumericosApp:
    VERSION = "v1.12,0"
    
    def __init__(
        self,
        root
    ):
        self.root = root
        
        self.root.title(
            f"Suite de Métodos Numéricos {self.VERSION}"
        )
        
        self.root.geometry(
            "950x600"
        )
        
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
        
        self.combo_metodos = ttk.Combobox(
            self.panel_control,
            textvariable=self.metodo_var,
            state="readonly",
            width=35
        )

        #---MÉTODOS DISPONIBLES---
        self.combo_metodos['values'] = [
            "───── Raíces Cerradas ─────",
            "Bisección",
            "Falsa Posición",
            "Búsqueda por Incrementos",
            
            "───── Raíces Abiertas ─────",
            "Newton Raphson",
            "Secante",
            "Punto Fijo",
            
            "───── Ajuste de Curvas ─────",
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            
            "───── Derivación Numérica ─────",
            "Diferencias Finitas"
            "───── Integración Numérica ─────",
            "Método de Trapecios"
        ]
        
        self.combo_metodos.pack(
            pady=5
        )
        
        self.combo_metodos.bind(
            "<<ComboboxSelected>>",
            self.validar_metodo
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

    #---BISECCIÓN---
    def metodo_biseccion(
        self,
        expr,
        a,
        b,
        erra
    ):
        ejex, ejey = [], []
        n = 0
        error = abs(
            a - b
        )
        
        while error > erra:
            pi = (
                a + b
            ) / 2
            
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
                
            error = abs(
                a - b
            )
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
        erra
    ):
        ejex, ejey = [], []
        iteracion = 0
        xr_anterior = a
        error = 100
        
        while error > erra:
            fa = self.evaluar_funcion(
                expr,
                a
            )
            fb = self.evaluar_funcion(
                expr,
                b
            )
            
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
                error = abs(
                    (
                        xr - xr_anterior
                    ) / xr
                )
                
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
        erra
    ):
        ejex, ejey = [], []
        error = 100
        n = 0
        
        while error > erra:
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
            
            error = abs(
                (
                    Xn - Xi
                ) / Xn
            )
            
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
        erra
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
            
            error = abs(
                (
                    x2 - x1
                ) / x2
            ) if x2 != 0 else 0
            
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
        erra
    ):
        ejex, ejey = [], []
        error = 100
        n = 0
        
        while error > erra and n < 100:
            x1 = self.evaluar_funcion(
                gx,
                x0
            )
            
            error = abs(
                (
                    x1 - x0
                ) / x1
            ) if x1 != 0 else 0
            
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

        #---INTERPOLACIÓN LINEAL---
        if metodo == "Interpolación Lineal de Newton":
            ttk.Label(
                self.frame_inputs,
                text="x0:"
            ).grid(
                row=0, 
                column=0
            )
            
            self.entry_x0 = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_x0.grid(
                row=0,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="y0:"
            ).grid(
                row=1, 
                column=0
            )
            
            self.entry_y0 = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_y0.grid(
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
            
            self.entry_x1 = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_x1.grid(
                row=2,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="y1:"
            ).grid(
                row=3, 
                column=0
            )
            
            self.entry_y1 = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_y1.grid(
                row=3,
                column=1
            )
            
            ttk.Label(
                self.frame_inputs,
                text="x a interpolar:"
            ).grid(
                row=4, 
                column=0
            )
            
            self.entry_xi = ttk.Entry(
                self.frame_inputs
            )
            
            self.entry_xi.grid(
                row=4,
                column=1
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
                text="Límite inferior (a):"
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
                text="Límite superior (b):"
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
                text="Número de trapecios (n):"
            ).grid(
                row=3,
                column=0
            )

            self.entry_n = ttk.Entry(
                self.frame_inputs
            )

            self.entry_n.grid(
                row=3,
                column=1
            )

            self.entry_n.insert(
                0,
                "4"
            )
        #---FUNCIONES GENERALES---
        if metodo not in [
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton",
            "Interpolación de Lagrange",
            "Diferencias Finitas"
            "método de Trapecios"
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
            "Diferencias Finitas"
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

            #---INTERPOLACIÓN LINEAL---
            if metodo == "Interpolación Lineal de Newton":
                x0 = float(
                    self.entry_x0.get()
                )
                
                y0 = float(
                    self.entry_y0.get()
                )
                
                x1 = float(
                    self.entry_x1.get()
                )
                
                y1 = float(
                    self.entry_y1.get()
                )
                
                xi = float(
                    self.entry_xi.get()
                )
                
                resultado, b1 = self.metodo_interpolacion_newton(
                    x0,
                    y0,
                    x1,
                    y1,
                    xi
                )
                
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nPendiente: {b1}"
                    + f"\nResultado: {resultado}"
                )
                
                self.text_resultados.insert(
                    tk.END,
                    texto
                )
                
                plt.figure(
                    "Interpolación Lineal"
                )
                
                plt.plot(
                    [
                        x0, 
                        x1
                    ],
                    [
                        y0, 
                        y1
                    ],
                    marker='o',
                    linestyle='-',
                    color='blue',
                    label='Puntos Conocidos'
                )
                
                plt.plot(
                    xi,
                    resultado,
                    marker='x',
                    markersize=10,
                    color='red',
                    label='Interpolación'
                )
                
                plt.title(
                    "Interpolación Lineal de Newton"
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

                # Graficar la función original y el punto
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
                expr = self.entry_func.get()

                a = float(
                    self.entry_a.get()
                )

                b = float(
                    self.entry_b.get()
                )

                n = int(
                    self.entry_n.get()
                )

                resultado, x_vals, y_vals = self.metodo_trapecios(
                    expr,
                    a,
                    b,
                    n
                )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )

                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nIntegral aproximada = {resultado}\n"
                    + f"Intervalo: [{a}, {b}]"
                    + f"\nNúmero de trapecios: {n}\n"
                )

                self.text_resultados.insert(
                    tk.END,
                    texto
                )

                # Graficar
                plt.figure(
                    "Método de Trapecios"
                )

                x_cont = np.linspace(
                    a,
                    b,
                    200
                )

                y_cont = [
                    self.evaluar_funcion(expr, x)
                    for x in x_cont
                ]

                plt.plot(
                    x_cont,
                    y_cont,
                    label='f(x)'
                )

                plt.plot(
                    x_vals,
                    y_vals,
                    marker='o',
                    linestyle='-',
                    label='Trapecios'
                )

                for i in range(len(x_vals)-1):
                    plt.fill(
                        [
                            x_vals[i],
                            x_vals[i],
                            x_vals[i+1],
                            x_vals[i+1]
                        ],
                        [
                            0,
                            y_vals[i],
                            y_vals[i+1],
                            0
                        ],
                        alpha=0.2
                    )

                plt.title(
                    "Integración Numérica - Método de Trapecios"
                )

                plt.xlabel(
                    "x"
                )

                plt.ylabel(
                    "f(x)"
                )

                plt.grid(
                    True
                )

                plt.legend()

                plt.show()

            #---MÉTODOS DE RAÍCES (General)---
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
                        erra
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
                        erra
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
                        erra
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
                        erra
                    )

                elif metodo == "Punto Fijo":
                    x0 = float(
                        self.entry_a.get()
                    )
                    
                    raiz, err, ex, ey = self.metodo_punto_fijo(
                        expr, 
                        x0, 
                        erra
                    )

                self.text_resultados.delete(
                    1.0,
                    tk.END
                )
                
                texto = (
                    f"MÉTODO: {metodo}\n"
                    + "-" * 30
                    + f"\nRaíz encontrada: {raiz}\n"
                    + f"Error Final: {err}\n"
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
                    label='Error Relativo'
                )
                
                plt.title(
                    f"Gráfica de Error: {metodo}"
                )
                
                plt.xlabel(
                    "Número de Iteración"
                )
                
                plt.ylabel(
                    "Magnitud de Error"
                )
                
                plt.grid(
                    True,
                    which="both"
                )
                
                plt.legend()
                
                plt.show()

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