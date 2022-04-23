import sys


sys.stdin = open('input.txt')

# def multi(a, b): 함수로 한번 정의해보고 싶다.
#     max_multiply = 0  # 최대 곱셈
#     if a > b :
#         long = a
#         short = b
#     else:
#         long = b
#         short = a
#     for i in range(len(long)-len(short)+1):
#         multiply = 0
#         for j in range(len(short)):
#             multiply += long[i+j]*short[j]
#     if max_multiply < multiply:
#         max_multiply = multiply
#     return max_multiply

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # N = a의 길이 M = b의 길이
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_multiply = 0  # 최대 곱셈

    if len(a) > len(b):  # 만약 a가 b보다 길다면
        for i in range(N - M + 1):  # 0 1 2  짧은게 긴거 안에서 도는 횟수
            multiply = 0  # 곱한 값을 저장하는 공간
            for j in range(M):  # 0 1 2  # 짧은 리스트에서 곱하는 횟수
                multiply += a[i + j] * b[j]  # 인덱스로 빼서 곱함
            if max_multiply < multiply:  # 곱한 값이 최대이면 저장
                max_multiply = multiply
    else:  # 위와 반대 경우! b가 a 보다 긴 경우
        for i in range(M - N + 1):
            multiply = 0
            for j in range(N):
                multiply += b[i + j] * a[j]
            if max_multiply < multiply:
                max_multiply = multiply

    print(f'#{tc} {max_multiply}')
