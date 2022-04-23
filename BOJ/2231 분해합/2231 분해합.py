import sys

sys.stdin = open('input.txt')

N = int(input())
for i in range(1, N + 1):  # 1부터 들어온 숫자까지 값 확인하기
    num = i
    for j in str(i):
        num += int(j)
    if num == N:
        print(i)
        break
    elif i == N:
        print(0)
