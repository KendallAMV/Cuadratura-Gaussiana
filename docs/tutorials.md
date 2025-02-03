# Tutorials

Para usar este código las primeras 2 funciones se pueden dejar sin editar, la primera calcula los puntos de muestréo y sus pesos, mientras que la segunda funciona para escalarlos a los limites de la integral que se quiera resolver.

Seguidamente se hace llamado a ambas, a la primera indicandole el número de subregiones que se quiera usar (por ejemplo xw = gaussxw(7)) y a la segunda se le indica que tome los limites de la integral y los resultados de la tupla anterior: xw_{escalado} = gaussxwab(1,3, xw[0],xw[1]).

Después de esto se le indica la función a tratar, en este paso es solo de indicarle que retorne la función como tal, en nuestro caso, \Begin{align} \int_{1}^{3} \left( x^6 - x^2 \sin(2x) \right) \, dx \end{align} .
 
Y finalmente la última función realizará la sumatoria de los N resultados obtenidos aplicando los pesos y puntos a la función para luego dar el resultado de la integral.
