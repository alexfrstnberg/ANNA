import matplotlib.pyplot as plt
from numpy import sin, linspace
import os           
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

x = []
y = []
xdata = linspace(-5,5,200)
ydata = 1/xdata*sin(5*xdata)

fig = plt.figure()
fig.set(facecolor = 'pink')
ax = fig.add_subplot()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ln, = plt.plot([], [], 'magenta')

def init():
    ax.set_xlim(-5, 5)
    ax.set_ylim(min(ydata), max(ydata))
    return ln,

def update(frame):
    x.append(frame)
    y.append(1/frame*sin(5*frame))
    ln.set_data(list(x), list(y))
    return ln,

ani = FuncAnimation(fig, update, frames=linspace(-5, 5, 200),
                    init_func=init, blit=True, interval=50)

plt.show()

