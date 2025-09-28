N, M = map(int, input().split())
baskets = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j + 1):
        baskets[x] = k

print(*baskets[1:])