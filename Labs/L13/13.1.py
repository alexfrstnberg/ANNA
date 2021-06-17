import matplotlib.pyplot as plt
from numpy import sin, linspace
import os

x = linspace(-5, 5, 200)
y = 1/x*sin(5*x)

fig = plt.figure()
fig.set(facecolor = 'pink')
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.plot(x, y, 'pink', label = 'Y = 1/x*sin(5*x)')
plt.legend(loc='upper right')
plt.savefig(os.path.join('L13', '13.1.png'))
plt.show()
