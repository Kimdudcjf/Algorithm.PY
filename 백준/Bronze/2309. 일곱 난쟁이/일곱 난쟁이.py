from itertools import combinations

a = list()
for _ in range(9):
  n = int(input())
  a.append(n)

for comb in combinations(a, 7):
  if sum(comb) == 100:
    result = sorted(comb)
    for i in result:
      print(i)
    break
  