from random import randint

R = int(input())

for i in range(10):
    x, y = map(int, input().split())
    if -R <= y <= 0 <= x <= 2 * R:
        print('yes')
    elif (x + R) ** 2 - (y - R) ** 2 <= R ** 2:
        print('yes')
    else:
        print('no')

for i in range(10):
    x = randint(-2*R, 2*R)
    y = randint(-2*R, 2*R)
    if -R <= y <= 0 <= x <= 2 * R:
        print('yes')
    elif (x + R) ** 2 - (y - R) ** 2 <= R ** 2:
        print('yes')
    else:
        print('no')
