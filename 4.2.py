from math import log10
from math import e
from math import atan
from prettytable import PrettyTable

xs, xe, dx = map(int, input().split())
y_all = ['y']
x_all = ['x']
for x in range(xs, xe+1, dx):
    y = abs(9 * x ** 3 + 2)

    if x < 4:
        y += 3 * x ** 5 - x ** 3 + 2 * x - 1
    if x >= 7:
        y += log10(2 * x ** (-1) + e ** (3 * x + 1))
    if 4 <= x < 7:
        y += atan((x - 2) / 3)
    y_all.append(y)
    x_all.append(x)
table = PrettyTable(x_all)
table.add_row(y_all)
print(table)
