import sys


sys.stdin = open('sample_input.txt')

def dfs(graph, start, visited):
    visited[start] = 1  # 방문처리를 해준다.
    for i in graph[start]:  # 이어진 노드들을 불러왔을 때
        if visited[i] == 0:  # 그 노드가 방문처리가 되어있지 않다면
            dfs(graph, i, visited)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())  # V = 노드 수, E 는 주어지는 연결노드 정보 개수
    graph = [[] for _ in range(V+1)]  # 인덱스 0은 사용하지 않는다
    for _ in range(E):  # E 개만큼 받는다.
        p, c = map(int,input().split())
        graph[p].append(c)

    visited = [0] * (V+1)

    start, end = map(int, input().split())

    dfs(graph, start, visited)

    print(f'#{tc} {visited[end]}')
