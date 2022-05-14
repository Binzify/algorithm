from heapq import heappush, heappop  # 우선순위 큐 라이브러리
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def breakroom ():
    q = []
    heappush(q, [0, 0, 0])  # q에 push하기 = 출발지점 좌표 + 가중치
    visited[0][0] = True
    while q:
        l, x, y = heappop(q)  # 거리, x, y 좌표 (거리를 우선 한 이유는 앞의 값으로 힙 생성하므로)
        # 종료 조건: 끝에 도달
        if x == n-1 and y == n-1:
            return l
        for move in [(-1,0),(1,0),(0,1),(0,-1)]:
            nx = x+move[0]
            ny = y+move[1]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                if maze[nx][ny] == 0:  # 만약에 이동한 곳이 검은방이다 -> 부수기
                    heappush(q, [l+1, nx, ny])
                else:  # 그렇지 않으면 그냥 넣어주고 지나가기
                    heappush(q, [l, nx, ny])

n = int(input())
maze = [list(map(int,input().rstrip())) for _ in range(n)]  # 미로
visited = [[False]*n for _ in range(n)]  # 방문표시

print(breakroom())