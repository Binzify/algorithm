import sys


sys.stdin = open('input.txt')

def search_code(codes):
    global find_code
    # 배열을 돌며 1이 존재하는 곳 찾기 (암호가 있는 곳, 뒤에서부터 찾아서 슬라이싱)
    for i in range(N):
        for j in range(M-1, -1, -1):  # 뒤에서부터 찾아서 1발견하면 자르기 (앞에서 자르면 암호 개수가 맞지 않음 0으로 시작되는 경우도 있어서)
            if codes[i][j] == '1':
                find_code = codes[i][j-55:j+1]  # 56개 찾은 암호를 빈 문자열 공간에 넣어준다
                return find_code

secret = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
        '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
        '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())  # N=세로 M= 가로
    codes = [input() for _ in range(N)]
    find_code = ''
    result = []  # 암호 해독 후 암호를 저장할 공간
    search_code(codes)


    # 암호는 0과 1로 이루어진 7자리이므로 (0 1 2 3 4 5 6 7)
    start = 0  # 암호의 시작 인덱스
    end = 7  # 암호의 마지막 인덱스
    for _ in range(8):  # 총 8자리의 암호로 구성되어 있다.
        target = find_code[start:end]  # 슬라이싱은 원하는 인덱스자리의 +1을 해주어야 뒤에를 잘라서 그 인덱스 반환
        result.append(secret[target])
        # 슬라이싱 후 다음 번호를 자르기 위해 늘려준다.
        start += 7
        end += 7

    # 최종 비밀번호는 해독한 숫자들의 유효성 검사로 참인지 확인이 가능하다. (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드
    password = (result[0] + result[2] + result[4] + result[6]) * 3 + (result[1] + result[3] + result[5]) + result[7]

    if password % 10 == 0:
        print(f'#{tc} {sum(result)}')
    else:
        print(f'#{tc} 0')

