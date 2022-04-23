import sys


sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T + 1):
    busstop = [0] * 1001  # 정류장 최대, 표시할 곳
    N = int(input())  # 노선의 수
    for _ in range(N):  # 노선의 수만큼 반복한다
        K, A, B = map(
            int, input().split()
        )  # K = 버스의 특징 1 일반 2 급행 3 광역급행 / A = 출발 번호 , B = 종점
        if K == 1:  # 일반인 경우 모든 정류장에 정차한다.
            for i in range(A, B + 1):  # 버스 정류장 시작점부터 종점 +1 (== 종점)까지
                busstop[i] += 1
        elif K == 2:  # 급행인 경우, A가 짝수면 짝수에만, 홀수면 홀수에만 정차한다. B에도 정차한다.
            for i in range(A, B, 2):
                busstop[i] += 1
            busstop[B] += 1
        else:  # 광역인 AB는 별도로 처리한다. A 짝수인 경우, A와 B사이의 모든 4의 배수
            busstop[A] += 1
            busstop[B] += 1
            for i in range(A + 1, B):  # A는 미리 처리해두고 그 다음 정류장부터 계산하기. 종점도 계산했으므로 종점-1 까지
                if (
                    A % 2 == 1 and i % 3 == 0 and i % 10 != 0
                ):  # 홀수인 경우 A와 B 사이의 3의 배수이면서 10의 배수가 아닌 번호 정류장
                    busstop[i] += 1
                elif A % 2 == 0 and i % 4 == 0:  # A가 짝수인 경우 A와 B 사이의 모든 4의 배수 번호 정류장
                    busstop[i] += 1

        maxstop = 0
        for i in busstop:
            if maxstop < i:
                maxstop = i

    print(f'#{tc} {maxstop}')
