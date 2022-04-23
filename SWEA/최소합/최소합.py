import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    global min_sum, current
    # 가지치기
    if min_sum < current:
        return
    if x == N - 1 and y == N - 1:  # 도착지점에 도착하면 결과값 저장해주기
        min_sum = current
        return
    for dx, dy in [(1, 0), (0, 1)]:  # 우측과 아래로만 내려간다고 했으므로
        nx = x + dx
        ny = y + dy
        if (
            0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited
        ):  # 인덱스 범위 내에 있고 방문한 곳이 아니라면
            visited.append((nx, ny))  # 방문 표시 공간에 넣어준다
            current += arr[nx][ny]  # 지나다니며 합 구하기
            dfs(nx, ny)  # 재귀로 방문
            current -= arr[nx][ny]  # 재귀 끝나면 다시 원상복귀 시켜주기
            visited.remove((nx, ny))  # 방문표시 빼주기


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []  # 이동한 위치를 방문표시했다가 빼는 공간
    min_sum = 130  # 최종 프린트 할 정답
    current = arr[0][0]  # 가장 처음 값을 맨 처음 합으로 지정해둔다
    dfs(0, 0)
    print(f'#{tc} {min_sum}')
