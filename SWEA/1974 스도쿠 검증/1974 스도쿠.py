import sys


sys.stdin = open('input.txt')


def check(lst):
    global result, total
    # 행 검사하기
    for i in range(9):
        sumnum = 0
        for j in range(9):
            sumnum += lst[i][j]
        if sumnum != total:
            result = 0
            return

    # 열 검사하기
    for i in range(9):
        sumnum = 0
        for j in range(9):
            sumnum += lst[j][i]
        if sumnum != total:
            result = 0
            return

    # 3x3 배열 검사하기
    for n in range(0, 7, 3):  # 0 3 6
        for m in range(0, 7, 3):  # 0 3 6
            sumnum = 0
            for i in range(3):
                for j in range(3):
                    sumnum += lst[i + n][j + m]
            if sumnum != total:
                result = 0
                return


T = int(input())
for tc in range(1, T + 1):
    sdoku = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠는 9x9이므로
    total = 45  # 1에서 9까지 다 더하면 45이다. 이를 행, 열, 3x3 배열의 합과 비교해서 결과 확인
    result = 1  # 최종출력값 (True 면 1 false면 0)
    check(sdoku)  # 함수를 실행해서 스도쿠의 값들을 확인한다.

    print(f'#{tc} {result}')
