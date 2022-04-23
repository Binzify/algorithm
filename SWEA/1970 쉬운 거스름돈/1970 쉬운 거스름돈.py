import sys


sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    smoney = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    remoney = [0] * 8  # 거스름돈 카운팅
    money = int(input())  # 돌려줘야 할 거스름돈

    for i in range(len(smoney)):  # S 도시의 금액 종류만큼 범위 돈다
        a = money // smoney[i]  # a는 거스름돈을 각 금액으로 나눈 몫
        remoney[i] += a  # 거스름돈 개수 카운트에 몫을 더한다.
        money -= smoney[i] * a  # 그리고 잔돈에서 금액과 함께 몫을 곱한값을 빼준다. (거스름돈 준 돈 빼기)
    print(f'#{t}')
    print(*remoney)
