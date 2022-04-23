penny = [25, 10, 5, 1]

T = int(input())
for _ in range(T):
    paid = int(input())
    change = []
    for i in range(4):
        if paid >= penny[i]:  # 주어진 값이 거스름돈보다 크다면
            change.append(paid // penny[i])
            paid %= penny[i]
        else:  # 거스름돈을 주지 못하는 경우에는 0을 집어넣어준다
            change.append(0)
    print(*change)
