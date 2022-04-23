import sys

sys.stdin = open('sample_input.txt')

from itertools import combinations

# 중복되지 않는 조합 사용
def change_battery(lst):
    global change

    for i in range(len(lst)):
        charge = combinations(lst, i)
        for j in charge:
            if sum(j) + start == N:
                change = len(j)
                return change


T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, sys.stdin.readline().split()))
    N = arr[0]  # 정류장의 개수
    start = arr[1]  # 첫 시작지점에서 배터리 갖구 간다.
    battery = arr[2:]  # 정류장 이후의 배터리량 리스트
    change = 0  # 배터리 교체한 횟수
    print(f'#{tc} {change_battery(battery)}')
