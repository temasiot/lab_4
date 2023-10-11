from math import cos
from math import sin

P = 1
for n in range(1, 21):
    S = 0
    for k in range(n, 21):
        S += k**2
    P *= (1+sin(S))/(1+cos(S))
print(P)

P = 1
for n in range(20, 0, -1):
    S = 0
    for k in range(20, n-1, -1):
        S += k**2
    P *= (1+sin(S))/(1+cos(S))
print(P)

P = 1
n = 1
while n <= 20:
    S = 0
    k = n
    while k <= 20:
        S += k ** 2
        k += 1
    P *= (1 + sin(S)) / (1 + cos(S))
    n += 1
print(P)

P = 1
n = 1
while True:
    S = 0
    k = n
    while True:
        S += k ** 2
        k += 1
        if k > 20:
            break
    P *= (1 + sin(S)) / (1 + cos(S))
    n += 1
    if n > 20:
        break
print(P)
