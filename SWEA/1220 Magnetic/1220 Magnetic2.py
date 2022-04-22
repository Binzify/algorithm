import sys


sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]  # 1 = N (아래로이동) 2 = S (위로이동)
    result = 0  # 교착 세기 위한 값 result += 1이 되며 최종 프린트할 결과값

    for i in range(N):
        block = 0  # 교착 상태 확인하기
        for j in range(N):
            if table[j][i] == 1:  # 1을 확인하는 이유 : 1은 아래로 내려가는 성질이 있고, 2를 안만나면 통과, 만나면 교착이 되므로
                block = 1
            elif table[j][i] == 2:   # 2를 만나서 교착이 되어있고
                if block == 1:  # 만약 1을 위에서 만났다면
                    result += 1  # 카운트를 세준다
                    block = 0  # 블록 초기화

    print(f'#{t} {result}')
