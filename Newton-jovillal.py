#!/usr/bin/env python
# coding: utf-8

# Newton Rapson es un método para encontrar raices de funciones, en su versión más simple toma una función de una variable real en una variable real y sin discontinuidades (que soporte una expansión en serie de Taylor). 
# El método requiere de un punto inicial, alrededor del cual se buscará la raiz.
# Newton-Rapson se aproxima a la raíz de manera recurrente, se puede resumir de la siguiente manera:
#     Dado un punto inicial $x_0$ y una función $f$
#         1) Se calcula la recta tanjente a $f(x_0)$, esto es $y(x) = m (x-x0) + b$ con $m = f^\prime (x_0)$ y $b = f(x_0)$
#         2) Una vez tenemos la recta tanjente, calculamos $x_1$ tal que $y(x_1) = 0$, es decir. el cero de esta recta. Tenemos, entonces que $x_1 = x_0 - \frac{f(x_0)}{f^\prime(x_0)}$. Este $x_1$ es la primera aproximación de la raíz.
#         3) En general $f(x_1) \ne 0$, pero podemos repetir los pasos (1) y (2) con este nuevo valor para obtener una nueva aproximación, es decir, podemos calcular $x_2 = x_1 - \frac{f(x_1)}{f^\prime(x_1)}$; la idea es que $|f(x_2)| < |f(x_1)|$.
#         4) Podemos repetir los pasos (1) y (2) tantas veces como queramos hasta llegar a un $x_n$ tal que $|f(x_n)| \le 10^{-s}$ donde $s$ fue definido previamente por nosotros (es decir, podemos encontrar un $f(x_n)$ tan cercano a cero como se desee.
#      
# Newton-Rapson converge de forma cuadrática y encuentra raices siempre que $f(x)$ sea bien comportada (derivadas continuas en todo su dominio, sin discontinuidades).
# 
# Problemas del método: 
#   Newton-Rapson requiere el cálculo de la derivada, esto puede ser problemático si se calcula de manera numérica.
#   Si la primera derivada en $x_0$ es cercana a 0, el método puede dispararse y encontrar una raiz lejana al punto inicial.
#   Si la primera derivada en $x_0$ es 0, el método no funciona.
#   
#   
#  La implementación de Newton-Rapson depende de las facilidades computacionales que de el lenguaje de programación que se utilice, si el lenguaje tiene facilidades simbólicas y soporta un paradigma de programación funcional implementarlo es trivial, algo del tipo:
#      newt[f_,x0,iter_]:=Nest[#-(f[#])/(D[f[#]),x0,iter] 
#      donde iter sea el número de iteraciones y f la función.
#      
# En caso de ser un lenguaje procedimental sin capacidades simbólicas (C, o Python) sería necesario hacer el cálculo de la derivada de forma numérica.
# Otra posibilidad es utilizar funciones ya creadas, en Python existe scipy.optimize.newton (https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html)
# 
# A continuación un ejemplo utilizando scipy, para la función coseno (el jupiter que está correindo no tiene scipy, salvo con el error)

# In[4]:


import numpy
import matplotlib.pyplot as plt
import scipy


# In[2]:


x = numpy.linspace(0, 2*numpy.pi, 32)


# In[4]:


fig = plt.figure()
plt.plot(x,numpy.cos(x)) 
plt.show()


# In[5]:


from scipy import optimize


# In[ ]:


root = optimize.newton(f, 1.5) #esto debería funcionar, pero scipy no carga


# Procedimentalmente, para la función coseno, se haría algo de la siguiente manera:

# In[5]:


def d(f, x, h): #esto calcula la derivada numérica cerca a x, utiliza un paso (step) de tamaño h
    deriv = (1.0/(2*h))*(f(x+h)-f(x-h))
    return deriv


# In[8]:


def newton(f, x0, h): #esta es la implementación del método
    xn = x0
    prev = 0

    while (abs(f(xn) - prev) > h):
         xn = xn - (f(xn))/d(f, xn, h)

    return xn


# Para un caso en el que iniciamos cerca a un cero de la función

# In[9]:


newton(numpy.cos,2,10**(-3))


# In[11]:


numpy.cos(newton(numpy.cos,2,10**(-3)))


# In[ ]:


Para un caso en el que iniciamos cerca a un punto donde la derivada es cercana a cero


# In[12]:


newton(numpy.cos,0.0001,10**(-3))


# In[ ]:


El cero que se encontró está muy lejos del punto inicial

