n = int(input())

n = 1000 - n
count = 0

coin_array = [500, 100, 50, 10, 5, 1]

for coin in coin_array :
    count += n // coin
    n %= coin

print(count)
    