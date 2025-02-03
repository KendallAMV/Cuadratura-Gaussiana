# Explanation

## Cuadratura Gaussiana

Uno de los métodos más poderosos para evaluar integrales de forma numérica es la **cuadratura Gaussiana**.

La idea principal está dada por
\begin{align}
\int_{a^b} {\rm{d}}x f(x) \approx \sum_{k=1}^{N+1} w_{k} f(x_{k}).
\end{align}
donde:
  * $w_{k}$ son los "pesos"
  * $x_{k}$ son los puntos de muestreo. Nótese que usamos $N+1$ puntos (es decir, $N$ subregiones o subintervalos)
  
Para las ecuaciones de Newton-Cotes de la clase anterior:  
  * Los puntos de muestreo son **equidistantes**.
  * Una ecuación de Newton-Cotes de orden $N$ es *exacta* (i.e., no hay aproximación) para un polinomio de grado $N$.
  * Un polinomio de orden $N$ aproxima una función bien comportada mejor que un polinomio de orden $N-1$, debido al grado de libertad añadido.
  
Por el otro lado, para la cuadratura Gaussiana:
  * Los puntos de muestreo se escogen de manera tal que **no son equidistantes**. Esto introduce más grados de libertad para la misma discretización en $N$ subregiones.
  * Es exacta para un polinomio de orden $(2N - 1)$.
  * Es decir, la cuadratura Gaussiana da la misma precisión que un polinomio de orden $(2N - 1)$.

Existe una **regla universal para escoger $w_k$ y $x_k$**. Los pesos y puntos de muestreo se eligen tal que:
  * $x_{k}$ corresponden a las $N$ raíces (ceros) de los polinomios de Legendre $P_{N}(x)$ de orden $N$.
  * Los pesos se eligen tal que:
      - $\displaystyle w_{k} = \left[\frac{2}{1-x^2}\left(\frac{dP_{N}}{dx}\right)^{-2}\right]_{x={x_k}}$, con $x_k$ que cumple $P_N(x_k)=0$

## Polinomios de Legendre

Los polinomios de Legendre son un sistema de polinomios ortogonales que pueden ser definidos de manera recursiva. Tenemos:
\begin{align}
\forall (M, N) \in\mathbb N^2, \quad \int_{-1}^1 {\rm{d}}x P_{N}(x)P_{M}(x) = \frac{2\delta_{MN}}{2N+1}.
\end{align}
Note que los polinomios están definidos en el intervalo $[-1, 1]$.
Los se definen empezando con
\begin{align}
P_{0}(x) = 1 \Rightarrow P_{1}(x) = x,
\end{align}
tal que los siguientes órdenes se generan con la regla de recursividad
\begin{align}
(N+1)P_{N+1}(x) = (2N+1)xP_{N}(x) -NP_{N-1}(x).
\end{align}
Alternativamente, los polinomios pueden ser definidos de manera iterativa bajo la regla (fórmula de Rodrigues)
\begin{align}
P_{N}(x) = \frac1{2^N N!}\frac{d^N}{dx^N}\left[(x^2-1)^N\right].
\end{align}

Una vez que conocemos los polinomios de Legendre, debemos encontrar sus raíces y calcular los pesos de acuerdo con la regla que describimos al inicio de esta explicación.

Esto es un procedimiento ligeramente costoso dependiendo de la metodología que se utilice. La idea es que si necesitamos evaluar la integral utilizando distintos intervalos de integración, primero realizamos el cálculo de los puntos de muestreo $x_{k}$ y los pesos $w_{k}$ en el intervalo $[-1, 1]$. Posteriormente, podemos escalar los parámetros para ser modificados a un intervalo $[a, b]$.

El código visto aquí calcula los $x_{k}$ y  los $w_{k}$ utilizando **código vectorial**.



