Guia de trabajo para un trabajo limpio 
PARA GIT
1. No toques main: Nunca hagas commits directo a la rama principal
2. Crea una rama: Usa nombres que digan qué estás haciendo:

-feat/nombre-del-metodo (si vas a agregar Bisección, Secante, etc.)
-fix/error-matematico (si corriges un bug de cálculo o de la UI)
-docs/cambios-leeme (si solo vas a moverle a la documentación)
3. Pull Request (PR): Cuando termines, sube tu rama y avísale a los demás para que revisemos que todo corre bien antes de fusionar.

COMMITS
para que el historial no se vea mal usa 
-feat: Nuevo método o función (ej: feat: agregamos biseccion con graficas)
-fix: Arreglar algo roto (ej: fix: corregida division por cero en Newton)
-docs: Puros textos o manuales.
-style: Cambios visuales en la interfaz que no afectan el cálculo.

PARA EL CODIGO
al ser matematicas hay que tratar de ser lo mas explicitos posibles , por ende recomiendo :
-Nombres de variables: No uses solo a, b, c. Usa lim_inferior, raiz, error_aprox, iter_max. Que cualquiera que lea el código entienda qué fórmula estás usando.
-Comenta tus funciones: Cada método que agregues debe llevar un comentario rápido arriba explicando:
   1. Qué resuelve.
   2. Qué parámetros recibe (función, intervalos, tolerancia).
   3. Cuál es el criterio de parada (error o iteraciones).
-Manejo de Errores: Si el método no converge o el usuario mete un dato que rompe la función, lanza un aviso en la interfaz, no dejes que truene el programa.

ANTES DE SUBIR CAMBIOS 
prueba tu metodo con los ejercicios que veamos en clases de metodos numericos, si el resultado no coincide con el valor real , checa tu logica una ves mas...
sin mas que decir ¡BUENA SUERTE!.


