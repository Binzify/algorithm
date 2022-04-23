import sys

sys.stdin = open('input.txt')


def DFS(s):
    global cnt
    v[s] = 1
    for i in connect[s]:
        if v[i] == 0:  # 만약 v[i] 가 방문하지 않은 곳이라면? if not 0 : 참
            cnt += 1
            DFS(i)


computer = int(input())
node = int(input())
connect = [[] * computer for _ in range(computer + 1)]  # 인접행렬 만들기 위한 리스트
v = [0] * (computer + 1)
cnt = 0

for _ in range(node):
    p, c = map(int, input().split())
    connect[p].append(c)
    connect[c].append(p)

DFS(1)

print(connect)
print(cnt)
