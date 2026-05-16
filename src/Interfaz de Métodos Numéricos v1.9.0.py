#---IMPORTACIONES---
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math
import numpy as np

#---CLASE PRINCIPAL---
class MetodosNumericosApp:
    VERSION = "v1.9.0"
    def __init__(self, root):
        self.root = root
        self.root.title(f"Suite de Métodos Numéricos {self.VERSION}")
        self.root.geometry("950x600")
        self.crear_layout()
        self.crear_statusbar()

    #---INTERFAZ---
    def crear_layout(self):
        self.main_frame = ttk.Frame(self.root)
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
        ).pack(pady=5)
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
            "Polinomios de Interpolación de Newton"
        ]
        self.combo_metodos.pack(pady=5)
        self.combo_metodos.bind(
            "<<ComboboxSelected>>",
            self.validar_metodo
        )
        ttk.Button(
            self.panel_control,
            text="Cargar Método",
            command=self.cargar_metodo
        ).pack(pady=10)
        ttk.Button(
            self.panel_control,
            text="Ejecutar",
            command=self.ejecutar_metodo
        ).pack(pady=5)

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
    def crear_statusbar(self):

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
    def validar_metodo(self, event=None):
        metodo = self.metodo_var.get()
        if "────" in metodo:
            self.combo_metodos.set("")
            self.status.set(
                "Seleccione un método válido"
            )

    #---EVALUAR FUNCIONES---
    def evaluar_funcion(self, expr, x):
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
        error = abs(a - b)
        while error > erra:
            pi = (a + b) / 2
            fa = self.evaluar_funcion(expr, a)
            fpi = self.evaluar_funcion(expr, pi)
            if fa * fpi <= 0:
                b = pi
            else:
                a = pi
            error = abs(a - b)
            n += 1
            ejex.append(n)
            ejey.append(error)
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
            fa = self.evaluar_funcion(expr, a)
            fb = self.evaluar_funcion(expr, b)
            xr = a - (
                fa * (b - a)
            ) / (
                fb - fa
            )
            fxr = self.evaluar_funcion(expr, xr)
            if iteracion > 0:
                error = abs(
                    (xr - xr_anterior) / xr
                )
            if fa * fxr < 0:
                b = xr
            else:
                a = xr
            xr_anterior = xr
            iteracion += 1
            ejex.append(iteracion)
            ejey.append(error)
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
            Xn = Xi - (fxi / fpxi)
            error = abs(
                (Xn - Xi) / Xn
            )
            Xi = Xn
            n += 1
            ejex.append(n)
            ejey.append(error)
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
                fx1 * (x1 - x0)
            ) / (
                fx1 - fx0
            )
            error = abs(
                (x2 - x1) / x2
            ) if x2 != 0 else 0
            x0, x1 = x1, x2
            n += 1
            ejex.append(n)
            ejey.append(error)
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
                (x1 - x0) / x1
            ) if x1 != 0 else 0
            x0 = x1
            n += 1
            ejex.append(n)
            ejey.append(error)
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
            ejex.append(x)
            ejey.append(fx)
            if fx * fx_sig < 0:
                intervalos.append(
                    (x, x_sig)
                )
            x = x_sig
        return intervalos, ejex, ejey

    #---MÍNIMOS CUADRADOS LINEALES---
    def metodo_minimos_cuadrados(
        self,
        arreglo_x,
        arreglo_y
    ):
        suma_X = sum(arreglo_x)
        suma_Y = sum(arreglo_y)
        suma_XY = sum(
            arreglo_x[i] * arreglo_y[i]
            for i in range(
                len(arreglo_x)
            )
        )
        suma_X2 = sum(
            arreglo_x[i] ** 2
            for i in range(
                len(arreglo_x)
            )
        )
        n = len(arreglo_x)
        a = (
            (n * suma_XY)
            - (suma_X * suma_Y)
        ) / (
            (n * suma_X2)
            - (suma_X ** 2)
        )
        b = (
            (suma_X * suma_XY)
            - (suma_Y * suma_X2)
        ) / (
            (suma_X ** 2)
            - (n * suma_X2)
        )
        eje_y = []
        for i in range(len(arreglo_x)):
            funcion = (
                (a * arreglo_x[i]) + b
            )
            eje_y.append(funcion)
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
            b1 * (x_interp - x0)
        )
        return resultado, b1

    #---POLINOMIOS DE INTERPOLACIÓN DE NEWTON---
    def metodo_polinomios_newton(
        self,
        arreglo_x,
        arreglo_y,
        x_interp
    ):
        n = len(arreglo_x)
        tabla = [
            [0 for j in range(n)]
            for i in range(n)
        ]
        for i in range(n):
            tabla[i][0] = arreglo_y[i]
        for j in range(1, n):
            for i in range(n - j):
                tabla[i][j] = (
                    tabla[i + 1][j - 1]
                    - tabla[i][j - 1]
                ) / (
                    arreglo_x[i + j]
                    - arreglo_x[i]
                )
        coeficientes = [
            tabla[0][i]
            for i in range(n)
        ]
        resultado = coeficientes[0]
        producto = 1
        for i in range(1, n):
            producto *= (
                x_interp
                - arreglo_x[i - 1]
            )
            resultado += (
                coeficientes[i]
                * producto
            )
        return resultado, coeficientes, tabla

    #---CARGAR MÉTODO---
    def cargar_metodo(self):
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
            ).grid(row=0, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)
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
            ).grid(row=3, column=0)
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
            ).grid(row=4, column=0)
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
            ).grid(row=0, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)
            self.entry_xinterp = ttk.Entry(
                self.frame_inputs
            )
            self.entry_xinterp.grid(
                row=2,
                column=1
            )

        #---FUNCIONES---
        if metodo not in [
            "Mínimos Cuadrados Lineales",
            "Mínimos Cuadrados Polinomiales",
            "Interpolación Lineal de Newton",
            "Polinomios de Interpolación de Newton"
        ]:
            ttk.Label(
                self.frame_inputs,
                text="Función:"
            ).grid(row=0, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)

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
            ).grid(row=3, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)
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
                ).grid(row=3, column=0)
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
            ).grid(row=1, column=0)
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
            ).grid(row=2, column=0)
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
            "Polinomios de Interpolación de Newton"
        ]:
            ttk.Label(
                self.frame_inputs,
                text="Tolerancia:"
            ).grid(row=3, column=0)
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
    def ejecutar_metodo(self):
        try:
            metodo = self.metodo_var.get()

            #---INTERPOLACIÓN LINEAL---
            if metodo == "Interpolación Lineal de Newton":
                x0 = float(self.entry_x0.get())
                y0 = float(self.entry_y0.get())
                x1 = float(self.entry_x1.get())
                y1 = float(self.entry_y1.get())
                xi = float(self.entry_xi.get())
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
                plt.figure("Interpolación")
                plt.plot(
                    [x0, x1],
                    [y0, y1],
                    marker='o'
                )
                plt.plot(
                    xi,
                    resultado,
                    marker='x',
                    markersize=10
                )
                plt.grid(True)
                plt.show()

            #---POLINOMIOS DE NEWTON---
            elif metodo == "Polinomios de Interpolación de Newton":
                arreglo_x = list(
                    map(
                        float,
                        self.entry_x.get().split(",")
                    )
                )
                arreglo_y = list(
                    map(
                        float,
                        self.entry_y.get().split(",")
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
                for i, coef in enumerate(coeficientes):
                    texto += (
                        f"b{i} = {coef}\n"
                    )
                texto += (
                    f"\nResultado interpolado:"
                    f"\nf({x_interp}) = {resultado}\n"
                )
                texto += (
                    "\nTabla de diferencias divididas:\n"
                )
                for i in range(len(tabla)):
                    for j in range(
                        len(tabla) - i
                    ):
                        texto += (
                            f"{tabla[i][j]:.6f}\t"
                        )
                    texto += "\n"
                self.text_resultados.insert(
                    tk.END,
                    texto
                )
                plt.figure(
                    "Polinomios de Newton"
                )
                plt.scatter(
                    arreglo_x,
                    arreglo_y
                )
                x_suave = np.linspace(
                    min(arreglo_x),
                    max(arreglo_x),
                    200
                )
                y_suave = []
                for xv in x_suave:
                    yv = coeficientes[0]
                    producto = 1
                    for i in range(
                        1,
                        len(coeficientes)
                    ):
                        producto *= (
                            xv
                            - arreglo_x[i - 1]
                        )
                        yv += (
                            coeficientes[i]
                            * producto
                        )
                    y_suave.append(yv)
                plt.plot(
                    x_suave,
                    y_suave
                )
                plt.scatter(
                    x_interp,
                    resultado,
                    marker='x',
                    s=100
                )
                plt.grid(True)
                plt.show()
            elif metodo != "Mínimos Cuadrados Lineales" and metodo != "Mínimos Cuadrados Polinomiales":
                expr = self.entry_func.get()

            #---BISECCIÓN---
            if metodo == "Bisección":
                erra = float(
                    self.entry_error.get()
                )
                a = float(
                    self.entry_a.get()
                )
                b = float(
                    self.entry_b.get()
                )
                res, err, ex, ey = self.metodo_biseccion(
                    expr,
                    a,
                    b,
                    erra
                )

            #---FALSA POSICIÓN---
            elif metodo == "Falsa Posición":
                erra = float(
                    self.entry_error.get()
                )
                a = float(
                    self.entry_a.get()
                )
                b = float(
                    self.entry_b.get()
                )
                res, err, ex, ey = self.metodo_falsa_posicion(
                    expr,
                    a,
                    b,
                    erra
                )

            #---NEWTON---
            elif metodo == "Newton Raphson":
                erra = float(
                    self.entry_error.get()
                )
                x0 = float(
                    self.entry_a.get()
                )
                fprima = self.entry_fprima.get()
                res, err, ex, ey = self.metodo_newton_raphson(
                    expr,
                    fprima,
                    x0,
                    erra
                )

            #---SECANTE---
            elif metodo == "Secante":
                erra = float(
                    self.entry_error.get()
                )
                x0 = float(
                    self.entry_a.get()
                )
                x1 = float(
                    self.entry_b.get()
                )
                res, err, ex, ey = self.metodo_secante(
                    expr,
                    x0,
                    x1,
                    erra
                )

            #---PUNTO FIJO---
            elif metodo == "Punto Fijo":
                erra = float(
                    self.entry_error.get()
                )
                x0 = float(
                    self.entry_a.get()
                )
                res, err, ex, ey = self.metodo_punto_fijo(
                    expr,
                    x0,
                    erra
                )

            #---BÚSQUEDA---
            elif metodo == "Búsqueda por Incrementos":
                xi = float(
                    self.entry_a.get()
                )
                xf = float(
                    self.entry_b.get()
                )
                incremento = float(
                    self.entry_incremento.get()
                )
                intervalos, ex, ey = self.metodo_busqueda_incrementos(
                    expr,
                    xi,
                    xf,
                    incremento
                )

            #---MÍNIMOS CUADRADOS LINEALES---
            elif metodo == "Mínimos Cuadrados Lineales":
                arreglo_x = list(
                    map(
                        float,
                        self.entry_x.get().split(",")
                    )
                )
                arreglo_y = list(
                    map(
                        float,
                        self.entry_y.get().split(",")
                    )
                )
                a, b, eje_y = self.metodo_minimos_cuadrados(
                    arreglo_x,
                    arreglo_y
                )

            #---MÍNIMOS CUADRADOS POLINOMIALES---
            elif metodo == "Mínimos Cuadrados Polinomiales":
                arreglo_x = list(
                    map(
                        float,
                        self.entry_x.get().split(",")
                    )
                )
                arreglo_y = list(
                    map(
                        float,
                        self.entry_y.get().split(",")
                    )
                )
                grado = int(
                    self.entry_grado.get()
                )
                coeficientes, eje_y = self.metodo_minimos_cuadrados_polinomiales(
                    arreglo_x,
                    arreglo_y,
                    grado
                )

            #---RESULTADOS---
            if metodo not in [
                "Interpolación Lineal de Newton",
                "Polinomios de Interpolación de Newton"
            ]:
                self.text_resultados.delete(
                    1.0,
                    tk.END
                )

                #---BÚSQUEDA---
                if metodo == "Búsqueda por Incrementos":
                    texto = (
                        f"MÉTODO: {metodo}\n"
                        + "-" * 30
                        + "\nIntervalos encontrados:\n\n"
                    )
                    if intervalos:
                        for i, intervalo in enumerate(
                            intervalos,
                            start=1
                        ):
                            texto += (
                                f"Raíz {i}: "
                                f"[{intervalo[0]:.6f}, "
                                f"{intervalo[1]:.6f}]\n"
                            )
                    else:
                        texto += (
                            "No se encontraron raíces"
                        )
                    self.text_resultados.insert(
                        tk.END,
                        texto
                    )

                #---LINEALES---
                elif metodo == "Mínimos Cuadrados Lineales":
                    texto = (
                        f"MÉTODO: {metodo}\n"
                        + "-" * 30
                        + f"\nPendiente (a): {a}"
                        + f"\nIntercepto (b): {b}"
                        + f"\n\nRecta Ajustada:"
                        + f"\ny = {a}x + {b}"
                    )
                    self.text_resultados.insert(
                        tk.END,
                        texto
                    )

                #---POLINOMIALES---
                elif metodo == "Mínimos Cuadrados Polinomiales":
                    funcion = ""
                    grado_actual = grado
                    for coef in coeficientes:
                        if grado_actual > 1:
                            funcion += (
                                f"{coef:.4f}x^{grado_actual} + "
                            )

                        elif grado_actual == 1:
                            funcion += (
                                f"{coef:.4f}x + "
                            )

                        else:
                            funcion += (
                                f"{coef:.4f}"
                            )
                        grado_actual -= 1
                    texto = (
                        f"MÉTODO: {metodo}\n"
                        + "-" * 30
                        + f"\nCoeficientes:\n{coeficientes}"
                        + f"\n\nPolinomio Ajustado:"
                        + f"\ny = {funcion}"
                    )
                    self.text_resultados.insert(
                        tk.END,
                        texto
                    )

                #---RAÍCES---
                else:
                    texto = (
                        f"MÉTODO: {metodo}\n"
                        + "-" * 30
                        + f"\nRaíz estimada: {res}"
                        + f"\nError final: {err}"
                        + f"\nIteraciones: {len(ex)}"
                    )
                    self.text_resultados.insert(
                        tk.END,
                        texto
                    )

                #---GRÁFICAS---
                if metodo == "Búsqueda por Incrementos":
                    plt.figure("Búsqueda")
                    plt.plot(
                        ex,
                        ey,
                        marker='o'
                    )
                    plt.axhline(0)
                    plt.grid(True)
                    
                elif metodo == "Mínimos Cuadrados Lineales":
                    plt.figure(
                        "Mínimos Cuadrados"
                    )
                    plt.scatter(
                        arreglo_x,
                        arreglo_y
                    )
                    plt.plot(
                        arreglo_x,
                        eje_y
                    )
                    plt.grid(True)

                elif metodo == "Mínimos Cuadrados Polinomiales":
                    plt.figure(
                        "Mínimos Cuadrados Polinomiales"
                    )
                    plt.scatter(
                        arreglo_x,
                        arreglo_y
                    )
                    x_suave = np.linspace(
                        min(arreglo_x),
                        max(arreglo_x),
                        200
                    )
                    polinomio = np.poly1d(
                        coeficientes
                    )
                    y_suave = polinomio(
                        x_suave
                    )
                    plt.plot(
                        x_suave,
                        y_suave
                    )
                    plt.grid(True)

                else:
                    plt.figure(
                        "Convergencia"
                    )
                    plt.plot(
                        ex,
                        ey,
                        marker='o'
                    )
                    plt.grid(True)
                    
                plt.show()
            self.status.set(
                "Ejecución exitosa"
            )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Detalle: {e}"
            )

#---MAIN---
if __name__ == "__main__":
    root = tk.Tk()
    app = MetodosNumericosApp(root)
    root.mainloop()