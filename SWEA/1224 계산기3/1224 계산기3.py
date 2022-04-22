import sys


sys.stdin = open('input.txt')

# 중위 -> 후위 -> 계산까지 진행하기
for tc in range(1, 11):
    chars = input().split()  # ['5', '3', '*', '+', '.']
    result = ''
    stack = []

    for char in chars:
        if char.isdecimal():
            stack.append(int(char))

        # 연산자가 들어왔을 때
        else:
            # 여는 괄호면 스택에 넣는다.
            if char == '(':
                stack.append(char)
            else:
                # 연산 시 숫자 순서 유의!!
                p1 = stack.pop()
                p2 = stack.pop()
                if char == '+':
                    stack.append(p2 + p1)
                elif char == '*':
                    stack.append(p2 * p1)

    print(f'#{tc} {result}')

