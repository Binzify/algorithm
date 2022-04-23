answers = [1, 3, 2, 4, 2]


def solution(answers):
    answer = []
    # 수포자들의 정답 찍는 방식
    giveup1 = [1, 2, 3, 4, 5]
    giveup2 = [2, 1, 2, 3, 2, 4, 2, 5]
    giveup3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 맞은 개수 세어주기
    dict = {1: 0, 2: 0, 3: 0}

    # 정답 길이만큼 돌리기
    for i in range(len(answers)):
        if answers[i] == giveup1[i % len(giveup1)]:
            dict[1] += 1
        if answers[i] == giveup2[i % len(giveup2)]:
            dict[2] += 1
        if answers[i] == giveup3[i % len(giveup3)]:
            dict[3] += 1

    # 최대값 추출하기
    max_cnt = 0
    for j in dict:
        if dict[j] > max_cnt:
            max_cnt = dict[j]

    # 추출한 최대값에 해당하는 수포자의 번호 찾기
    for key, value in dict.items():
        if value == max_cnt:
            answer.append(key)

    return answer


print(solution(answers))
