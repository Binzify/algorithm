import sys


sys.stdin = open('input.txt')

# 10번의 테스트 케이스
for t in range(1, 11):
    (
        n,
        pwd,
    ) = (
        input().split()
    )  # 문자열로 받아버린다. # ['1', '2', '3', '8', '0', '9', '9', '0', '8', '4']
    real = []  # 스택으로 담을 패스워드

    # 패스워드에서 문자열을 하나씩 꺼내서 다음 것과 같은지 비교한 후 틀리면 스택에 넣는다.
    for i in pwd:  # 조건세우기
        if len(real) == 0 or real[-1] != i:  # 스택이 비어있거나 기존 스택의 마지막에 찾는 수가 없으면
            real.append(i)  # 해당하는 수를 스택에 집어넣는다.
        elif i == real[-1]:  # 만약 스택에 방금 들어온 수와 다음 수가 일치하면
            real.pop(-1)  # 스택에서 빼버린다.

    result = ''  # 리스트로 각각 담긴 번호를 하나로 붙이기
    for a in real:  # 스택의 담긴 진짜 비밀번호를 하나씩 result에 붙인다.
        result += a
    print(f'#{t} {result}')
