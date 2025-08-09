N = int(input())
A = []

for _ in range(N):
    a = int(input())
    A.append(a)

A.sort()
sorted(A, reverse=False)

for i in range(N):
    print(A[i])
    