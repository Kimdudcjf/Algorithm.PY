import sys

M = int(input())
N = int(input())

prime = [True] * (N + 1)
prime[0] = prime[1] = False

for i in range(2, int(N**0.5) + 1):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False

sum = 0
for i in range(M, N + 1):
    if prime[i]:
        sum += i
if sum == 0:
    print(-1)
else:
    print(sum)
    for i in range(M, N + 1):
        if prime[i]:
            print(i, end=' ')
            break