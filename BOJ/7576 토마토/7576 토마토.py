import sys
sys.stdin = open('input.txt')

from collections import deque

m, n = map(int, input().split())
tomatobox = [list(map(int, input().split())) for _ in range(n)]


# 델타이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
q = deque([])

for i in range(n):
    for j in range(m):
        if tomatobox[i][j] == 1:
            q.append([i,j])

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안 + 안익은 토마토
            if 0 <= nx < n and 0 <= ny < m and tomatobox[nx][ny] == 0:
                # 1을 더해가면서 왔음을 표시하고 다음 이동
                # 최대 값이 정답이 될 것
                tomatobox[nx][ny] = tomatobox[x][y] + 1
                q.append([nx, ny])

bfs()

# 이후 토마토 상태 확인
for i in tomatobox:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    # 모두 익은 경우 가장 높은 값이 정답
    answer = max(answer, max(i))
# 맨 처음을 1로 표시해서-1로 빼주기
print(answer - 1)