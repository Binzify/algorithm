import sys


sys.stdin = open('input.txt')

# DFS 가장 깊은 노드부터 검사하기
def dfs(v):
    # 방문한 노드 뽑기
    print(v, end=' ')
    visited[v] = True # 방문처리하기
    # 다른 노드 재귀적 방문
    for i in graph[v]:
        if not visited[i]:  # 방문 안했다면
            dfs(i)

# BFS 근처의 노드 검사하기
def bfs(v):
    q = [v]
    b_visited[v] = 1  # 방문표시하기
    while q:  # 큐가 비어있지 않으면
        a = q.pop(0)  # 큐 리스트에서 원소를 꺼내서
        print(a, end=' ')   # 방문 흔적을 프린트한다.
        for i in graph[a]:  # a인덱스에 있는 연결정점들을 확인해서
            if b_visited[i] == 0:  # 방문하지 않았다면
                q.append(i)  # 큐 리스트에다가 집어넣어주세요
                b_visited[i] = 1  # 그리고 방문표시를 해준다.



N, M, V = map(int,input().split())   # [[], [2, 3, 4], [4], [4], []]
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)  # dfs용 방문표시
b_visited = [0] * (N+1)  # bfs용 방문표시
for _ in range(M):  # 방문할 수 있는 정점이 여러개이다 => 인접리스트이므로 그래프에 모두 넣어야한다.
    p, c = map(int,input().split())
    graph[p].append(c)
    graph[c].append(p)
# 숫자가 작은 순서대로 움직여야 하므로 그래프를 정렬해주어야 한다.
for i in range(1,N+1):  # 인덱스가 1부터 시작하고 N+1 개만큼의 리스트를 만들어놨기 때문에
    graph[i].sort()  # 큰 그래프를 순회하면서 정렬해주기

dfs(V)
print()  # 사이 간격을 해줘야댐(왜냐면 end ' ' 때문에 붙어서 나옴)
bfs(V)

