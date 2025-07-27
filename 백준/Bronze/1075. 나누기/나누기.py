N = int(input())
F = int(input())

M = N % 100
N = N - M

result = 0

if N % F == 0:
    result = 0
else:
    result = F - (N % F)

if result < 10:
    print('0' + str(result))
else:
    print(result)

    