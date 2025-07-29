n = int(input())
dp = []
for _ in range(n):
    a, b = input().split()
    a = int(a)
    dp.append([a,b])

dp.sort(key=lambda x: x[0])

for i in range(n):
  print(*dp[i])
