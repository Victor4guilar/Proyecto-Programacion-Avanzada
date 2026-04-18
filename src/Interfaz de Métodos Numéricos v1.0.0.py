# ------------------ IMPORTACIONES ------------------

import tkinter as tk                      # Librería para crear interfaces gráficas
from tkinter import ttk, messagebox      # Widgets modernos y ventanas de error
import matplotlib.pyplot as plt          # Librería para graficar
import math                              # Librería de funciones matemáticas


# ------------------ CLASE PRINCIPAL ------------------

class MetodosNumericosApp:
    VERSION = "v1.0.0"  # Versión del programa (solo informativo)

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
        self.combo_metodos['values'] = ["Bisección"]  # Métodos disponibles
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


    # ------------------ MÉTODO DE BISECCIÓN ------------------

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


    # ------------------ CARGAR MÉTODO ------------------

    def cargar_metodo(self):
        # Limpiar inputs anteriores
        for widget in self.frame_inputs.winfo_children():
            widget.destroy()

        # Crear inputs para bisección
        if self.metodo_var.get() == "Bisección":

            ttk.Label(self.frame_inputs, text="f(x):").grid(row=0, column=0)
            self.entry_func = ttk.Entry(self.frame_inputs, width=30)
            self.entry_func.grid(row=0, column=1)

            ttk.Label(self.frame_inputs, text="Ej: x**3 - x - 2").grid(row=0, column=2)

            ttk.Label(self.frame_inputs, text="Valor de a:").grid(row=1, column=0)
            self.entry_a = ttk.Entry(self.frame_inputs)
            self.entry_a.grid(row=1, column=1)

            ttk.Label(self.frame_inputs, text="Valor de b:").grid(row=2, column=0)
            self.entry_b = ttk.Entry(self.frame_inputs)
            self.entry_b.grid(row=2, column=1)

            ttk.Label(self.frame_inputs, text="Error aproximado:").grid(row=3, column=0)
            self.entry_error = ttk.Entry(self.frame_inputs)
            self.entry_error.grid(row=3, column=1)

        self.status.set("Método cargado")


    # ------------------ EJECUTAR MÉTODO ------------------

    def ejecutar_metodo(self):
        try:
            # Obtener datos del usuario
            expr = self.entry_func.get()
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            erra = float(self.entry_error.get())

            # Validar que exista raíz en el intervalo
            if self.evaluar_funcion(expr, a) * self.evaluar_funcion(expr, b) > 0:
                messagebox.showerror("Error", "No hay cambio de signo en el intervalo")
                return

            # Ejecutar método
            a, b, error, ejex, ejey = self.metodo_biseccion(expr, a, b, erra)

            # Mostrar resultados
            self.text_resultados.delete(1.0, tk.END)
            self.text_resultados.insert(tk.END,
                f"Resultados:\n\n"
                f"Intervalo final:\n"
                f"a = {a}\n"
                f"b = {b}\n"
                f"Error ≈ {error}\n"
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