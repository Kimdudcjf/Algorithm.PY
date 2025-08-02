n = int(input())

A = list(map(int, input().split()))
sortA = sorted(A)
P = []

for i in range(n):
    P.append(sortA.index(A[i]))
    sortA[sortA.index(A[i])] = -1

for i in range(n):
    print(str(P[i]), end=' ')
