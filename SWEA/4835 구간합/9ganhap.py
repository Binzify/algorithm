import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc+1):
    N, M = map(int, input().split())  # 10, 3
    arr = list(map(int, input().split())) # 1~ 10까지

     # 인덱스 값

    maxslice = 0  # 최대 슬라이스 값 비교용
    minslice = 0  # 최소 슬라이스 값 비교용
    idx = 0

    for i in range(N):
        slice = 0
        if idx + M < N+1 :  # 찾으려는 구간합의 마지막 인덱스 값이 N 보다 작으면 9 < 10
            for j in range(idx, idx + M):  # 012 123 234 345 ... 789
                slice += arr[j] # 3
            if i == 0:  # 처음 최대, 최소의 기준을 잡기
                maxslice = slice
                minslice = slice
                idx += 1
            if maxslice < slice :  # 최대보다 slice 가 더 크면 교체
                maxslice = slice
                idx += 1
            elif minslice > slice :
                minslice = slice
                idx += 1
            elif minslice < slice and maxslice > slice :  # 최대 최소에 속하지 않는 경우, 인덱스만 올려준다
                idx += 1


    print(f'#{t} {maxslice-minslice}')

