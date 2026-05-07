# ------------------ IMPORTACIONES ------------------
import tkinter as tk                      # Librería para crear interfaces gráficas
from tkinter import ttk, messagebox      # Widgets modernos y ventanas de error
import matplotlib.pyplot as plt          # Librería para graficar
import math                              # Librería de funciones matemáticas


# ------------------ CLASE PRINCIPAL ------------------
class MetodosNumericosApp:
    VERSION = "v1.1.0"  # Versión del programa (solo informativo)

    # Constructor: se ejecuta al iniciar el programa
    def __init__(self, root):
        self.root = root  # Guarda la ventana principal
        self.root.title(f"Suite de Métodos Numéricos {self.VERSION}")  # Título de la ventana
        self.root.geometry("850x520")  # Tamaño de la ventana

        self.crear_layout()     # Construye la interfaz
        self.crear_statusbar()  # Crea la barra inferior


    # ------------------ INTERFAZ ------------------
    def crear_layout(self):
        # Frame principal (contenedor general)
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # -------- Panel izquierdo (configuración) --------
        self.panel_control = ttk.LabelFrame(self.main_frame, text="Configuración")
        self.panel_control.pack(side="left", fill="y", padx=5, pady=5)

        ttk.Label(self.panel_control, text="Método:").pack(pady=5)

        # Variable donde se guarda el método seleccionado
        self.metodo_var = tk.StringVar()

        # Lista desplegable
        self.combo_metodos = ttk.Combobox(
            self.panel_control,
            textvariable=self.metodo_var,
            state="readonly"
        )
        self.combo_metodos['values'] = ["Bisección", "Falsa Posición", "Newton Raphson"]
        self.combo_metodos.pack(pady=5)

        # Botón que carga los inputs del método
        ttk.Button(self.panel_control, text="Cargar Método",
                   command=self.cargar_metodo).pack(pady=10)

        # Botón que ejecuta el método
        ttk.Button(self.panel_control, text="Ejecutar",
                   command=self.ejecutar_metodo).pack(pady=5)

        # -------- Panel derecho --------
        self.panel_trabajo = ttk.Frame(self.main_frame)
        self.panel_trabajo.pack(side="right", fill="both", expand=True)

        # Frame donde el usuario escribe datos
        self.frame_inputs = ttk.LabelFrame(self.panel_trabajo, text="Entradas")
        self.frame_inputs.pack(fill="x", padx=5, pady=5)

        # Frame donde se muestran resultados
        self.frame_resultados = ttk.LabelFrame(self.panel_trabajo, text="Resultados")
        self.frame_resultados.pack(fill="both", expand=True, padx=5, pady=5)

        # Caja de texto para imprimir resultados
        self.text_resultados = tk.Text(self.frame_resultados)
        self.text_resultados.pack(fill="both", expand=True)


    # ------------------ BARRA DE ESTADO ------------------
    def crear_statusbar(self):
        self.status = tk.StringVar(value="Listo")  # Texto inicial
        ttk.Label(self.root, textvariable=self.status,
                  relief="sunken").pack(fill="x", side="bottom")


    # ------------------ FUNCIÓN DINÁMICA ------------------
    def evaluar_funcion(self, expr, x):
        """
        Convierte una función escrita como texto en una función real.
        Ejemplo: 'x**2 - 4'
        """
        try:
            # Solo permitimos funciones matemáticas seguras
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

            # Evalúa la expresión usando solo lo permitido
            return eval(expr, {"__builtins__": {}}, permitido)

        except:
            raise ValueError("Error en la función")


    # MÉTODO DE BISECCIÓN 
    def metodo_biseccion(self, expr, a, b, erra):
        ejex, ejey = [], []  # Listas para la gráfica
        n = 0                # Contador de iteraciones
        error = abs(a - b)   # Error inicial

        # Ciclo del método
        while error > erra:
            pi = (b + a) / 2  # Punto medio

            # Evaluar función en puntos
            fa = self.evaluar_funcion(expr, a)
            fpi = self.evaluar_funcion(expr, pi)

            # Determinar en qué intervalo está la raíz
            if fa * fpi <= 0:
                b = pi
            else:
                a = pi

            error = abs(a - b)  # Nuevo error
            n += 1              # Incrementa iteración

            # Guardar datos para gráfica
            ejex.append(n)
            ejey.append(error)

        return a, b, error, ejex, ejey  # Regresa resultados

    #MÉTODO DE LA FALSA POSICIÓN
    def metodo_falsa_posicion(self, expr, a, b, erra):
        ejex, ejey = [], []  # Listas para graficar error vs iteración
        iteracion = 0  # Contador de iteraciones
        xr_anterior = a  # Guarda valor previo de xr para cálculo de error
        error = 100  # Inicializa error alto para iniciar el ciclo

        while error > erra:  # Itera hasta cumplir la tolerancia
            fa = self.evaluar_funcion(expr, a)  # Evalúa f(a)
            fb = self.evaluar_funcion(expr, b)  # Evalúa f(b)

            xr = a - (fa * (b - a)) / (fb - fa)  # Fórmula de falsa posición
            fxr = self.evaluar_funcion(expr, xr)  # Evalúa f(xr)

            if iteracion == 0:
                error = 1  # Primer error asumido como máximo
            else:
                error = abs((xr - xr_anterior) / xr)  # Calcula error relativo

            if fa * fxr < 0:
                b = xr  # Actualiza límite superior
            elif fa * fxr > 0:
                a = xr  # Actualiza límite inferior
            else:
                break  # Se encontró la raíz exacta

            xr_anterior = xr  # Guarda xr actual para siguiente iteración
            iteracion += 1  # Incrementa contador

            ejex.append(iteracion)  # Guarda número de iteración
            ejey.append(error)  # Guarda error correspondiente

        return xr, error, ejex, ejey  # Retorna resultados del método

    # MÉTODO DE NEWTON RAPHSON 
    def metodo_newton_raphson(self, fun, fprima, Xi, erra):

        ejex = []                                      #Lista donde se guardarán los valores del eje x
        ejey = []                                      #Lista donde se guardarán los valores del eje y

        error = 10000
        Xn = 0
        Xn_anterior = Xi
        n = 0

        def f(x):
            return eval(fun, {"x": x, "e": math.e, "log": math.log,
                              "sin": math.sin, "exp": math.exp})

        def g(x):
            return eval(fprima, {"x": x, "e": math.e, "log": math.log,
                                 "sin": math.sin, "exp": math.exp})

        while error > erra:
            fxi = f(Xi)
            fpxi = g(Xi)

            Xn = Xi - ((fxi) / (fpxi))

            if Xn != 0:
                error = abs((Xn - Xn_anterior) / Xn)

            Xn_anterior = Xn
            Xi = Xn

            n = n + 1                                  #Contador para n
            ejex.append(n)                             #Lista donde se guardarán los valores de n
            ejey.append(error)

        return Xn, error, ejex, ejey

    # ------------------ CARGAR MÉTODO ------------------
    def cargar_metodo(self):
        # Limpiar inputs anteriores
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        # Crear inputs para bisección
        if self.metodo_var.get() in ["Bisección", "Falsa Posición", "Newton Raphson"]:

            ttk.Label(self.frame_inputs, text="f(x):").grid(row=0, column=0)
            self.entry_func = ttk.Entry(self.frame_inputs, width=30)
            self.entry_func.grid(row=0, column=1)
            
            # Input para derivada en Newton Raphson
            if self.metodo_var.get() == "Newton Raphson":
                ttk.Label(self.frame_inputs, text="f'(x):").grid(row=1, column=0)

                self.entry_fprima = ttk.Entry(self.frame_inputs, width=30)
                self.entry_fprima.grid(row=1, column=1)

                ttk.Label(self.frame_inputs, text="Ej: 3*x**2 - 1").grid(row=1, column=2)

            ttk.Label(self.frame_inputs, text="Ej: x**3 - x - 2").grid(row=0, column=2)

            fila_inicio = 1

            if self.metodo_var.get() == "Newton Raphson":
                fila_inicio = 2

            ttk.Label(self.frame_inputs, text="Valor de a:").grid(row=fila_inicio, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=fila_inicio, column=1)

            # Solo mostrar b en métodos cerrados
            if self.metodo_var.get() in ["Bisección", "Falsa Posición"]:

                ttk.Label(self.frame_inputs, text="Valor de b:").grid(row=fila_inicio + 1, column=0)

                self.entry_b = ttk.Entry(self.frame_inputs)
                self.entry_b.grid(row=fila_inicio + 1, column=1)

            fila_error = fila_inicio + 1

            if self.metodo_var.get() in ["Bisección", "Falsa Posición"]:
                fila_error = fila_inicio + 2

            ttk.Label(self.frame_inputs, text="Error aproximado:").grid(row=fila_error, column=0)
            self.entry_error = ttk.Entry(self.frame_inputs)
            self.entry_error.grid(row=fila_error, column=1)

        self.status.set("Método cargado")


    # ------------------ EJECUTAR MÉTODO ------------------
    def ejecutar_metodo(self):
        try:
            # Obtener datos del usuario
            expr = self.entry_func.get()
            a = float(self.entry_a.get())
            erra = float(self.entry_error.get())

            metodo = self.metodo_var.get()

            # Solo pedir b en métodos cerrados
            if metodo in ["Bisección", "Falsa Posición"]:
                b = float(self.entry_b.get())
          

            # Validar solo métodos cerrados
            if metodo in ["Bisección", "Falsa Posición"]:
                if self.evaluar_funcion(expr, a) * self.evaluar_funcion(expr, b) > 0:
                    messagebox.showerror("Error", "No hay cambio de signo en el intervalo")
                    return

            metodo = self.metodo_var.get()  # Obtiene el método seleccionado por el usuario

            if metodo == "Bisección":
                a, b, error, ejex, ejey = self.metodo_biseccion(expr, a, b, erra)
                resultado = f"a = {a}\nb = {b}\nError ≈ {error}"  # Formato de salida para bisección

            elif metodo == "Falsa Posición":
                xr, error, ejex, ejey = self.metodo_falsa_posicion(expr, a, b, erra)
                resultado = f"Raíz aproximada ≈ {xr}\nError ≈ {error}"  # Formato de salida para falsa posición

            elif metodo == "Newton Raphson":

                fprima = self.entry_fprima.get()

                xr, error, ejex, ejey = self.metodo_newton_raphson(
                    expr,
                    fprima,
                    a,
                    erra
                )

                resultado = f"Raíz aproximada ≈ {xr}\nError ≈ {error}"            

            # Mostrar resultados
            self.text_resultados.delete(1.0, tk.END)
            self.text_resultados.insert(tk.END,
                f"Método: {metodo}\n\n"  # Muestra el método usado
                f"{resultado}"  # Muestra resultados calculados
            )

            # Graficar error vs iteraciones
            plt.plot(ejex, ejey)
            plt.title("Error vs Iteraciones")
            plt.xlabel("Iteraciones")
            plt.ylabel("Error")
            plt.show()

            self.status.set("Ejecución completada")

        except:
            messagebox.showerror("Error", "Verifica la función o los datos")


# ------------------ MAIN ------------------
if __name__ == "__main__":
    root = tk.Tk()                    # Crear ventana principal
    app = MetodosNumericosApp(root)  # Crear aplicación
    root.mainloop()                  # Mantener ejecución