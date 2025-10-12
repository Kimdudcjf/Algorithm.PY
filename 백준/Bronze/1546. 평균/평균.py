N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
newscores = [(score / M) * 100 for score in scores]
average = sum(newscores) / N

print(average)