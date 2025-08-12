n = int(input())
tip = 0
tiplist = []

for i in range(1,n+1):
    a = int(input())
    tiplist.append(a)

tiplist.sort(reverse=True)

for i in range(1,n+1):
    if tiplist[i-1] - (i - 1) <= 0:
        tip += 0
    else:
        tip += tiplist[i-1] - (i -1)

print(tip)