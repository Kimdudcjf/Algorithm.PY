import sys
sys.setrecursionlimit(10000)

computer = int(input())
network = int(input())

graph = [[] for _ in range(computer + 1)]
visited = [False] * (computer + 1)
count = 0

for _ in range(network):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    global count
    visited[v] = True
    count += 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

print(count - 1)