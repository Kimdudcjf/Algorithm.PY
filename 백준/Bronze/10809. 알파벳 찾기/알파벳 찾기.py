S = input()

po = [-1] * 26

for i in range(len(S)):
    ch = S[i]
    index = ord(ch) - ord('a')
    if po[index] == -1:
        po[index] = i

print(*po)