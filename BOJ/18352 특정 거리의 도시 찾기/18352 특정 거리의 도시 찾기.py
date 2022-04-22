import sys, heapq
sys.stdin = open('input.txt')


def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in cities[now]:
            length = dist + i[1]
            if length < distance[i[0]]:
                distance[i[0]] = length
                heapq.heappush(q, (length, i[0]))


n, m, k, x = map(int,input().split())
N = n+1
inf = int(1e9)
# 단방향 그래프 생성하기
cities = [[] for _ in range(N)]
visited = [0] * N  # 방문 체크
distance = [inf] * N  # 최단 거리 테이블 생성 후 무한으로 초기화시키기

for _ in range(m):
    a, b = map(int,input().split())
    cities[a].append((b, 1))  # 모든 거리가 1로 이루어져 있으므로 가중치 1을 함께 저장

dijkstra(x)

answer = -1
for i in range(1, n+1):
    if distance[i] == k:
        answer = 1
        print(i)

if answer == -1:
    print(answer)
