import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)  # DFS사용 시 코테할 때 쓰셈 범위

# 델타 (상하좌우 + 대각선) 0,0 ~ 2,2
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def dfs(x, y):
    visited[x][y] = 1

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < h and 0 <= ny < w:  # 인덱스 범위 안인지 확인하고
            if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                dfs(nx, ny)


# 계속 주어지다가 0 0 으로 끝이 남
while True:
    w, h = map(int, input().split())  # w가 열, h가 행
    if w == 0 and h == 0:
        break
    else:
        maps = []  # 그래프 만들기
        island = 0  # 섬 개수 세기
        for _ in range(h):
            maps.append(list(map(int, input().split())))
        visited = [[0] * w for _ in range(h)]  # 방문표시

        for i in range(h):
            for j in range(w):
                if maps[i][j] == 1 and visited[i][j] == 0:
                    dfs(i, j)
                    island += 1
        print(island)
