array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i in commands:
        start, end, pick = i
        # 정답에 정렬된 슬라이싱 리스트의 pick번째 숫자를 넣는다.
        answer.append(sorted(array[start-1:end])[pick-1])
    return answer

print(solution(array,commands))