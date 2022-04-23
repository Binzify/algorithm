import sys


sys.stdin = open('sample_input.txt')


def bfs(starti, startj, exiti, exitj):
    q = []  # 빈 큐 리스트
    visited = [[0] * N for _ in range(N)]  # 방문표시를 위한 리스트

    q.append([starti, startj])  # 처음 시작지점을 큐에 넣고, 방문표시를 한다.
    visited[starti][startj] = 1

    while q:  # 큐가 있는동안에
        goi, goj = q.pop(0)  # 큐에서 기존 값을 빼내어서
        for i in range(4):  # 델타 이동으로 확인하기
            newi, newj = goi + dx[i], goj + dy[i]
            if (
                0 <= newi < N
                and 0 <= newj < N
                and visited[newi][newj] == 0
                and maze[newi][newj] != '1'
            ):
                q.append([newi, newj])
                visited[newi][newj] = visited[goi][goj] + 1
            if goi == exiti and goj == exitj:  # 그 값이 최종 도착지점의 인덱스랑 같다면
                return visited[goi][goj] - 2  # 최종 결과값으로 도착지점 전의 위치를 반환한다.
    return 0  # 만약 최종 지점에 접하지 않는다면 0을 반환한다.


# 상하좌우 델타
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                starti, startj = i, j
            elif maze[i][j] == '3':
                exiti, exitj = i, j

    answer = bfs(starti, startj, exiti, exitj)
    print(f'#{tc} {answer}')
