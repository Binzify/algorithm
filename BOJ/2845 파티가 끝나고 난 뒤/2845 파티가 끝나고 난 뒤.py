l, p = map(int, input().split())
party = list(map(int, input().split()))

answer = []

for number in party:
    answer.append(number - (l * p))

print(*answer)
