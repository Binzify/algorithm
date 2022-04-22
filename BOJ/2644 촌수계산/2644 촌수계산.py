import sys
sys.stdin = open('input.txt')

def BFS(s):
    q = [s]
    v[s] = 1
    while q:
        next = q.pop(0)
        if next == end:
            return v[end]-1
        for i in relations[next]:
            if v[i] == 0:
                v[i] = v[next]+1
                q.append(i)
    return -1

people = int(input())  # 노드 수
start, end = map(int,input().split())  # 찾아야 하는 두 관계
relate = int(input())  # 간선 수
relations = [[]*(people+1) for _ in range(people+1)] # 인덱스 개수 하나 맞추기, 그래프 만들 때
v = [0] * (people+1)

for _ in range(relate):
    p1, p2 = map(int,input().split())
    relations[p1].append(p2)
    relations[p2].append(p1)

print(relations)
print(BFS(start))


