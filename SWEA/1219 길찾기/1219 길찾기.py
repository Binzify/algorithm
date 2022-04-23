import sys


sys.stdin = open('input.txt')


def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)


for _ in range(10):
    tc, v = map(int, input().split())  # 간선, 테스트케이스
    arr = list(map(int, input().split()))
    graph = [[] for _ in range(100)]  # 0 ~ 99까지 있으므로 그래프 형식으로 만들기 위해
    for i in range(v):
        p, c = arr[i * 2], arr[i * 2 + 1]  # 인덱스, 인덱스에 들어갈 값
        graph[p].append(c)

    visited = [0] * 100  # 미방문 0, 방문 1
    dfs(graph, 0, visited)  # 0부터 시작하기 때문에 그래프, 시작점, 방문목록 넣어준다.

    print(
        f'#{tc} {visited[-1]}'
    )  # visited[-1]은 99번째를 방문한 경우를 의미하고, 방문한 경우 1을 아니면 0을 출력한다
