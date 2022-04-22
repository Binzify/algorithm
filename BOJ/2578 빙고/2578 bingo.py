import sys


sys.stdin = open('input.txt')

def check(gamer):
    bingo = 0

    # 행, 열 확인
    for i in range(5):
        row = col = 0 # 한 줄 끝날때마다 초기화 해주기
        for j in range(5):
            row += gamer[i][j]
            col += gamer[j][i]
            if row == 0:
                bingo += 1
            if col == 0:
                bingo += 1
    d1 = d2 = 0  # 대각선 양방향 확인
    for i in range(5):
        d1 += gamer[i][i]
        d2 += gamer[i][4-i]
        if d1 == 0:
            bingo += 1
        if d2 == 0:
            bingo += 1
    if bingo >= 3:
        print(speak)
    return

gamer = [list(map(int,input().split())) for _ in range(5)]
host = []
for _ in range(5):
    host.extend(map(int,input().split()))

speak = 0
for number in host:
    speak += 1
    for i in range(5):
        for j in range(5):
            if gamer[i][j] == number:
                gamer[i][j] = 0
    if speak >= 10: # 만약 10번 이상 부르면 그때마다 체크해준다.
        bingo = 0
        # 행, 열 확인
        for i in range(5):
            row = col = 0  # 한 줄 끝날때마다 초기화 해주기
            for j in range(5):
                row += gamer[i][j]
                col += gamer[j][i]
            if row == 0:
                bingo += 1
            if col == 0:
                bingo += 1
        d1 = d2 = 0  # 대각선 양방향 확인
        for i in range(5):
            d1 += gamer[i][i]
            d2 += gamer[i][4 - i]
        if d1 == 0:
            bingo += 1
        if d2 == 0:
            bingo += 1
        if bingo >= 3:
            print(speak)
            break
