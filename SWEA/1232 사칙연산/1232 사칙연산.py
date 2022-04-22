import sys

sys.stdin = open('input.txt')

# 후위 순회를 해준다. 그림을 보았을 때 나누기가 먼저 실행되기 전에 뺄셈을 실행시켜야 하며 그것이 우측에 있으므로 R>V>L순으로 진행
def post_order(node):
    if len(problem[node]) == 2:
        return problem[node][1]
    else:
        l = post_order(problem[node][2])
        r = post_order(problem[node][3])

        if problem[node][1] == '+':
            return l + r
        elif problem[node][1] == '-':
            return l - r
        elif problem[node][1] == '*':
            return l * r
        else:
            return l // r


for tc in range(1, 11):
    N = int(input())
    problem = [input().split() for _ in range(N)]  # [['1', '-', '2', '3'], ['2', '-', '4', '5'], ['3', '10'], ['4', '88'], ['5', '65']]

    for susik in problem:
        i = 0
        # isdecimal 활용하여 문자열 중 연산자가 아닌 것은 정수로 변경한다.
        while i < len(susik):
            if susik[i].isdecimal():
                susik[i] = int(susik[i])
            i += 1

    # node 번호가 1부터 시작 -> 0은 사용하지 않음
    problem.insert(0, 0)
    print(f'#{tc} {post_order(1)}')
