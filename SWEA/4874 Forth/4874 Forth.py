import sys


sys.stdin = open('sample_input.txt')


def check(lst):
    # 함수를 사용해서 연산자와 숫자의 갯수를 세서 처음부터 연산이 불가능한 경우에는 error 를 뽑도록 한다.
    global number, string
    for word in math:
        if word not in '+-*/.':
            number += 1
        elif word in '+-*/':
            string += 1
        else:
            string += 0
    return


T = int(input())
for tc in range(1, T + 1):
    math = input().split()  # ['5', '3', '*', '+', '.']
    stack = []
    number = 0  # 숫자를 셀 것
    string = 0  # 연산자를 셀 것
    result = 0
    check(math)

    if number > string:
        for word in math:
            if word not in '+-*/.':
                stack.append(int(word))
            else:
                if word == '+':
                    p1 = stack.pop()  # 2
                    p2 = stack.pop()  # 10
                    stack.append(p2 + p1)

                elif word == '-':
                    p1 = stack.pop()  # 2
                    p2 = stack.pop()  # 10
                    stack.append(p2 - p1)

                elif word == '*':
                    p1 = stack.pop()  # 2
                    p2 = stack.pop()  # 10
                    stack.append(p2 * p1)

                elif word == '/':
                    p1 = stack.pop()  # 2
                    p2 = stack.pop()  # 10
                    stack.append(p2 // p1)

                else:
                    if len(stack) == 1:
                        result = stack.pop()
                    else:  # 마침표가 나왔는데 스택에 2개이상 있다. 연산자 부족 > 에러
                        result = 1

    elif number <= string:  # 만약 연산자보다 숫자가 적은 경우 또는 연산자랑 숫자랑 같은 경우
        result = 1

    if result > 1:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} error')
