def rev(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())

result = rev(rev(x) + rev(y))

print(result)
