from math import pi
from math import atan
from prettytable import PrettyTable

xp, xk, dx, eps = map(float, input().split())
th = ['x', 'atan', 'Сума', 'n']
table = PrettyTable(th)
td = []
x = xp
while x <= xk:
    S = 0
    n = 1
    a = pi/2-x+(x**3)/3
    while True:
        S += a
        a *= -(x ** 2) / 2
        if abs(a) < eps:
            S += pi/2
            td.append(x)
            td.append(atan(x))
            td.append(S)
            td.append(n)
            table.add_row(td)
            td = []
            break
        n += 1
    x += dx
print(table)
