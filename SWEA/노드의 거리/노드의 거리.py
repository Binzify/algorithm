import sys


sys.stdin = open('sample_input.txt')


def bfs(start, goal):
    queue = [start]  # 출발 큐에 담기
    visited[start] = 1  # 방문 표시해주기
    while queue:
        n = queue.pop(0)  # 노드라는 변수에 시작할 번호를 넣는다
        for i in graph[n]:  # 해당 노드 번호와 연결된 노드들을 꺼내서
            if visited[i] == 0:  # 방문하지 않은 상태라면
                queue.append(i)  # 큐에 넣어주고
                visited[i] = visited[n] + 1  # 방문표시를 하되 이전 방문한 표시에 +1씩 움직인 거리를 표시해준다

    if visited[goal] != 0:  # 만약 목표 지점이 0이상이라면? (도달했다는 의미이므로)
        return visited[goal] - 1  # 최종 도달 간선을 구하기 위해 -1을 해준다 (노드의 개수 -1 = 간선)
    else:  # 만약 0이라면
        return 0  # 도달하지 않은 것이므로 0 처리를 해준다.


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 노드의 개수, 입력용 수
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        p, c = map(int, input().split())
        graph[p].append(c)
        graph[c].append(p)
    # 시작과 끝 노드
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G)}')
