N = int(input())

for num in range(N, 3, -1):
    if all(ch in '47' for ch in str(num)):
        print(num)
        break
