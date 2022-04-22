import sys


sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N, arr = input().split  # 우선 16진수 문자열 이므로
    result = ''

    # 16진수의 각 값을 10진수로 변환하기기
    for i in arr:
        tmp = int(i, 16)

        binary = bin(tmp).replace('0b','')

        while len(binary) < 4:
            binary = '0' + binary  # 0이 부족한 경우 앞에다가 추가해주기

        result += binary
    print(f'{tc} {result}')

