from collections import deque

N, K = map(int,(input().split()))

sircle = deque([i for i in range(1, N+1)])
result = []

while sircle:
    sircle.rotate(-(K-1))
    result.append(sircle.popleft())

print(f"<{', '.join(map(str, result))}>")