# ------------------ IMPORTACIONES ------------------
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math

# ------------------ CLASE PRINCIPAL ------------------
class MetodosNumericosApp:
    VERSION = "v1.4.0"

    def __init__(self, root):
        self.root = root
        self.root.title(f"Suite de Métodos Numéricos {self.VERSION}")
        self.root.geometry("900x550")

        self.crear_layout()
        self.crear_statusbar()

    # ------------------ INTERFAZ ------------------
    def crear_layout(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Panel izquierdo
        self.panel_control = ttk.LabelFrame(self.main_frame, text="Configuración")
        self.panel_control.pack(side="left", fill="y", padx=5, pady=5)

        ttk.Label(self.panel_control, text="Método:").pack(pady=5)

        self.metodo_var = tk.StringVar()

        self.combo_metodos = ttk.Combobox(
            self.panel_control,
            textvariable=self.metodo_var,
            state="readonly"
        )

        # MÉTODOS DISPONIBLES
        self.combo_metodos['values'] = [
            "Bisección",
            "Falsa Posición",
            "Newton Raphson",
            "Secante",
            "Punto Fijo"
        ]

        self.combo_metodos.pack(pady=5)

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

        # Panel derecho
        self.panel_trabajo = ttk.Frame(self.main_frame)
        self.panel_trabajo.pack(side="right", fill="both", expand=True)

        self.frame_inputs = ttk.LabelFrame(self.panel_trabajo, text="Entradas")
        self.frame_inputs.pack(fill="x", padx=5, pady=5)

        self.frame_resultados = ttk.LabelFrame(self.panel_trabajo, text="Resultados")
        self.frame_resultados.pack(fill="both", expand=True, padx=5, pady=5)

        self.text_resultados = tk.Text(self.frame_resultados, height=10)
        self.text_resultados.pack(fill="both", expand=True)

    def crear_statusbar(self):
        self.status = tk.StringVar(value="Listo")

        ttk.Label(
            self.root,
            textvariable=self.status,
            relief="sunken"
        ).pack(fill="x", side="bottom")

    # ------------------ EVALUACIÓN DE FUNCIONES ------------------
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

            return eval(expr, {"__builtins__": {}}, permitido)

        except Exception as e:
            raise ValueError(f"Error en la expresión: {e}")

    # ------------------ MÉTODO BISECCIÓN ------------------
    def metodo_biseccion(self, expr, a, b, erra):
        ejex, ejey = [], []

        n = 0
        error = abs(a - b)

        while error > erra:
            pi = (b + a) / 2

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

    # ------------------ MÉTODO FALSA POSICIÓN ------------------
    def metodo_falsa_posicion(self, expr, a, b, erra):
        ejex, ejey = [], []

        iteracion = 0
        xr_anterior = a
        error = 100

        while error > erra:
            fa = self.evaluar_funcion(expr, a)
            fb = self.evaluar_funcion(expr, b)

            xr = a - (fa * (b - a)) / (fb - fa)

            fxr = self.evaluar_funcion(expr, xr)

            if iteracion > 0:
                error = abs((xr - xr_anterior) / xr)

            if fa * fxr < 0:
                b = xr
            else:
                a = xr

            xr_anterior = xr

            iteracion += 1

            ejex.append(iteracion)
            ejey.append(error)

        return xr, error, ejex, ejey

    # ------------------ MÉTODO NEWTON RAPHSON ------------------
    def metodo_newton_raphson(self, fun, fprima, Xi, erra):
        ejex, ejey = [], []

        error = 100
        n = 0

        while error > erra:
            fxi = self.evaluar_funcion(fun, Xi)
            fpxi = self.evaluar_funcion(fprima, Xi)

            if fpxi == 0:
                break

            Xn = Xi - (fxi / fpxi)

            error = abs((Xn - Xi) / Xn)

            Xi = Xn

            n += 1

            ejex.append(n)
            ejey.append(error)

        return Xi, error, ejex, ejey

    # ------------------ MÉTODO SECANTE ------------------
    def metodo_secante(self, expr, x0, x1, erra):
        ejex, ejey = [], []

        error = 100
        n = 0

        while error > erra and n < 100:
            fx0 = self.evaluar_funcion(expr, x0)
            fx1 = self.evaluar_funcion(expr, x1)

            if (fx1 - fx0) == 0:
                break

            x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)

            error = abs((x2 - x1) / x2) if x2 != 0 else 0

            x0, x1 = x1, x2

            n += 1

            ejex.append(n)
            ejey.append(error)

        return x1, error, ejex, ejey

    # ------------------ MÉTODO PUNTO FIJO ------------------
    def metodo_punto_fijo(self, gx, x0, erra):
        ejex, ejey = [], []

        error = 100
        n = 0

        while error > erra and n < 100:
            x1 = self.evaluar_funcion(gx, x0)

            error = abs((x1 - x0) / x1) if x1 != 0 else 0

            x0 = x1

            n += 1

            ejex.append(n)
            ejey.append(error)

        return x1, error, ejex, ejey

    # ------------------ CONTROLADOR DE INTERFAZ ------------------
    def cargar_metodo(self):

        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        metodo = self.metodo_var.get()

        if not metodo:
            return

        # Campo común
        ttk.Label(self.frame_inputs, text="Función:").grid(
            row=0,
            column=0,
            padx=5
        )

        self.entry_func = ttk.Entry(self.frame_inputs, width=30)
        self.entry_func.grid(row=0, column=1)

        # ------------------ NEWTON ------------------
        if metodo == "Newton Raphson":

            ttk.Label(
                self.frame_inputs,
                text="f'(x):"
            ).grid(row=1, column=0)

            self.entry_fprima = ttk.Entry(self.frame_inputs, width=30)
            self.entry_fprima.grid(row=1, column=1)

            ttk.Label(
                self.frame_inputs,
                text="x0 (Inicial):"
            ).grid(row=2, column=0)

            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=2, column=1)

        # ------------------ SECANTE ------------------
        elif metodo == "Secante":

            ttk.Label(
                self.frame_inputs,
                text="x0 (Punto 1):"
            ).grid(row=1, column=0)

            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=1, column=1)

            ttk.Label(
                self.frame_inputs,
                text="x1 (Punto 2):"
            ).grid(row=2, column=0)

            self.entry_b = ttk.Entry(self.frame_inputs)
            self.entry_b.grid(row=2, column=1)

        # ------------------ PUNTO FIJO ------------------
        elif metodo == "Punto Fijo":

            ttk.Label(
                self.frame_inputs,
                text="x0 (Inicial):"
            ).grid(row=1, column=0)

            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=1, column=1)

        # ------------------ BISECCIÓN Y FALSA POSICIÓN ------------------
        elif metodo in ["Bisección", "Falsa Posición"]:

            ttk.Label(
                self.frame_inputs,
                text="Límite a:"
            ).grid(row=1, column=0)

            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=1, column=1)

            ttk.Label(
                self.frame_inputs,
                text="Límite b:"
            ).grid(row=2, column=0)

            self.entry_b = ttk.Entry(self.frame_inputs)
            self.entry_b.grid(row=2, column=1)

        # ------------------ ERROR ------------------
        ttk.Label(
            self.frame_inputs,
            text="Tolerancia:"
        ).grid(row=3, column=0)

        self.entry_error = ttk.Entry(self.frame_inputs)
        self.entry_error.grid(row=3, column=1)

        self.entry_error.insert(0, "0.0001")

        self.status.set(f"Configuración para {metodo} cargada")

    # ------------------ EJECUCIÓN ------------------
    def ejecutar_metodo(self):

        try:
            expr = self.entry_func.get()

            erra = float(self.entry_error.get())

            metodo = self.metodo_var.get()

            # ------------------ BISECCIÓN ------------------
            if metodo == "Bisección":

                a = float(self.entry_a.get())
                b = float(self.entry_b.get())

                res, err, ex, ey = self.metodo_biseccion(
                    expr,
                    a,
                    b,
                    erra
                )

            # ------------------ FALSA POSICIÓN ------------------
            elif metodo == "Falsa Posición":

                a = float(self.entry_a.get())
                b = float(self.entry_b.get())

                res, err, ex, ey = self.metodo_falsa_posicion(
                    expr,
                    a,
                    b,
                    erra
                )

            # ------------------ NEWTON ------------------
            elif metodo == "Newton Raphson":

                x0 = float(self.entry_a.get())

                f_der = self.entry_fprima.get()

                res, err, ex, ey = self.metodo_newton_raphson(
                    expr,
                    f_der,
                    x0,
                    erra
                )

            # ------------------ SECANTE ------------------
            elif metodo == "Secante":

                x0 = float(self.entry_a.get())
                x1 = float(self.entry_b.get())

                res, err, ex, ey = self.metodo_secante(
                    expr,
                    x0,
                    x1,
                    erra
                )

            # ------------------ PUNTO FIJO ------------------
            elif metodo == "Punto Fijo":

                x0 = float(self.entry_a.get())

                res, err, ex, ey = self.metodo_punto_fijo(
                    expr,
                    x0,
                    erra
                )

            # ------------------ RESULTADOS ------------------
            self.text_resultados.delete(1.0, tk.END)

            self.text_resultados.insert(
                tk.END,
                f"MÉTODO: {metodo}\n"
                + "-" * 30
                + f"\nRaíz estimada: {res}"
                + f"\nError final: {err}"
                + f"\nIteraciones: {len(ex)}"
            )

            # ------------------ GRÁFICA ------------------
            plt.figure("Análisis de Convergencia")

            plt.plot(ex, ey, marker='o', color='red')

            plt.title(f"Caída del Error - {metodo}")

            plt.xlabel("Iteración")
            plt.ylabel("Error")

            plt.grid(True)

            plt.show()

            self.status.set("Ejecución exitosa")

        except Exception as e:
            messagebox.showerror("Error", f"Detalle: {e}")

# ------------------ MAIN ------------------
if __name__ == "__main__":

    root = tk.Tk()

    app = MetodosNumericosApp(root)

    root.mainloop()