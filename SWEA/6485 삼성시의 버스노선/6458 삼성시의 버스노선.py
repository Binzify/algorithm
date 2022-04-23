import sys

sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    result = dict()  # 결과를 저장할 딕셔너리

    for i in range(1, 5001):  # 미리 딕셔너리를 생성해둔다. 1번부터 5000번까지
        result[i] = 0

    for _ in range(N):  # N만큼 돌려서
        a, b = map(int, input().split())  # 시작과 끝 정류장을 받은다음
        for i in range(a, b + 1):  # 첫번째 시작, 끝 정류장을 받으면 그 구간을 범위로 설정해서
            result[i] += 1  # 딕셔너리에 +1 을 해준다.

    P = int(input())  # 마지막 P 돌릴 횟수를 받아서
    busstop = []  # 정류장 개수를 최종적으로 담을 리스트에
    for _ in range(P):  # for문을 돌려서
        busstop.append(result[int(input())])  # 정류장

    print(f'#{tc}', *busstop)
