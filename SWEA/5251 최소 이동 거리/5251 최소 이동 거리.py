import sys

sys.stdin = open('sample_input.txt')


def dijkstra(s):
    distance[s] = 0

    for i in range(nodes):
        for j in range(nodes):
            if distance[i] + graph[i][j] < distance[j]:
                distance[j] = distance[i] + graph[i][j]

    # 최종 도착지점에서의 최단 경로 출력
    return distance[N]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())  # N 마지막 노드번호, E 간선 개수
    nodes = N + 1
    INF = 987654321  # 최소값 비교를 위한 무한대 설정
    graph = [[INF] * nodes for _ in range(nodes)]  # 마지막 노드번호 +1개만큼 노드 생성
    distance = [INF] * nodes  # 최소 거리 값 저장을 위한 가중치 리스트

    for _ in range(E):
        s, e, w = map(int, input().split())  # s,e,w = 출발, 끝, 가중치
        graph[s][e] = graph[s][e] = w  # 그래프 만드는 방식 => 연결된 노드 위치에 가중치 입력하기
    print(graph)
    print(f'#{tc} {dijkstra(0)}')
