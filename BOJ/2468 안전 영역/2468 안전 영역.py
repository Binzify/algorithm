import sys

sys.stdin = open('input.txt')

N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
