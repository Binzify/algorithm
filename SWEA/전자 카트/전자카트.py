import sys
sys.stdin = open('sample_input.txt')

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    office = [list(map(int,input().split())) for _ in range(N)]

    # 1-2-3-1, 1-3-2-1 순 으로 돈다는 의미는 부분집합 생각하면 될 듯
    # 모든 부분을 다 탐색하면서 최소 값을 구해주면 됨
    min_energy = 1000
    visit = [i for i in range(1,N)]  # 0부터 시작이지만 사무실이므로 1부터 시작
    moves = list(permutations(visit))  # [(1, 2), (2, 1)] 이런식으로 출력됨

    for move in moves:  # 만든 순열 리스트를 순회하면서
        used = 0
        idx = 0
        for p in move:  # 그 안의 각각 순서들을 뽑아서 배터리 소모량을 비교한다.
            used += office[idx][p]  # 순회하면서 소모한 배터리량 증가시키기
            idx = p  # 1-2-3 돌면 그 뒤는 2-3-1 순으로 돌아야하므로
        used += office[idx][0]  # 마지막 도착 지점 (사무실 복귀)
        if min_energy > used :
            min_energy = used

    print(f'#{tc} {min_energy}')
