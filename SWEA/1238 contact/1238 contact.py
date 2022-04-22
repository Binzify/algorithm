import sys
sys.stdin = open('input.txt')

def BFS(start):
    q = [start]  # 큐를 만들고 그 안에 시작 지점을 넣어준다.
    v = [0] * 101 # 최대 100개이므로 +1개를 더 해준다.
    v[start] = 1  # 시작지점 방문표시를 해준다.
    sol = start  # 현재 가장 멀리까지 간 지점을 솔루션으로 표시한다 (정답)

    while q:  # 큐가 다 돌동안
        c = q.pop(0)  # 큐에서 변수를 꺼내서
        if v[sol] < v[c] or v[sol] == v[c] and sol < c:  # 만약 이미 방문표시된 번호의 거리가 시작지점에서 더 멀다면
            sol = c  # 최종 정답을 바꿔준다.

        for j in range(1, 101):  # 1~100까지 있으므로
            if graph[c][j] and v[j] == 0:  # 큐에서 꺼낸 행을 기점으로 열을 다 순회하면서 1을 찾는다 (연결된 전화번호부) 그리고 그 지점이 방문한 곳인지 확인한다.
                q.append(j)  # 위의 조건에 부합하다면 새로운 지점으로 큐에 집어넣어주고
                v[j] = v[c] + 1  # 그 방문지점의 거리를 하나 더 늘려서 표시해준다.
    return sol

for tc in range(1,11):
    graph = [[0]*101 for _ in range(101)]  # 전화번호부 인덱스 최대 100까지 이루어지기 때문에
    # 인접행렬 그래프를 만들어주기 위해서 만들어주었다. graph[행][열] = 1을 넣어서 연결되어 있는 것이 있는지 확인해주기
    contacts, start = map(int,input().split())  # 연락 간선 수, 시작하는 지점
    phones = list(map(int,input().split()))
    # 인접 행렬 배열에 넣어주기
    for i in range(0, contacts, 2):  # 앞 번호 : 행 / 뒷 번호 : 열
        graph[phones[i]][phones[i+1]] = 1  # graph[행][열] = 1 을 해두어서 연결되어 있음을 나타냄
    answer = BFS(start)  # 최종 정답은 BFS의 시작 번호의 값을 받아온다.
    print(f'#{tc} {answer}')

# 초반에 미리 답들을 다 받아준 상태에서 함수를 작성해주기

