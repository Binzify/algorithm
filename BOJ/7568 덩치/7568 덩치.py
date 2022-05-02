import sys
sys.stdin = open('input.txt')

n = int(input())
# 학생리스트
person = []
# 덩치 등수 담기
ranklist = []

for _ in range(n):
    x, y = map(int,input().split())
    person.append((x, y))

# 덩치 비교
for i in range(n):
    rank = 1
    for j in range(n):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank += 1
    ranklist.append(rank)

print(*ranklist)
