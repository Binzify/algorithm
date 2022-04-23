import sys

sys.stdin = open('input.txt')

from collections import deque


def bfs(s):
    global answer
    q = deque()  # 시작 지점과 이동 거리를 함께 튜플로 묶어서 큐에 담는다
    q.append((s, 0))
    visited[s] = 1  # 방문처리하기
    while q:
        city, cnt = q.popleft()
        if cnt == k:  # 만약 해당하는 거리의 도시라면
            answer.append(city)  # 정답 리스트에 담아버리기
        elif cnt < k:
            for i in cities[city]:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append((i, cnt + 1))


n, m, k, x = map(int, input().split())
N = n + 1
# 단방향 그래프 생성하기
cities = [[] for _ in range(N)]
visited = [0] * N  # 방문 체크
answer = []  # 해당하는 도시 집어넣기

for _ in range(m):
    a, b = map(int, input().split())
    cities[a].append(b)

bfs(x)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()  # 오름차순 정렬
    for num in answer:
        print(num)
