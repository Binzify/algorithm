from itertools import permutations

numbers = "011"


def solution(numbers):
    # 에라토스테네스의 체
    n = 10 ** len(numbers)
    a = [False, False] + [True] * (n - 1)
    primes = []

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    answer = 0
    make_numbers = []
    for i in range(1, len(numbers) + 1):
        make_number = list(permutations(numbers, i))  # [('1',), ('7',)]
        for num in make_number:
            make_numbers.append(int(''.join(num)))
    for number in set(make_numbers):
        if number in primes:
            answer += 1
    return answer


print(solution(numbers))
