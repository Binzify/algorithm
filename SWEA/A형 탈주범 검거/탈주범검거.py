import sys
sys.stdin = open('sample_input.txt')

# 파이프 번호에 따른 갈 수 있는 길
pipe = [[0,0,0,0],[1,1,1,1],[1,1,0,0],[0,0,1,1],[1,0,0,1],[0,1,0,1],[0,1,1,0],[1,0,1,0]]
di, dj = (-1,1,0,0), (0,0,-1,1)
opp = [1,0,3,2]  # 반대편 파이프 (맞돌아가는가?) 상하좌우 - 하,상,우,좌

def bfs(n,m,si,sj,l):
    q = []
    v = [[0]*m for _ in range(n)]  # 방문표시를 위한 공간

    q.append((si,sj))  # 큐에다 시작 지점 담고
    v[si][sj] = 1  # 방문 표시
    cnt = 1  # 도망친 장소 세기

    while q:  # 큐가 있는 동안
        ci, cj = q.pop(0)
        if v[ci][cj] == l:  # 만약 소요 시간된 위치다
            return cnt  # 끝

        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]  # 이동한 거리(이동한 파이프)
            # 새로 이동한 곳이 인덱스 범위 안이고, 방문하지 않았으며, 현재 있는 파이프의 갈 방향과 이동할 파이프의 방향이 연결되어 있는지?
            if 0 <= ni < n and 0 <= nj < m and v[ni][nj] == 0 and pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                q.append((ni, nj))  # 연결되어 있다면 다음 갈 장소를 큐에다 넣고
                v[ni][nj] = v[ci][cj]+1  # 방문표시를 이전 간 횟수 +1 을 해주어 탈출 소요 시간을 확인한다.
                cnt += 1  # 도망칠 수 있는 장소 +1
    return cnt  # 더이상 도망칠 곳이 없다면 그 상태에서 출력



T = int(input()) # 테케
for tc in range(1, T+1):
    n, m, r, c, l = map(int,input().split())  # 세로, 가로 / 맨홀세로, 가로 / 탈출 소요시간
    arr = [list(map(int,input().split())) for _ in range(n)]
    answer = bfs(n,m,r,c,l)
    print(f'#{tc} {answer}')