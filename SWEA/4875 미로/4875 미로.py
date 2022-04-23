import sys


sys.stdin = open('sample_input.txt')


def miro(x, y):
    global result
    maze[x][y] = 1
    for d in range(4):
        xi = di[d] + x
        yj = dj[d] + y
        if (0 <= xi < N) and (0 <= yj < N):  # 인덱스 범위 안에 있으면
            if maze[xi][yj] == 0:  # 0 : 갈 수 있는 길이라면
                miro(xi, yj)  # 재귀를 통해 다시 미로를 돈다.
            if maze[xi][yj] == 3:  # 만약 3을 만나게 되었다면
                result = 1  # 출력을 1로 전환해준다.
                return  # 그리고 재귀를 종료한다.


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 상 하 좌 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발 2 지점을 찾아서
                x, y = i, j  # 변수에 지정해 준 다음

    result = 0  # 출력을 위한 결과값
    miro(x, y)  # 미로 함수 돌기

    print(f'#{tc} {result}')
