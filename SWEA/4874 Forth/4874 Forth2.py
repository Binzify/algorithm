import sys


sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    chars = input().split()  # ['5', '3', '*', '+', '.']
    result = ''
    stack = []

    for char in chars:
        if char.isdecimal():
            stack.append(int(char))

        # 연산자가 들어왔을 때
        else:
            # stack에 아무 숫자도 없으면 에러
            if not stack:
                result = 'error'
                break
            # stack에 숫자가 있을 때
            else:
                # 온점이 들어왔을 때
                if char == '.':
                    if len(stack) == 1:
                        result = stack.pop()
                        # break 안 한 이유 --> 어차피 마지막이니까
                    # stack에 남은 숫자가 1개 이상이면 에러
                    else:
                        result = 'error'
                # 연산자가 들어왔는데 stack에 숫자가 하나 밖에 없으면 에러
                elif len(stack) == 1:
                    result = 'error'
                    break
                else:
                    # 연산 시 숫자 순서 유의!!
                    p1 = stack.pop()
                    p2 = stack.pop()
                    if char == '+':
                        stack.append(p2 + p1)
                    elif char == '-':
                        stack.append(p2 - p1)
                    elif char == '*':
                        stack.append(p2 * p1)
                    elif char == '/':
                        stack.append(p2 // p1)

    print(f'#{tc} {result}')

