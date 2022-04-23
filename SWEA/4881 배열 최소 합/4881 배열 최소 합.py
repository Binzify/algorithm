import sys


sys.stdin = open('sample_input.txt')


def minsum(idx):
    global total, mini
    if idx == N:
        return
    for i in range(N):  # 0 1 2
        total += arr[idx][i]


'''
0 1 2 순차적으로 돌면서 행은 자동적으로 range가 돌게 하고 
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [
        list(map(int, input().split())) for _ in range(N)
    ]  # [[2, 1, 2], [5, 8, 5], [7, 2, 2]]
    stack = []  # 열을 확인하고 비교할 스택
    check = [0] * N  # 내가 해당 열을 뽑았는지 체크할 리스트
    total = 0
    mini = 1e9

    for i in range(N):  # 0 1 2
        total += arr[i][j]
        if len(stack) == 0 or stack[-1] != j:  # 스택에 아무것도 없거나, 이미 채택한 열이 아니라면
            stack.append(j)  # 열 비교를 위해 열을 집어넣는다.
