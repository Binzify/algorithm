import sys


sys.stdin = open('input.txt')

# 델타이동 우>하>좌>상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    x = y = 0
    move = 0

    for i in range(1, N * N + 1):
        arr[x][y] = i
        x = x + dx[move]
        y = y + dy[move]
        if x < 0 or x >= N or y < 0 or y >= N or arr[x][y] > 0:
            x = x - dx[move]
            y = y - dy[move]
            move += 1
            if move == 4:
                move = 0
            x = x + dx[move]
            y = y + dy[move]

    print(f'#{tc}')
    for i in arr:
        print(*i)
