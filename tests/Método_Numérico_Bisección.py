#Programa: Método de Bisección
#Autor: Aguilar Ortiz Victor 
#Descripción: Resuelve ecuaciones algebraicas 
#             por el método de bisección
#Funnción con la que trabaja el progrma: a) f(x)= (3x^2-18x+15)/5

import matplotlib.pyplot as plt

ejex = []                                      #Lista donde se guardarán los valores del eje x
ejey = []                                      #Lista donde se guardarán los valores del eje y

print("Programa Metodo de Bisección")
print("Ahora ingresarás el intervalo")
a = float(input("Valor de a:"))
b = float(input("Valor de b:"))

erra = float(input("Ahora el error aproximado:")) #Error aproximado
n = 0                                          #Variable para el contador n

error = abs(a - b)                             #Error que se estara comparando con erra
x = 0                                      #Variable x para la función   
def f(x):                                  #Definimos la funcion f(x)
    return ((3 * x**2)-(18 * x)+(15)) / 5  #Escribimos la función para recibir los resultados de la funcion evaluada

while error > erra: 
    pi = (b + a) / 2                           #Se calcula pi para los intervalos

    funa = f(a)                                #Se evalúa f(x) con repeecto a "a"
    funb = f(b)                                #Se evalúa f(x) con respecto a "b"

    if f(a) * f(pi) <= 0:                      #Se busca en que intervalo se encuentra la raíz
        b = pi                                 #Si esta en (a,pi) b se vuelve pi para deshechar (pi,b)
    else:
        a = pi                                 #Si esta en (b,pi) a se vuelve pi para deshechar (a,pi)
    
    error = abs(a - b)                         #Se calcula el error
    
    n = n + 1                                  #Contador para n
    ejex.append(n)                             #Lista donde se guardarán los valores de n
    ejey.append(error)                         #Lista donde se guardarán los valores del error
   
plt.plot(ejex, ejey)                           #Creamos la gráfica
plt.title("Gráfica Para el Error Obtenido")    #Le damos nombre
plt.xlabel("Número de Repeticiones")           #Nombre eje x
plt.ylabel("Valores del Error")                #Nombre eje y
plt.show()                                     #Mostramos la gráfica
    
print("Valor de a:", a)                        #Se imprime los resultados
print("Valor de b:", b)
print("Error aproximado:", error)
