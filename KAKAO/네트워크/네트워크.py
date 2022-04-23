computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n = 3


def solution(n, computers):
    def bfs(start):
        visited[start] = 1
        q = [start]
        while q:
            computer = q.pop(0)
            visited[computer] = 1
            for network in range(n):
                # 자기자신이 아니고 연결되어 있으며 아직 방문하지 않았다면
                if (
                    network != computer
                    and computers[computer][network] == 1
                    and visited[network] == 0
                ):
                    q.append(network)

    answer = 0
    visited = [0] * n  # 방문리스트
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer += 1
    return answer


print(solution(n, computers))
