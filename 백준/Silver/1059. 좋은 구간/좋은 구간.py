L = int(input())
S = list(map(int, input().split()))
n = int(input())

S.sort()
count = 0
A = 0
B = 0

if n in S:
    print(0)
else:
    for i in range(len(S)):
        if S[i] <= n:
            A = S[i]
        elif S[i] >= n:
            B = S[i]
            break

    left = n - A
    right = B - n
    result = left * right - 1

    print(result)