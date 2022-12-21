import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(x):
   return np.sin(x) + x + x * np.sin(x)

x = np.linspace(-10, 10, 100)

plt.plot(x, f(x), color='red')
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
plt.grid()
# giving a title to my graph
plt.title('My first graph!')
plt.show()