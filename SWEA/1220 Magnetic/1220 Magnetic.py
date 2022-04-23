import sys


sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    lst = [
        list(map(int, input().split())) for _ in range(N)
    ]  # 1 = N (아래로이동) 2 = S (위로이동)
    table = list(map(list, zip(*lst)))  # 받은 자석 리스트를 전치해줘서 열을 행으로 보게 만든다
    result = 0  # 교착 세기 위한 값 result += 1이 되며 최종 프린트할 결과값

    for i in range(N):
        front = 0  # 앞쪽부터 판단 N극이 >> S 극으로 떨어지는 것(전치해서 우측이동)
        back = N - 1  # 뒤쪽부터 판단 S 극이 << N극으로 떨어지는 것 (좌측이동)
        while front < N:  # 같은 N을 만나면 >>쪽으로 이동, S극 만나면 멈추고 교착상태
            if table[i][front] == 1:
                table[i][front] = 0
            elif table[i][front] == 2:
                break
            front += 1
        while back >= 0:  # 같은 S를 만나면 같이 떨어지므로 제거, N을 만나면 멈추고 교착
            if table[i][back] == 2:
                table[i][back] = 0
            elif table[i][back] == 1:
                break
            back -= 1

    for i in range(N):
        stack = []
        for j in range(N):
            if table[i][j] == 2 or table[i][j] == 1:
                stack.append(table[i][j])
