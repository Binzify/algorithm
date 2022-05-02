import sys
sys.stdin = open('input.txt')

'''
def dfs(s, cnt):
    visited[s] = 1
    for i in airplane[s]:
        if visited[i] == 0 :
            dfs(i, cnt+1)
        return cnt
'''
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    # # 트리 인접 리스트
    # airplane = [[] for _ in range(n+1)]
    # # 여행국가 방문체크
    # visited = [0] * (n+1)
    # cnt = 0

    for _ in range(m):
        a, b = map(int,input().split())
    print(n-1)




'''
airplane[a].append(b)
airplane[b].append(a)
print(airplane)

print(dfs(1, cnt))
'''