from prettytable import PrettyTable

a, b, c, xs, xe, dx = map(int, input().split())
y_all = ['F']
x_all = ['x']
for x in range(xs, xe+1, dx):
    if x < 5 and c != 0:
        F = -a * x ** 2 - b
    if x > 5 and c == 0:
        F = (x - a) / x
    if not (x < 5 and c != 0) and not (x > 5 and c == 0):
        F = -x / c
    y_all.append(F)
    x_all.append(x)
table = PrettyTable(x_all)
table.add_row(y_all)
print(table)
