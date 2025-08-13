X = int(input())

line = 1

while X > line * (line + 1) // 2:
    line += 1

pos = X - (line * (line - 1) // 2)

if line % 2 == 0:
    numerator = pos
    denominator = line - pos + 1
else:
    numerator = line - pos + 1
    denominator = pos

print(f"{numerator}/{denominator}")