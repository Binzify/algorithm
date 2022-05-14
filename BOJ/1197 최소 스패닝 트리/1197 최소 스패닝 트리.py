# 다시 문제 풀기 (pypyp로 돌리면 틀렸습니다 뜨고 ... python3으로 돌리면 시간초과 뜸)

from heapq import heappush
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline



def find_set(x):
    while x != p[x]:  # 대표원소가 아니면
        x = p[x]  # x가 가리키는 정점으로 이동
    return x


V, E = map(int,input().split())
tree = []

for _ in range(E):
    a, b, c = map(int,input().split())
    heappush(tree, (c,a,b))

p = [i for i in range(V + 1)]  # 대표원소 초기화

# N개의 정점이 있으면 사이클이 생기지 않도록 N-1개의 간선을 선택
# MST에 포함된 간선의 가중치의 합 구하기
N = V + 1  # 0~V번 까지의 정점
cnt = 0
total = 0  # 가중치의 합

for w, u, v in tree:  # N-1개의 간선 선택 루프
    if find_set(u) != find_set(v):  # 사이클을 형성하지 않으면 선택
        cnt += 1
        total += w  # 가중치의 합
        p[find_set(v)] = find_set(u)  # v의 대표원소를 u의 대표원소로 바꿈
        if cnt == N - 1:
            break
print(total)