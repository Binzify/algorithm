import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline



def find_set(x):
    while x != p[x]:  # 대표원소가 아니면
        x = p[x]  # x가 가리키는 정점으로 이동
    return x


V, E = map(int,input().split())
tree = []
p = [i for i in range(V + 1)]  # 대표 원소 초기화시키기

for _ in range(E):
    a, b, c = map(int,input().split())
    tree.append([a,b,c])
# 가중치 기준으로 정렬하기
tree.sort(key=lambda x: x[2])
# MST에 포함된 간선의 가중치의 합 구하기
total = 0  # 가중치의 합

for s, e, w in tree:  # 가중치, 시작, 끝노드
    start_root = find_set(s)
    end_root = find_set(e)
    if start_root != end_root:
        if start_root > end_root:
            p[start_root] = end_root
        else:
            p[end_root] = start_root
        total += w
print(total)