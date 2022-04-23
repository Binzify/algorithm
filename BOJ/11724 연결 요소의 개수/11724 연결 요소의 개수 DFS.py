import sys

sys.stdin = open('input.txt')

# dfs 구현
def dfs(n):
    # 방문하기
    visited[n] = True
    # 해당 노드와 연결된 노드들 확인
    for i in graph[n]:
        if not visited[i]:  # 그 노드가 방문된 노드인지 확인
            visited[i] = True
            dfs(i)  # 재귀로 또 들어가 확인
    return


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인접 리스트
visited = [False] * (N + 1)  # 방문 리스트 만들기
count = 0  # 정답 출력을 위한 카운팅

for _ in range(M):  # 간선 개수만큼 for문 돌리기
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    # 인접 리스트이므로 돌아가며 받아야 한다.

for i in range(1, N + 1):  # 주어진 노드 개수만큼 돌면서 연결된 집단 개수 세기
    if not visited[i]:
        dfs(i)
        count += 1
print(count)
