numbers = [int(input()) for _ in range(10)]

re = {num % 42 for num in numbers}

print(len(re))