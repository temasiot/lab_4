from math import pi
from math import atan
from prettytable import PrettyTable

xp, xk, dx = map(float, input().split())
#eps = float(input())
eps = 0.000000000001
th = ['x', 'atan', 'Сума', 'n']
table = PrettyTable(th)
td = []
x = xp
while x <= xk:
    S = 0
    n = 1
    a = x**3/3+x
    while True:
        S += a
        a *= -(x ** 2) / 2
        if abs(a) < eps:
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
