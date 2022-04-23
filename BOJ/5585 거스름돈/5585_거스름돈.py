yen = [500, 100, 50, 10, 5, 1]
cnt = [0] * 6

price = int(input())
pay = 1000
change = pay - price

for i in range(len(yen)):
    if change >= yen[i]:
        cnt[i] += change // yen[i]
        change %= yen[i]
    else:
        continue

print(sum(cnt))
