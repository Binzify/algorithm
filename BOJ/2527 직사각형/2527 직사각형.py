import sys


sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    x1, y1, x2, y2, p1, q1, p2, p2 = map(
        int, input().split()
    )  # 3 10 50 60 100 100 300 300
    area = [[0] * 5000 for _ in range(5000)]
