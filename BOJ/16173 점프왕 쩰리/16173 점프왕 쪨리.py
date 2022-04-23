import sys

sys.stdin = open('input.txt')

from collections import deque

# 젤리의 점프
def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        mx, my = q.pop()
        if area[mx][my] == -1:
            return 'HaruHaru'
        for dx, dy in (0, 1), (1, 0):
            nx = mx + dx * area[mx][my]
            ny = my + dy * area[mx][my]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
    return 'Hing'


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
print(bfs(0, 0))
