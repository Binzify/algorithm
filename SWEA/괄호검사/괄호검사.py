import sys


sys.stdin = open('sample_input.txt')

def check(lst):
    stack = []  # 여는 괄호를 넣을 스택
    for i in lst:
        if i == '(' or i == '{':  # 만약 꺼내온 i가 여는 괄호라면 스택에 넣는다.
            stack.append(i)
        if i == ')' or i == '}':  # 닫는 괄호가 나왔는데 비교할 여는 괄호가 없는 경우에는 바로 false인 0출력
            if len(stack) == 0:
                return 0
            elif i == ')':  # 닫는 괄호가 ) 이면 스택 마지막이 ( 인지 확인해서 없애기
                if stack[-1] == '(':  # 짝이 맞으면 스택에서 지워버리기
                    stack.pop(-1)
                else:
                    return 0
            elif i == '}': # 닫는 괄호가 } 이면 스택 마지막이 { 인지 확인해서 없애기
                if stack[-1] == '{':
                    stack.pop(-1)
                else:
                    return 0
    if len(stack) != 0:  # 만약 다 돌았음에도 불구하고 스택에 원소가 남아있다면
        return 0  # 짝이 안맞으므로 0 출력
    return 1  # 그렇지 않으면 True

tc = int(input())
for t in range(1, tc+1):
    stc = list(input())
    print(f'#{t} {check(stc)}')