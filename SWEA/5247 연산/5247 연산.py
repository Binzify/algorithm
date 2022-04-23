import sys

sys.stdin = open('sample_input.txt')
from collections import deque


def bfs(N, M):
    global cnt
    q = deque()
    q.append((N, cnt))  # 첫 시작 숫자와 횟수를 기록한다.
    visited = [0] * 1000001  # 이미 등장했던 숫자인지 표시하기
    while q:
        node, count = q.popleft()
        if visited[node] == 1:  # 이미 방문한 곳이라면
            continue  # 그냥 진행함
        visited[node] = 1
        if node == M:
            cnt = count
            return cnt
        count += 1
        if 0 < node + 1 <= 1000000:
            q.append((node + 1, count))
        if 0 < node - 1 <= 1000000:
            q.append((node - 1, count))
        if 0 < node * 2 <= 1000000:
            q.append((node * 2, count))
        if 0 < node - 10 <= 1000000:
            q.append((node - 10, count))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = 0
    bfs(N, M)
    print(f'#{tc} {cnt}')
