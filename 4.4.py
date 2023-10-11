from math import sqrt
from prettytable import PrettyTable

xs, xe, dx, R = map(int, input().split())
y_all = ['y']
x_all = ['x']
for x in range(xs, xe+1, dx):
    if x <= -R:
        y = R
    elif -R < x < R:
        y = R - sqrt(R ** 2 - x ** 2)
    elif R <= x < 6:
        y = (9 * R - 3 * x - R * x) / (6 - R)
    else:
        y = x - 9
    y_all.append(y)
    x_all.append(x)
table = PrettyTable(x_all)
table.add_row(y_all)
print(table)
