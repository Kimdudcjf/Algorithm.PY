import sys
sys.setrecursionlimit(10000)

N , M = map(int, input().split())

field = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def dfs(x, y, symbol):
    visited[x][y] = True

    if symbol == '-':
        ny = y + 1
        if ny < M and not visited[x][ny] and field[x][ny] == '-':
            dfs(x, ny, symbol)
    elif symbol == '|':
        nx = x + 1
        if nx < N and not visited[nx][y] and field[nx][y] == '|':
            dfs(nx, y, symbol)

count = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j, field[i][j])
            count += 1

print(count)