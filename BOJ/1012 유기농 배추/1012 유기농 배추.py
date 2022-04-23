import sys


sys.stdin = open('input.txt')


def bfs(x, y):
    global worm
    worm.append(1)  # 벌레 한 마리 추가해주기
    q = []  # 빈 큐
    q.append((x, y))
    while q:
        cx, cy = q.pop(0)
        for i in range(4):
            nx = cx + dx[i]  # 가로
            ny = cy + dy[i]  # 세로
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                q.append((nx, ny))
                maps[nx][ny] = 0
    return


# 이동 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())  # 가로, 세로, 배추심은위치 개수
    maps = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())  # 좌표값 받기
        maps[y][x] = 1  # 좌표에 배추 심기

    worm = []  # 한 번 함수 돌때마다 벌레를 담고 최종적으로 길이를 답으로 내놓기
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                bfs(i, j)
    print(sum(worm))
