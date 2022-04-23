import sys

input = sys.stdin.readline
n = int(input())
numbers = sorted(list(map(int, input().split())))

for i in range(1, numbers[0] + 1):
    if n == 2:
        if numbers[0] % i == 0 and numbers[1] % i == 0:
            print(i)
    else:
        if numbers[0] % i == 0 and numbers[1] % i == 0 and numbers[2] % i == 0:
            print(i)
