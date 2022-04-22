import sys
sys.stdin = open('input.txt')

def bfs(x, y):
    q = []
    q.append((x, y))  # 첫 시작지점
    while q:
        gx, gy = q.pop(0)
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx = gx+dx
            ny = gy+dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[gx][gy] + 1
                q.append((nx, ny))

    return maze[N-1][M-1]

N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

print(bfs(0, 0))