import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    work_list = []  # 작업 예약 목록

    for _ in range(N):
        s, e = map(int, input().split())
        work_list.append(
            (s, e)
        )  # 작업 예약 목록 [(20, 23), (17, 20), (23, 24), (4, 14), (8, 18)]

    # 끝나는 시간을 기준으로 내림차순 정렬하기
    work_list.sort(
        key=lambda x: x[1], reverse=True
    )  # [(23, 24), (20, 23), (17, 20), (8, 18), (4, 14)]

    # 첫 작업 시간 중 가장 빠른 사람의 시간을 기준으로 삼고 돌면서 작업 횟수 세기
    last_time = work_list[-1][1]  # 14
    max_cnt = 1  # 최대 작업 횟수 세기(정답) 이미 기준 하나 잡았으므로 1부터 시작
    while work_list:  # 작업 예약 목록에서 하나씩 빼면서 기준이 된 가장 빠른 사람의 시간과 비교하여 목록 정리
        start, end = work_list.pop()
        if last_time <= start:  # 가장 처음 시작한 사람의 끝난 시간에 시작하는 사람의 시간이 같거나 크다면 일할 수 있으므로
            last_time = end  # 그 끝난 시점을 새로 지정해주고
            max_cnt += 1  # 일할 횟수를 세어준다.
    print(f'#{tc} {max_cnt}')
