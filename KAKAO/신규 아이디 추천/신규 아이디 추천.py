def solution(new_id):
    answer = ''
    second_id = []

    # 1단계 대문자 > 소문자로 변경
    new_id = new_id.lower()

    # 2단계 -,_,. 제외 없애기
    for i in new_id:
        if i in '~!@#$%^&*()=+[{]}:?,<>/':
            continue
        else:
            answer += i

    # 3단계 . 중복 없애기
    # 가장 먼저 찾아서 나오는 . 의 인덱스
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 리스트에 담아서 나머지 처리해주기
    for i in answer:
        second_id += [i]
    answer = ''

    # 4단계 처음 또는 끝
    if second_id[0] == '.':
        if len(second_id) >= 2:
            second_id.pop(0)
        else:
            second_id = ['.']
    if second_id[-1] == '.':
        second_id.pop()

    # 5단계 아이디 빈 문자열인 경우
    if len(second_id) == 0:
        second_id.append('a')

    # 6단계 아이디 길이 16자 이상인 경우, 슬라이싱 후 마지막 마침표인지 확인
    if len(second_id) > 15:
        second_id = second_id[:15]
        if second_id[-1] == '.':
            second_id.pop()

    # 7단계 아이디 길이 2자 이하인 경우
    if len(second_id) <= 2:
        while len(second_id) != 3:
            second_id.append(second_id[-1])

    for i in second_id:
        answer += i
    return answer
