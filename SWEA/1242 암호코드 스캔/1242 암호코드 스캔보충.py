import sys
from pprint import pprint

sys.stdin = open('small.txt')

hex = [
    [0, 0, 0, 0],  # 0
    [0, 0, 0, 1],  # 1
    [0, 0, 1, 0],  # 2
    [0, 0, 1, 1],  # 3
    [0, 1, 0, 0],  # 4
    [0, 1, 0, 1],  # 5
    [0, 1, 1, 0],  # 6
    [0, 1, 1, 1],  # 7
    [1, 0, 0, 0],  # 8
    [1, 0, 0, 1],  # 9
    [1, 0, 1, 0],  # A
    [1, 0, 1, 1],  # B
    [1, 1, 0, 0],  # C
    [1, 1, 0, 1],  # D
    [1, 1, 1, 0],  # E
    [1, 1, 1, 1]  # F
]

# 3차원 배열, 해당하는 0과 1의 비율에 따라 암호값을 보낸다.
scode = [[[0] * 5 for _ in range(5)] for _ in range(5)]
scode[2][1][1] = 0
scode[2][2][1] = 1
scode[1][2][2] = 2
scode[4][1][1] = 3
scode[1][3][2] = 4
scode[2][3][1] = 5
scode[1][1][4] = 6
scode[3][1][2] = 7
scode[2][1][3] = 8
scode[1][1][2] = 9

def solve():
    result = 0 # 최종 합 출력할 것
    # 뒤에서 1을 찾아서 바로 위에 0이 있는 시작위치를 찾기
    for i in range(N):
        j = M * 4 - 1
        while j >= 55:
            if arr[i][j] == 1 and arr[i-1][j] == 0 :  # 1을 찾고 바로 위가 0인지 확인하기 (위에 0이여야 맨 처음 코드줄이라는 걸 알 수 있음)
                # 0 : 1 : 0 : 1 의 비율 구하기
                code = [0] * 8
                for k in range(7, -1, -1):
                    x = y = z = 0
                    while arr[i][j] == 1:
                        z += 1
                        j -= 1
                    while arr[i][j] == 0:
                        y += 1
                        j -= 1
                    while arr[i][j] == 1:
                        x += 1
                        j -= 1
                    while arr[i][j] == 0:  # 마지막 앞의 0은 돌리되 개수에는 포함시키지 않는다.
                        j -= 1
                        
                    # 1 : 0 : 1 의 비율을 찾아서 위에 scode에서 해당 암호를 code (암호)에 넣어준다
                    d = min(x, y, z)
                    x //= d
                    y //= d
                    z //= d

                    code[k] = scode[x][y][z]

                odd = code[0] + code[2] + code[4] + code[6]
                even = code[1] + code[3] + code[5] + code[7]
                if (odd * 3 + even) % 10 == 0:
                    result += odd + even
                j += 1
            j -= 1
    return result


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [[0] * (M*4) for _ in range(N)]

    # 16진수를 2진수로 변환해서 입력받기
    for i in range(N):
        temp = input()
        for j in range(M):
            ch = temp[j]
            if '0' <= ch <= '9':  # 아라비아 숫자
                dec = ord(ch) - ord('0')
            else:
                dec = ord(ch) - ord('A') + 10
            for k in range(4):
                arr[i][j*4+k] = hex[dec][k]  # 기존 값에서 한자씩 4배씩 늘어나야하므로
    print(f'#{tc} {solve()}')
