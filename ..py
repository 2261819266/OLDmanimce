# x = 0.0
# n = 100000
# for i in range(1, n):
#     x += 1.0 / (i * i)
# print(x)

import math

n = 1000
def f(x):
    if x > n:
        return 0
    return math.sqrt(x + (x + 1) * f(x + 1))

print(f(1))