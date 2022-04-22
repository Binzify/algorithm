import sys
sys.stdin = open('sample_input.txt')

# 프림 알고리즘
def mst_prim(graph,s):
    global distance
    visited[s] = 1  # 첫 시작 노드 방문표시
    distance[s] = 0  # 첫 시작 노드이기 때문에 스스로는 거리 0

    connect = 0  # 연결된 간선의 개수
    while connect < V:  # 모든 노드를 다 방문할 때까지 (최소신장트리는 nodes-1개의 간선을 가질때까지 반복되므로)
        for next_node in range(nodes):  # 노드의 개수만큼 for문을 돌려서 다음 이동할 노드의 가중치 확인
            if visited[next_node] == 0 and graph[s][next_node] < distance[next_node]:  # 다음 노드를 방문하지 않았고, 가중치가 작다면
                distance[next_node] = graph[s][next_node]  # 해당 가중치 입력 리스트에 그래프에 입력되어 있는 가중치를 입력한다.

        # 최소 가중치 값 입력해 둔 후 다음 노드를 돌 때 확인하기
        short_dis = INF    # 가장 작은 거리를 무한대로 우선 놔두고
        for next_node in range(nodes):  # 다시한번 노드를 순회하면서
            if visited[next_node] == 0 and distance[next_node] < short_dis:  # 위에서 입력된 가중치가 작은 값이라면
                short_dis = distance[next_node]  # 최소 거리 갱신 후
                s = next_node  # 다음 시작 노드를 다음 노드로 변경한다
        visited[s] = 1  # 그리고 방문표시를 진행한 다음
        connect += 1  # 한번 연결되었음을 표시한다.

    return sum(distance)  # 구성된 최소 신장 트리의 가중치 리스트를 다 더하면 정답이다.


T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())  # V 마지막 노드번호, E 간선 개수
    nodes = V+1
    INF = 9999  # 값 갱신을 위해 무한대를 표에 설정해둔다.
    graph = [[INF]*nodes for _ in range(nodes)]  # 마지막 노드번호 +1개만큼 노드 생성 [[9999, 1, 1], [1, 9999, 6], [1, 6, 9999]]
    visited = [0] * nodes  # 방문표시 확인 리스트
    distance = [INF] * nodes  # 가중치 입력 리스트 [0, 1, 9999] > [0, 1, 1]
    for _ in range(E):
        n1, n2, w = map(int,input().split())  # n1,n2 간선의 양 끝 노드, w 가중치
        graph[n1][n2] = graph[n2][n1] = w  # 그래프 만드는 방식 => 연결된 노드 위치에 가중치 입력하기

    print(f'#{tc} {mst_prim(graph,0)}')

