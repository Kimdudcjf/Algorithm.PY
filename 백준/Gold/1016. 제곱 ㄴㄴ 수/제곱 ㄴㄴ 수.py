import math

minv, maxv = map(int, input().split())

size = maxv - minv + 1
check = [False] * size

for i in range(2, int(math.sqrt(maxv)) + 1):
    squ = i * i
    start = ((minv + squ - 1) // squ) * squ

    for j in range(start, maxv + 1, squ):
        check[j - minv] = True

print(check.count(False))
        