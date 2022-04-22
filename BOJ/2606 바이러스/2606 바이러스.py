import sys


sys.stdin = open('input.txt')

from collections import deque

def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    virus[v] = 1
    while q:
        c = q.popleft()
        for i in connect[c]:
            if virus[i] == 0 :
                cnt += 1
                q.append(i)
                virus[i] = 1



computer = int(input())  # 컴퓨터 개수
network = int(input())   # 연결된 쌍의 수
connect = [[] for _ in range(computer+1)]
virus = [0] * (computer+1)
cnt = 0
for _ in range(network):
    c1, c2 = map(int,input().split())
    connect[c1].append(c2)
    connect[c2].append(c1)

bfs(1)
print(cnt)

