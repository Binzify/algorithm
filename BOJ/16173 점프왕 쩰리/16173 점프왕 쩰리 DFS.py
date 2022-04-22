import sys
sys.stdin = open('input.txt')
# DFS로 구현
def dfs(x, y):
    # 범위 벗어나고 이미 방문을 한 경우라면
    if x < 0 or x >= N or y < 0 or y >= N or visited[x][y] == 1:
        return

    # 방문한 곳이 -1(도착점)이라면 방문 처리를 해주고 return 을 한다.
    if area[x][y] == -1:
        visited[x][y] = 1
        return

    # 방문 표시 (위의 재귀를 들어가지 않는다면)
    visited[x][y] = 1

    # 우측과 하단으로만 이동하므로 그에 대한 이동을 표시한다.
    dfs(x+area[x][y],y)
    dfs(x, y+area[x][y])


N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]  # 방문 여부 2차원 리스트
dfs(0, 0)

if visited[N-1][N-1] == 1:  # 만약 마지막 지점을 방문했다면
    print('HaruHaru')
else:
    print('Hing')