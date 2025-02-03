#!/usr/bin/env python
import numpy as np

"""Función de pesos y puntos de muestreo"""

def gaussxw(N):

    a = np.linspace(3, 4 * (N - 1), N) / ((4 * N) + 2)
    x = np.cos(np.pi * a + 1 / (8 * N * N * np.tan(a)))

    epsilon = 1e-15
    delta = 1.0
    while delta > epsilon:
        p0 = np.ones(N, dtype = float)
        p1 = np.copy(x)
        for k in range(1, N):
            p0, p1 = p1, ((2 * k + 1) * x * p1 - k * p0) / (k + 1)
        dp = (N + 1) * (p0 - x * p1) / (1 - x * x)
        dx = p1 / dp
        x -= dx
        delta = np.max(np.abs(dx))

    w = 2 * (N + 1) * (N + 1)/(N * N * (1 - x * x) * dp * dp)
    return x,w 
"""La misma retorna una tupla donde x son los puntos y w los pesos"""

"""Luego sigue la función para escalar a un intervalo [a,b] siendo estos el limite inferior y el limite superior
de la integral respectivamente"""

def gaussxwab(a, b, x, w):
    return 0.5 * (b - a) * x + 0.5 * (b + a), 0.5 * (b - a) * w

"""Con el siguiente paso se calculan los puntos y pesos según el N dado""" 
xw = gaussxw(7)

"""La siguiente instrucción sirve para escalar los resultados en el rango de la integral"""
xw_escalado = gaussxwab(1,3, xw[0],xw[1])

"""Aquí se crea la función y se evalua la integral""" 
def func(x):
    return x**6-x**2*np.sin(2*x)
"""Por lo que el valor de retorno es la función a tratar"""

def sumatoria(xw_escalado, func):
    result = np.sum(func(xw_escalado[0])*xw_escalado[1])
    return result
"""Finalmente se hace la sumatoria y se retorna el resultado de la integral"""
print(sumatoria(xw_escalado, func))
"""
Algunos ejemplos son:
    >>>from cuadratura import cuadratura
    >>>xw = gaussxw(4)
    317.3453903341579
    >>>xw = gaussxw(5)
    448.1161248127398
    >>>xw = gaussxw(6) 
    414.07734547752426
    >>>xw = gaussxw(7)
    317.34424667222606 

Siendo este último el más acercado al resultado de la integral

Este proyecto posee varias funciones de numpy:

- `np.linspace` - Funciona para hacer listas.
- `np.pi, np.cos, np.sin` - Argumentos matemáticos, pi,seno y coseno.
- `np.max` - Regresa el máximo
- `np.abs` - Regresa el valor absoluto.
- `np.ones` - Regresa un arreglo nuevo.
- `np.copy` - Crea la copia de lo indicado.
- `np.sum` - Regresa la sumatoria de los valores indicados.



"""







