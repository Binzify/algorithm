P, K = map(int,input().split())
'''
에라토스테네스의 체 : 소수 구할 때 손쉽게 찾아내는 방법
n = int(input())                        # 2부터 n까지의 소수 찾기위해 n 입력
a = [False, False] + [True] * (n - 1)   # 1은 소수가 아니고 인덱스가 수를 의미하기 위해 원소는 n + 1개
primes=[]                               # 소수 모음
for i in range(2, int(n ** 0.5) + 1):   # 2부터 n의 제곱근까지
  if a[i]:                              # i가 소수이면(True) 소수 모음에 추가
    primes.append(i)
    for j in range(2 * i, n + 1, i):    # i를 제외한 2 * i부터 모든 배수 지움
        a[j] = False
print(primes)
'''
K -= 1  # K보다 작은 소수이므로 -1을 해둔다
a = [False, False] + [True] * (K - 1)
primes = []
for i in range(2, K + 1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, K + 1, i):
            a[j] = False

result = 'GOOD'
for prime in primes:
    if P % prime == 0:
        result = f'BAD {prime}'
        break
print(result)