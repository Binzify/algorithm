import sys
sys.stdin = open('input.txt')

from collections import deque
def bfs(start):
    global count
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        subin = q.popleft()
        # 만약 수빈이가 동생 위치 도달하면 횟수 1회 추가
        if subin == K:
            count += 1
        for move_subin in [subin - 1, subin + 1, subin * 2]:
            # 수빈이가 범위 안에 있고 + 움직인 수빈이가 기존 최단시간과 같거나 기록한 적이 없다면
            if 0 <= move_subin < 100001 and (visited[move_subin] == visited[subin]+1 or visited[move_subin] == 0):
                visited[move_subin] = visited[subin]+1
                q.append(move_subin)




N, K = map(int,input().split())  # 수빈 / 동생 위치
visited = [0] * 100001  # 최대 10만까지 이동할 수 있으므로
count = 0 # 빠른 횟수 세기
bfs(N)

print(visited[K]-1) # 최단시간
print(count)
