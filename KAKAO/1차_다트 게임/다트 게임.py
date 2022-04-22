def solution(dartResult):
    answer = ''
    stack = []
    for score in dartResult:
        if score.isdecimal():  # 숫자면
            answer += score  # 문자열로 변환
        # 'S'의 경우는 1배이므로 스택에 넣기만 하기
        if score == 'S':
            stack.append(int(answer))
            answer = ''
        # 'D'는 제곱, 가장 최근에 넣은 값에 값 적용하기
        if score == 'D':
            stack.append(int(answer))
            answer = ''
            t2 = stack.pop()
            stack.append(t2**2)
        # 세제곱 계산
        if score == 'T':
            stack.append(int(answer))
            answer = ''
            t3 = stack.pop()
            stack.append(t3**3)
        # 두 배 적용하기
        if score == '*':
            if len(stack) == 1:
                stack[-1] = stack[-1]*2
            else:
                a1 = stack.pop()
                a2 = stack.pop()
                stack.append(a2 * 2)
                stack.append(a1 * 2)
        # 마이너스 적용하기
        if score == '#':
            stack[-1] = stack[-1]*(-1)
    # 스택에 저장된 숫자를 최종적으로 합한다.
    return sum(stack)

dartResult = '1D2S#10S'

print(solution(dartResult))
