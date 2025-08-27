li = []
for _ in range(int(input())):
    li.append(int(input()))
    
answer = li[-1]
if li[2]-li[1] == li[1]-li[0]:
    answer += (li[1]-li[0])
elif li[2]//li[1] == li[1]//li[0]:
    answer *= (li[1]//li[0])

print(answer)