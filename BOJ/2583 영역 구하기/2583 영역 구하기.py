import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)

M, N, K = map(int,input().split())
answer = []  # 빈 곳 넓이 담을 리스트

# 지도 만들기 
areamap = [[0]*N for _ in range(M)]

# 지도 표시
for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for a in range(x1, x2):
        for b in range(y1, y2):
            areamap[b][a] = 1  # 실수 금지... y값이 행 

# 델타
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x, y):
    global cnt
    areamap[x][y] = 1  # 넓이 셌음을 표시해줌
    cnt += 1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and areamap[nx][ny]==0:
            dfs(nx, ny)



# 넓이 세기
cnt = 0
for i in range(M):
    for j in range(N):
        if areamap[i][j] == 0:
            cnt = 0  # 매번 찾을 때 마다 초기화
            dfs(i,j)
            answer.append(cnt)

# 오름차순 정렬 후 출력
answer.sort()
print(len(answer))
print(*answer)

