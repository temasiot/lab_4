k, N = map(int, input().split())

i = k
S = 0
while i <= N:
    S += i**2/(k**2+N**2)
    i += 1
print(S)

i = k
S = 0
while True:
    S += i**2/(k**2+N**2)
    i += 1
    if i > N:
        break
print(S)

S = 0
for i in range(k, N+1):
    S += i**2/(k**2+N**2)
print(S)

S = 0
for i in range(N, k-1, -1):
    S += i**2/(k**2+N**2)
print(S)
