import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

nodes = [[] for _ in range(N+1)]  # 주어진 N개 인덱스가 마지막 노드번호이므로
parent = [0]*(N+1)  # 부모가 누구인지 번호 만들어주기
# 양방향 그래프이므로 인접리스트로 만들어줌
for _ in range(N-1):
    p, c = map(int,input().split())
    nodes[p].append(c)
    nodes[c].append(p)

def dfs(start):
    for i in nodes[start]:
        if parent[i] == 0:  # 부모 노드를 모르는 경우에
            parent[i] = start  # 시작 노드를 부모로 지정해준다.
            dfs(i)  # dfs로 다음 노드로 이동한다음 부모 지정해준다.

dfs(1)  # 1번부터 돌자

# 2번 노드의 부모부터 뽑아주기
for node in range(2,N+1):
    print(parent[node])