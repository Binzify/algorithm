import sys

sys.stdin = open('sample_input.txt')


def dfs(n, total):
    global min_tmp
    if total >= min_tmp:  # 가지치기
        return
    if n == N:
        min_tmp = total
        return
    for i in range(N):  # n행에 방문하지 않은 열을 선택
        if visited[i] == 0:  # 방문한 곳이 아니라면
            visited[i] = 1  # 방문 표시
            dfs(n + 1, total + factory[n][i])
            visited[i] = 0  # 방문 표시 지우기
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    min_tmp = 1500
    visited = [0] * N
    dfs(0, 0)

    print(f'#{tc} {min_tmp}')
