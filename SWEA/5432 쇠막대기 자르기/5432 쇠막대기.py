import sys

sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc + 1):
    iron = input()
    cnt = 0  # 투입된 쇠막대기 갯수 세기
    sticks = 0  # 최종적으로 잘린 쇠막대기 갯수

    for i in range(len(iron)):
        if iron[i] == '(':
            cnt += 1
        else:  # ')'
            if iron[i - 1] == '(':  # ()
                cnt -= 1
                sticks += cnt  # 만약 레이저였다면, 기존 센 쇠막대기 개수에서 빼고 지금까지 센 막대기 저장
            else:  # 레이저가 아닌 경우에는 쇠막대기 끝부분이기 때문에
                cnt -= 1
                sticks += 1  # 개수를 빼고 잘린 막대기의 끄트머리를 더한다.

    print(f'#{t} {sticks}')
