import sys


sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    maxcatch = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            catch = 0
            for ii in range(m):
                for jj in range(m):
                    catch += arr[i + ii][j + jj]
            if maxcatch < catch:
                maxcatch = catch

    print(f'#{tc} {maxcatch}')
