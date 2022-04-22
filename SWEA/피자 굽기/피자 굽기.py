import sys


sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())  # 화덕의 크기, 피자의 개수
    cheese = list(map(int,input().split()))  # [7, 2, 6, 5, 3]
    burn = []  # 화덕
    numbers = []  # 결과값 출력을 위해 피자 번호 붙이는 곳

    for i in range(N):
        burn.append(cheese[i])   # [7, 2, 6]
        numbers.append(i+1)  # [1, 2, 3]

    number = 0  # 새 피자를 넣기 위한 인덱스용 변수
    while len(burn) != 1:
        burn.append(burn.pop(0)//2)
        numbers.append(numbers.pop(0))
        if burn[-1] == 0 and N+number < M:  # 만약 치즈가 다 녹았고, 아직 녹여야 할 피자가 남아있다면
            burn.pop(-1)  # 화덕의 피자를 빼낸다. 그리고 해당하는 번호도 빼내버린다.
            numbers.pop(-1)
            burn.append(cheese[N+number])  # 4번 피자 넣으려면 cheese[3] 이므로
            number += 1  # 번호를 맞추기 위해 + 1을 해준다.
            numbers.append(N+number)  # 해당하는 피자 번호가 들어간다.
        elif burn[-1] == 0 and N+number == M:
            burn.pop(-1)  # 화덕의 피자를 빼낸다. 그리고 해당하는 번호도 빼내버린다.
            numbers.pop(-1)

    print(f'#{tc} {numbers[0]}')



