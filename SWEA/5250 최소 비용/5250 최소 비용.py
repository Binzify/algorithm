import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    fuel[x][y] = 0  # 첫 출발 연료는 0에서 시작

    while q:
        x, y = q.popleft()
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:  # 상하좌우 돌면서
            nx = x+dx
            ny = y+dy
            if 0 <= nx < N and 0 <= ny < N :  # 범위 안에 있다면
                # 이동한만큼의 사용한 연료 변수 (기본1)
                used = 1
                # 높이가 다르면 다른만큼 연료를 추가해주어야 하므로
                if H[x][y] < H[nx][ny]:  # 만약 기존 위치보다 이동하는 위치가 더 높으면
                    used += H[nx][ny] - H[x][y]  # 해당 위치의 차만큼 연료를 더해준다.
                # 연료 표시해주기 (최단거리 distance와 같음)
                if fuel[nx][ny] > fuel[x][y] + used:  # 기존 등록되어있는 연료의 값보다 새롭게 추가된 연료가 더 적다면
                    fuel[nx][ny] = fuel[x][y] + used  # 갱신해주기 (작은거리(값)으로)
                    q.append((nx, ny))  # 큐에다 삽입

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int,input().split())) for _ in range(N)]
    INF = 987654
    fuel = [[INF]*N for _ in range(N)]  # 소모한 연료를 체크하는 배열
    bfs(0,0)
    # bfs를 돌린 후 최종 도착지점을 프린트하면 된다.
    print(f'#{tc} {fuel[N-1][N-1]}')
