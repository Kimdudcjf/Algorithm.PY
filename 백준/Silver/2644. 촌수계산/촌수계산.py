n = int(input())
a, b = map(int, input().split())
m = int(input())

result = -1
parent = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    parent[x].append(y)
    parent[y].append(x)

def dfs(v, count):
    global result
    visited[v] = True

    if v == b:
        result = count
        return
      
    for i in parent[v]:
        if not visited[i]:
            dfs(i, count + 1)

dfs(a, 0)
print(result)