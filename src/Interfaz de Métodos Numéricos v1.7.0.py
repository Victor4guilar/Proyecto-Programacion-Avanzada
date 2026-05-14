#---IMPORTACIONES---
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import math

#---CLASE PRINCIPAL---
class MetodosNumericosApp:
    VERSION = "v1.7.0"

    def __init__(self, root):
        self.root = root
        self.root.title(f"Suite de Métodos Numéricos {self.VERSION}")
        self.root.geometry("900x550")

        self.crear_layout()
        self.crear_statusbar()

    #INTERFAZ
    def crear_layout(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.panel_control = ttk.LabelFrame(self.main_frame, text="Configuración")
        self.panel_control.pack(side="left", fill="y", padx=5, pady=5)

        ttk.Label(self.panel_control, text="Método:").pack(pady=5)

        self.metodo_var = tk.StringVar()
        self.combo_metodos = ttk.Combobox(
            self.panel_control,
            textvariable=self.metodo_var,
            state="readonly",
            width=35
        )

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
            "Interpolación Lineal de Newton"
        ]

        self.combo_metodos.pack(pady=5)
        self.combo_metodos.bind("<<ComboboxSelected>>", self.validar_metodo)
        
        ttk.Button(self.panel_control, text="Cargar Método", command=self.cargar_metodo).pack(pady=10)
        ttk.Button(self.panel_control, text="Ejecutar", command=self.ejecutar_metodo).pack(pady=5)

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
        ttk.Label(self.root, textvariable=self.status, relief="sunken").pack(fill="x", side="bottom")

    def validar_metodo(self, event=None):
        metodo = self.metodo_var.get()
        if "────" in metodo:
            self.combo_metodos.set("")
            self.status.set("Seleccione un método válido")

    def evaluar_funcion(self, expr, x):
        try:
            permitido = {"x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log, "exp": math.exp, "sqrt": math.sqrt, "pi": math.pi, "e": math.e}
            return eval(expr, {"__builtins__": {}}, permitido)
        except Exception as e:
            raise ValueError(f"Error en la expresión: {e}")

    #--- MÉTODOS DE CÁLCULO --- (TODOS LOS 7 ANTERIORES + INTERPOLACIÓN)
    def metodo_biseccion(self, expr, a, b, erra):
        ejex, ejey = [], []; n = 0; error = abs(a - b)
        while error > erra:
            pi = (b + a) / 2
            if self.evaluar_funcion(expr, a) * self.evaluar_funcion(expr, pi) <= 0: b = pi
            else: a = pi
            error = abs(a - b); n += 1
            ejex.append(n); ejey.append(error)
        return pi, error, ejex, ejey

    def metodo_falsa_posicion(self, expr, a, b, erra):
        ejex, ejey = [], []; iteracion = 0; xr_anterior = a; error = 100
        while error > erra:
            fa, fb = self.evaluar_funcion(expr, a), self.evaluar_funcion(expr, b)
            xr = a - (fa * (b - a)) / (fb - fa)
            if iteracion > 0: error = abs((xr - xr_anterior) / xr)
            if fa * self.evaluar_funcion(expr, xr) < 0: b = xr
            else: a = xr
            xr_anterior = xr; iteracion += 1
            ejex.append(iteracion); ejey.append(error)
        return xr, error, ejex, ejey

    def metodo_newton_raphson(self, fun, fprima, Xi, erra):
        ejex, ejey = [], []; error = 100; n = 0
        while error > erra:
            fxi, fpxi = self.evaluar_funcion(fun, Xi), self.evaluar_funcion(fprima, Xi)
            if fpxi == 0: break
            Xn = Xi - (fxi / fpxi); error = abs((Xn - Xi) / Xn); Xi = Xn; n += 1
            ejex.append(n); ejey.append(error)
        return Xi, error, ejex, ejey

    def metodo_secante(self, expr, x0, x1, erra):
        ejex, ejey = [], []; error = 100; n = 0
        while error > erra and n < 100:
            fx0, fx1 = self.evaluar_funcion(expr, x0), self.evaluar_funcion(expr, x1)
            if (fx1 - fx0) == 0: break
            x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
            error = abs((x2 - x1) / x2) if x2 != 0 else 0
            x0, x1 = x1, x2; n += 1
            ejex.append(n); ejey.append(error)
        return x1, error, ejex, ejey

    def metodo_busqueda_incrementos(self, expr, xi, xf, incremento):
        ejex, ejey = [], []; x = xi; intervalos = []
        while x <= xf:
            fx = self.evaluar_funcion(expr, x); x_sig = x + incremento
            if fx * self.evaluar_funcion(expr, x_sig) < 0: intervalos.append((x, x_sig))
            ejex.append(x); ejey.append(fx); x = x_sig
        return intervalos, ejex, ejey

    def metodo_punto_fijo(self, gx, x0, erra):
        ejex, ejey = [], []; error = 100; n = 0
        while error > erra and n < 100:
            x1 = self.evaluar_funcion(gx, x0)
            error = abs((x1 - x0) / x1) if x1 != 0 else 0
            x0 = x1; n += 1
            ejex.append(n); ejey.append(error)
        return x1, error, ejex, ejey
    
    def metodo_minimos_cuadrados(self, arreglo_x, arreglo_y):
        n = len(arreglo_x)
        suma_X, suma_Y = sum(arreglo_x), sum(arreglo_y)
        suma_XY = sum(x * y for x, y in zip(arreglo_x, arreglo_y))
        suma_X2 = sum(x**2 for x in arreglo_x)
        a = ((n * suma_XY) - (suma_X * suma_Y)) / ((n * suma_X2) - (suma_X ** 2))
        b = ((suma_X * suma_XY) - (suma_Y * suma_X2)) / ((suma_X ** 2) - (n * suma_X2))
        eje_y = [(a * x + b) for x in arreglo_x]
        return a, b, eje_y

    def metodo_interpolacion_newton(self, x0, y0, x1, y1, xt):
        b1 = (y1 - y0) / (x1 - x0)
        yt = y0 + b1 * (xt - x0)
        return yt, b1

    #---CONTROLADOR DE INTERFAZ---
    def cargar_metodo(self):
        for widget in self.frame_inputs.winfo_children(): widget.destroy()
        metodo = self.metodo_var.get()
        if not metodo or "────" in metodo: return

        if metodo not in ["Mínimos Cuadrados Lineales", "Interpolación Lineal de Newton"]:
            ttk.Label(self.frame_inputs, text="Función:").grid(row=0, column=0, padx=5)
            self.entry_func = ttk.Entry(self.frame_inputs, width=30); self.entry_func.grid(row=0, column=1)

        if metodo == "Interpolación Lineal de Newton":
            campos = [("x0:", 0), ("y0:", 1), ("x1:", 2), ("y1:", 3), ("Valor X a buscar:", 4)]
            self.entries_interp = []
            for texto, fila in campos:
                ttk.Label(self.frame_inputs, text=texto).grid(row=fila, column=0)
                e = ttk.Entry(self.frame_inputs); e.grid(row=fila, column=1); self.entries_interp.append(e)
        elif metodo == "Newton Raphson":
            ttk.Label(self.frame_inputs, text="f'(x):").grid(row=1, column=0)
            self.entry_fprima = ttk.Entry(self.frame_inputs, width=30); self.entry_fprima.grid(row=1, column=1)
            ttk.Label(self.frame_inputs, text="x0 (Inicial):").grid(row=2, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs); self.entry_a.grid(row=2, column=1)
        elif metodo == "Mínimos Cuadrados Lineales":
            ttk.Label(self.frame_inputs, text="Valores X (comas):").grid(row=1, column=0)
            self.entry_x = ttk.Entry(self.frame_inputs, width=40); self.entry_x.grid(row=1, column=1)
            ttk.Label(self.frame_inputs, text="Valores Y (comas):").grid(row=2, column=0)
            self.entry_y = ttk.Entry(self.frame_inputs, width=40); self.entry_y.grid(row=2, column=1)
        elif metodo in ["Bisección", "Falsa Posición", "Secante"]:
            ttk.Label(self.frame_inputs, text="x0 / a:").grid(row=1, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs); self.entry_a.grid(row=1, column=1)
            ttk.Label(self.frame_inputs, text="x1 / b:").grid(row=2, column=0)
            self.entry_b = ttk.Entry(self.frame_inputs); self.entry_b.grid(row=2, column=1)
        elif metodo == "Búsqueda por Incrementos":
            ttk.Label(self.frame_inputs, text="x Inicial:").grid(row=1, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs); self.entry_a.grid(row=1, column=1)
            ttk.Label(self.frame_inputs, text="x Final:").grid(row=2, column=0)
            self.entry_b = ttk.Entry(self.frame_inputs); self.entry_b.grid(row=2, column=1)
            ttk.Label(self.frame_inputs, text="Incremento:").grid(row=3, column=0)
            self.entry_incremento = ttk.Entry(self.frame_inputs); self.entry_incremento.grid(row=3, column=1); self.entry_incremento.insert(0, "0.1")
        elif metodo == "Punto Fijo":
            ttk.Label(self.frame_inputs, text="x0 (Inicial):").grid(row=1, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs); self.entry_a.grid(row=1, column=1)

        if metodo not in ["Búsqueda por Incrementos", "Mínimos Cuadrados Lineales", "Interpolación Lineal de Newton"]:
            ttk.Label(self.frame_inputs, text="Tolerancia:").grid(row=3, column=0)
            self.entry_error = ttk.Entry(self.frame_inputs); self.entry_error.grid(row=3, column=1); self.entry_error.insert(0, "0.0001")

    def ejecutar_metodo(self):
        try:
            metodo = self.metodo_var.get()
            self.text_resultados.delete(1.0, tk.END)

            if metodo == "Interpolación Lineal de Newton":
                x0, y0, x1, y1, xt = [float(e.get()) for e in self.entries_interp]
                res, b1 = self.metodo_interpolacion_newton(x0, y0, x1, y1, xt)
                self.text_resultados.insert(tk.END, f"MÉTODO: {metodo}\n" + "-"*30 + f"\nPendiente (b1): {b1}\nResultado f({xt}) = {res}")
            elif metodo == "Mínimos Cuadrados Lineales":
                arreglo_x = list(map(float, self.entry_x.get().split(",")))
                arreglo_y = list(map(float, self.entry_y.get().split(",")))
                a, b, eje_y = self.metodo_minimos_cuadrados(arreglo_x, arreglo_y)
                self.text_resultados.insert(tk.END, f"MÉTODO: {metodo}\n" + "-"*30 + f"\ny = {a}x + {b}")
            elif metodo == "Búsqueda por Incrementos":
                intervalos, ex, ey = self.metodo_busqueda_incrementos(self.entry_func.get(), float(self.entry_a.get()), float(self.entry_b.get()), float(self.entry_incremento.get()))
                self.text_resultados.insert(tk.END, f"Intervalos encontrados: {intervalos}")
            else:
                expr, erra = self.entry_func.get(), float(self.entry_error.get())
                if metodo == "Bisección": res, err, ex, ey = self.metodo_biseccion(expr, float(self.entry_a.get()), float(self.entry_b.get()), erra)
                elif metodo == "Newton Raphson": res, err, ex, ey = self.metodo_newton_raphson(expr, self.entry_fprima.get(), float(self.entry_a.get()), erra)
                elif metodo == "Secante": res, err, ex, ey = self.metodo_secante(expr, float(self.entry_a.get()), float(self.entry_b.get()), erra)
                elif metodo == "Falsa Posición": res, err, ex, ey = self.metodo_falsa_posicion(expr, float(self.entry_a.get()), float(self.entry_b.get()), erra)
                elif metodo == "Punto Fijo": res, err, ex, ey = self.metodo_punto_fijo(expr, float(self.entry_a.get()), erra)
                self.text_resultados.insert(tk.END, f"Resultado: {res}\nError: {err}")

            #---GRÁFICA---
            if metodo == "Búsqueda por Incrementos":

                plt.figure("Búsqueda por Incrementos")

                plt.plot(ex, ey, marker='o', color='green')

                plt.axhline(0, color='black')

                plt.title("Búsqueda por Incrementos")

                plt.xlabel("x")
                plt.ylabel("f(x)")

                plt.grid(True)

            elif metodo == "Mínimos Cuadrados Lineales":

                plt.figure("Mínimos Cuadrados Lineales")

                plt.plot(
                    arreglo_x,
                    eje_y,
                    label="Recta Ajustada"
                )

                plt.title("Método de Mínimos Cuadrados")

                plt.xlabel("Eje X")
                plt.ylabel("Eje Y")
            
                plt.grid(True)

                plt.legend()

            elif metodo == "Interpolación Lineal de Newton":

                plt.figure("Interpolación Lineal")

                plt.plot([x0, x1], [y0, y1], marker='o', color='blue', label="Línea de Interpolación")
                plt.plot(xt, res, marker='x', color='red', markersize=10, label="Punto Interpolado")

                plt.title("Interpolación Lineal de Newton")

                plt.xlabel("x")
                plt.ylabel("y")

                plt.grid(True)
                plt.legend()

            else:

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

if __name__ == "__main__":
    root = tk.Tk()
    app = MetodosNumericosApp(root)
    root.mainloop()