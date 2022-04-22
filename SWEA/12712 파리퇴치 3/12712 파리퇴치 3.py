import sys


sys.stdin = open('in1.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxkill = 0

    for i in range(N):
        for j in range(N):
            k = arr[i][j]
            # + 형태로 뿌려지는 경우
            # 델타 좌상우하
            di = [0, 1, 0, -1]
            dj = [-1, 0, 1, 0]

            for a in range(4):  # 델타 방향 순회
                for b in range(1, M):
                    ni = i + di[a] * b  # 주어진 스프레이의 최대거리까지 확인
                    nj = j + dj[a] * b
                    if 0 <= ni < N and 0 <= nj < N:
                        k += arr[ni][nj]
            if maxkill < k:  # 최대값 확인하기
                maxkill = k
            # 대각선 방향의 델타
            di = [1,1,-1,-1]
            dj = [1,-1,1,-1]
            k = arr[i][j]
            for a in range(4):  # 델타 방향 순회
                for b in range(1, M):
                    ni = i + di[a] * b  # 주어진 스프레이의 최대거리까지 확인
                    nj = j + dj[a] * b
                    if 0 <= ni < N and 0 <= nj < N:
                        k += arr[ni][nj]
            if maxkill < k:
                maxkill = k

    print(f'#{tc} {maxkill}')
