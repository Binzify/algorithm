import sys


sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 선구안 할 수 있는 날의 수
    day = list(map(int, input().split()))
    best = day[-1]  # 최고 비싼 날을 맨 뒤로 기준으로 삼는다.
    profit = 0  # 판매 이익금을 더할 변수, 최종 출력값

    for i in range(N-1, -1, -1):  # 거꾸로 내려가면서 이익을 담아내면 된다. 맨 마지막을 이미 기준삼아서 셀 필요없음 길이-1
        if day[i] >= best:  # 만약 숫자가 최대값으로 설정한 값보다 크거나 같다면
            best = day[i]  # 최대값을 바꾼다. 아무런 행동도 하지 않음
        else:  # 숫자가 최대값보다 작다면
            profit += best-day[i]  # 이익 += 최대값 - 나온 숫자

    print(f'#{tc} {profit}')


