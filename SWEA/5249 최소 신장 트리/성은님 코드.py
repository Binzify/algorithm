import sys

sys.stdin = open('sample_input.txt')


def Prim(r):
    MST = [0] * (V + 1)  # 연결될 간선의 정보
    key = [10] * (V + 1)  # 가중치의 최대값 이상으로 초기화(문제에서 주어진 가중치의 최대값은 10)

    key[r] = 0

    for _ in range(V):
        u = 0
        min_W = 10

        for i in range(1, V + 1):
            if MST[i] == 0 and key[i] < min_W:
                u = i
                min_W = key[i]

        MST[u] = 1
        for v in range(V + 1):
            if MST[v] == 0 and graph[u][v] != 0:
                if key[v] > graph[u][v]:
                    key[v] = graph[u][v]

    return sum(key[r:])


# 입력받기
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 노드 간 선과 가중치의 정보를 입력 받기 전에 이를 바로 표시할 그래프 생성
    # 노드 번호가 0부터 시작하므로 인덱스 값이 0인 것부터 바로 시작
    graph = [[0] * (V + 1) for _ in range(V + 1)]

    # 두 노드는 서로 무방향이므로 대칭을 이루도록 연결된 곳에 가중치를 표시한다.
    for _ in range(E):
        n1, n2, weight = map(int, input().split())
        graph[n1][n2] = weight
        graph[n2][n1] = weight

    print(f"#{tc} {Prim(0)}")
