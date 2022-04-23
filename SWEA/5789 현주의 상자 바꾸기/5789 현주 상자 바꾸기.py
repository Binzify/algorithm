import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc + 1):
    N, Q = map(int, input().split())  # N과 Q 값을 입력받기
    box = [0] * (N + 1)  # 상자의 개수를 문제에 주어진 수처럼 작성 (1부터 슬라이싱하여 출력)
    for j in range(1, Q + 1):
        L, R = map(int, input().split())
        for i in range(L, R + 1):
            box[i] = j
    print(f'#{t}', *box[1:])
