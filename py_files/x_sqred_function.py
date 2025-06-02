
import matplotlib.pyplot as plt 
import numpy as np

x = np.linspace(-10,10,400)

y = x**2 + + 3*x+5

plt.plot(x,y,label='$y = x^2+3x+5$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Grpah of $y = x^2+3x+5$')
plt.grid(True)
plt.legend()



plt.show()