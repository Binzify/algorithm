import sys


sys.stdin = open('sample_input.txt')

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))

    for _ in range(m):
        back = queue.popleft()
        queue.append(back)
    print(f'#{tc} {queue[0]}')

    # queue = list(map(int,input().split()))
    #
    # for _ in range(m):
    #     a = queue.pop(0)
    #     queue.append(a)
    # print(f'#{tc} {queue[0]}')
