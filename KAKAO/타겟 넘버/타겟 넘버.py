numbers = [1, 1, 1, 1, 1]
target = 3


def solution(numbers, target):
    answer = 0

    def dfs(idx, total):
        nonlocal answer
        # 총 5번의 dfs를 진행했다면 그 결과값이 목표값과 맞는지 비교
        if idx == len(numbers):
            if total == target:
                answer += 1
            return
        # dfs 계속 반복 (하나는 양수 하나는 음수)
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])

    dfs(0, 0)
    return answer


print(solution(numbers, target))
