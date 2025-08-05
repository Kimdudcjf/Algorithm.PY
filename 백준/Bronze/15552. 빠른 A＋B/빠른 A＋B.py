import sys


T = int(sys.stdin.readline().rstrip())
result = []
for _ in range(T):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  result.append(a+b)

for i in range(T):
  print(result[i])
