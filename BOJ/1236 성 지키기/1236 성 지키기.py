import sys


sys.stdin = open('input.txt')

n, m = map(int,input().split())
castle = [list(input()) for _ in range(n)]

cnt = 0  # 행 기준
colcnt = 0 # 열 기준
# 행 기준으로 찾기
for i in range(n):
    hall = 0
    for j in range(m):
        if castle[i][j] == '.':
            hall += 0
        else:
            hall += 1
    if hall == 0:
        cnt += 1
        
# 열로 돌리기
for i in range(m):
    hall = 0
    for j in range(n):
        if castle[j][i] == '.':
            hall += 0
        else:
            hall += 1
    if hall == 0:
        colcnt += 1
# 최소의 기준인데 요건을 충족하는 것이기에 필요 경비원 수가 많은 것을 출력한다
if colcnt < cnt:
    print(cnt)
else:
    print(colcnt)
