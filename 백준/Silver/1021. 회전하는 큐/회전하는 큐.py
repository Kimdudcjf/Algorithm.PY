from collections import deque

N, M = map(int, input().split())
queue = deque(range(1,N+1))
jimin = list(map(int, input().split()))
count = 0


for i in jimin:
    idx = queue.index(i)
    if idx <= len(queue) // 2:
        while queue[0] != i:
            queue.rotate(-1)
            count +=1
    else:
        while queue[0] != i:
            queue.rotate(1)
            count +=1
    queue.popleft()

print(count)
        