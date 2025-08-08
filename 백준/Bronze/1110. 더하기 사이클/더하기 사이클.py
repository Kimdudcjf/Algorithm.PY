N = int(input())
num = N

count = 0

while True:
    a = num // 10
    b = num % 10
    num = b * 10 + (a + b) % 10
    count += 1
    if num == N:
        break


print(count)