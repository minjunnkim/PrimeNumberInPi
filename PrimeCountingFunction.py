import matplotlib.pyplot as plt
import numpy as np
import math
from mpmath import *


def primecheck(n):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if n==1 or n==0 or (n % 2 == 0 and n > 2):
        return False
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(n**(1/2))+1, 2):
            if n%i == 0:
                return False
        return True


def mobius(n):
    p = 0

    # Handling 2 separately
    if (n % 2 == 0):

        n = int(n / 2)
        p = p + 1

        # If 2^2 also
        # divides N
        if (n % 2 == 0):
            return 0

    # Check for all
    # other prime factors
    for i in range(3, int(math.sqrt(n)) + 1):

        # If i divides n
        if (n % i == 0):

            n = int(n / i)
            p = p + 1

            # If i^2 also
            # divides N
            if (n % i == 0):
                return 0
        i = i + 2

    if (p % 2 == 0):
        return -1
    else:
        return 1


def R(x):
    nsum(lambda n: (mobius(n)/n)*li(x**(1/n)), [1, inf])


# x-axis values
x = np.arange(2, 3000000, 1)
# y-axis values
y1 = []

temp = 0
for i in x:
    if primecheck(i):
        temp += 1
        y1.append(temp)
    else:
        y1.append(temp)

# plotting points as a scatter plot
plt.plot(x, y1,  label="counted", color="red", marker="o", markersize=5, markerfacecolor='red', markeredgecolor='red', linestyle='dashed', linewidth=1)

y2 = x/(np.log(x))
plt.plot(x, y2, label="x/log(x)", color="magenta", linestyle='dashed', linewidth=1)

y3 = []

for i in x:
    y3.append(li(i))

plt.plot(x, y3, label="li(x)", color="black", linestyle='dashed', linewidth=1)



#R(x) + nsum(lambda p: )

# x-axis label
plt.xlabel('number')
# frequency label
plt.ylabel('prime count')
#show legend
plt.legend()
# plot title
plt.title('Prime Counting Function')

# function to show the plot
plt.show()