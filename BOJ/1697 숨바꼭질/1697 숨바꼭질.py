import sys
sys.stdin = open('input.txt')

def bfs(N, K):
    q = [N]
    while q:
        subin = q.pop(0)
        if subin == K:  # 종료조건 설정
            print(visited[subin])
            break
        for move_subin in [subin - 1, subin + 1, subin * 2]:  # 수빈아 이동해!! 순간이동, 좌,우 이동
            if 0 <= move_subin < 100001 and visited[move_subin] == 0:
                visited[move_subin] = visited[subin] + 1  # 수빈이가 이동했던 횟수 + 1을 새로 저장
                q.append(move_subin)  # 새롭게 수빈이를 이동시켜주자

N, K = map(int,input().split())  # 수빈 / 동생 위치
visited = [0] * 100001  # 최대 100000만까지 이동할 수 있으므로
bfs(N, K)

