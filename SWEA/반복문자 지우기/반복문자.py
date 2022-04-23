import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc + 1):
    spell = list(input())  # ['A', 'B', 'C', 'C', 'B']
    stack = []

    # 만약 단어를 꺼냈을 때, 스택리스트에 문자가 없으면 넣고, 있으면 사라지게 만들기
    # 최종적으로 스택에 남은 스펠이 있는지 없는지 확인해서 return을 한다.
    # while spell:  # spell 리스트가 0이 되기 전까지
    for _ in range(len(spell)):  # 또는 받은 스펠 리스트의 길이만큼
        pk = spell.pop(0)  # spell의 0번 인덱스에 위치한 값을 뽑는다.
        if len(stack) == 0 or pk != stack[-1]:  # 만약에 스택에 글자가 없거나, 마지막에 들어간 스택 글자가 다르면
            stack.append(pk)  # 뽑은 글자를 스택에 넣어준다.
        # if pk not in stack or pk != stack[-1]: => stack.append(pk)  # 뽑은 글자를 스택에 넣어준다.
        else:  # 그게 아닌 경우라면 스택에서 지워준다 (기존 spell에서는 pop으로 뽑아냈으니 사라졌다)
            stack.pop(-1)  # pop을 쓰면 맨 뒤에 들어온 값이 사라진다.

    print(f'#{t} {len(stack)}')  # 최종적으로 스택에 남아있는 리스트의 길이만큼 출력해주면 된다.
