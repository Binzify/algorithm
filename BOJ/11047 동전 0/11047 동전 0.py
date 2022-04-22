import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]
money.sort(reverse=True)
cnt = 0

for i in money:
    if K >= i:
        cnt += K//i
        K %= i

print(cnt)