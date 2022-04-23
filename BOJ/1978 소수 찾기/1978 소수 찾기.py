# 에라토스테네스의 체
n = 1000
a = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

N = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for number in numbers:
    if number in primes:
        cnt += 1
print(cnt)
