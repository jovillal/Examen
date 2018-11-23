#!/usr/bin/env python
# coding: utf-8

# Escriba en un notebook de jupyter una explicación de algún método para encontar la recta que mejor ajusta a un conjunto de puntos. Deje en claro que requisitos anteriores deben tener los estudiantes (por ejemplo, algebra lineal, ecuaciones diferenciales, transformada de Fourier, etc) para entender el método propuesto. Para explicar los conceptos cree un conjunto de puntos y haga el ajuste de la recta.
# 
# Una opción simple es utilizar una regresión con mínimos cuadrados, esto requiere, básicamente dos cosas: un conjunto de datos y una función que se quiere ajustar a esos datos, en este caso la función es una recta.
# El problema es encontrar la pendiente ($m$) y el intercepto ($b$) de la recta, tal que se minimice la distancia a cada uno de los puntos del conjunto de datos; en el método de mínimos cuadrados, uno encuentra $m$ y $b$ tal que la suma de la distancia vertical (al cuadrado) de cada uno de los puntos a la recta sea mínima.
# En Python, utilizando librerías que no cargan en donde estoy trabajando, se podría hacer algo como lo siguiente (ligeramente adaptado de https://scipy-cookbook.readthedocs.io/items/LinearRegression.html)

# Primero, generar una secuencia de puntos con algo de ruido

# In[1]:


from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from matplotlib.pyplot import plot, title, show, legend


# Generamos una recta $y = 0.8 x - 4$ y le añadimos ruido

# In[ ]:


t = linspace(-5,5,100)
#los parámetros de la recta
a = 0.8
b = -4
x = polyval([a, b], t)
# ahora con ruido
xn = x + randn(n)


# Esta sería la regresión lineal, el 1 en polyfit indica que utilizamos un polinomio de grado 1 (una recta)

# In[ ]:


(ar, br) = polyfit(t, xn, 1)
xr = polyval([ar, br], t)
# esto calcula el rmse (error cuadrado medio)
err = sqrt(sum((xr - xn)**2)/n)


# Se haría la gráfica así

# In[ ]:


title('Regresión lineal')
plot(t, x)
plot(t, xn, 'k.')
plot(t, xr, 'r.-')
legend(['original','con ruido', 'regresión'])
show();

