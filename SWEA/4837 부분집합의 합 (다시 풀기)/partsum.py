import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n, k = map(int, input().split())
    result = 0

    # 정수 12개의 모든 부분집합 경우의 수
    for i in range(1 << 12):
        # 임시 부분 집합
        tmp_list = []
        # 임시 부분 집합의 합
        tmp = 0
        for j in range(12):
            if i & (1 << j):  # i가 부분집합인 경우
                tmp_list.append(j + 1)  # 그 값에 해당하는 원소를 넣음
                tmp += j + 1  # 임시 부분집합의 합
        if len(tmp_list) == n and tmp == k:
            result += 1
    print(f'#{tc} {result}')
