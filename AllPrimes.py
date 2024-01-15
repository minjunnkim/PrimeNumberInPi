import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

with open('pi1mil.txt') as f:
    inp = f.read()
    inp = inp[2:]

    temp = []

    for i in inp:
        if int(i) == 2 or int(i) == 3 or int(i) == 5 or int(i) == 7:
            temp.append(i)
        else:
            temp.append(0)
    pi = np.array(temp, dtype=int)
    print(pi[99])


fig = plt.figure()
ax = plt.axes(xlim=(0, 500), ylim=(0, 9))
x = np.arange(0, 500, 1)
line, = ax.plot(x, pi[x], color='green', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='blue', markersize=5)

plt.title('Prime Numbers in Pi')
plt.show()

#animated lines
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

with open('pi1mil.txt') as f:
    inp = f.read()
    inp = inp[2:]

    temp = []

    for i in inp:
        if int(i) == 2 or int(i) == 3 or int(i) == 5 or int(i) == 7:
            temp.append(i)
        else:
            temp.append(0)
    pi = np.array(temp, dtype=int)
    print(pi[99])


fig, ax = plt.subplots()
x = np.arange(0, 1000000, 1)
line, = ax.plot(x, pi[x], color='green', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='blue', markersize=5)


def animate(i):
    line.set_ydata(pi[x+i])
    return line,


plt.title('Prime Numbers in Pi')

ani = animation.FuncAnimation(fig, animate, interval=20, blit=True)

plt.show()
"""

#animated individual points
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

with open('pi1mil.txt') as f:
    inp = f.read()
    inp = inp[2:]

    temp = []

    for i in inp:
        if int(i) == 2 or int(i) == 3 or int(i) == 5 or int(i) == 7:
            temp.append(i)
        else:
            temp.append(0)
    pi = np.array(temp, dtype=int)
    print(pi[99])


fig = plt.figure()
ax = plt.axes(xlim=(0, 500), ylim=(0, 9))
x = np.arange(0, 500, 1)
line, = ax.plot([], [], color='green', linestyle='dashed', linewidth=1, marker='o', markerfacecolor='blue', markersize=5)


def animate(i):

    line.set_data(i, pi[i])
    return line,


plt.title('Prime Numbers in Pi')

ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=500)

plt.show()
"""