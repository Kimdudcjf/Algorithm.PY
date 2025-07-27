def group_word(word):
    seen = set()
    prev_char = ''
    for char in word:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True

n = int(input())
count = 0

for _ in range(n):
    word = input().strip()
    if group_word(word):
        count += 1

print(count)
