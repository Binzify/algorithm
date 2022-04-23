import sys


sys.stdin = open('sample_input.txt')

# 오목 확인 함수 정의
def omok(lst):  # lst = 2차원 배열 오목판
    cnt = 0  # 오목 개수 셀 카운트
    # 가로 행
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 5:
                return 'YES'

    # 세로 행
    for i in range(N):
        for j in range(N):
            if lst[j][i] == 'o':
                cnt += 1
            else:
                cnt = 0
            if cnt >= 5:
                return 'YES'

    # 대각선 좌에서 우로 하단  + 추가적으로 대각선의 그 위대각선까지 다해야함
    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):
            for k in range(5):
                if lst[i + k][i + j] == 'o':
                    cnt += 1
                else:
                    cnt = 0
                if cnt >= 5:
                    return 'YES'
            for k in range(5):
                if lst[i + k][N - 1 - j - k] == 'o':
                    cnt += 1
                if cnt >= 5:
                    return 'YES'

    # 대각선 우에서 좌 하단
    for i in range(N):
        if lst[i][N - 1 - i] == 'o':
            cnt += 1
        else:
            cnt = 0
        if cnt >= 5:
            return 'YES'
    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(input()) for _ in range(N)]

    print(f'#{tc} {omok(area)}')
