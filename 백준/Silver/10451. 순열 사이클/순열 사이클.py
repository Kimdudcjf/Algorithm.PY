def dfs(v):
    visited[v] = True
    next = arr[v]
    if not visited[next]:
        dfs(next)


T = int(input())
graph = []

for _ in range(T):
    N = int(input())
    visited = [False] * (N + 1)
    count = 0

    arr = list(map(int, input().split()))
    arr.insert(0,0)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            count += 1
            
    print(count)
