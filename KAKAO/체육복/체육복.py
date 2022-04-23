n = 7
lost = [2, 3, 4]
reserve = [1, 2, 3, 6]


def solution(n, lost, reserve):
    # 학생들
    answer = [i for i in range(1, n + 1)]

    # 혹시 테케 18, 20 실패 이유... 혹시나 정렬 안된 상태로 리스트가 주어진 경우
    lost.sort()
    reserve.sort()

    # 옷 도난당한 사람 제외하기
    for no in lost:
        if no in reserve:  # 여분옷 있는데 도난 당한 경우
            reserve.remove(no)
        else:
            answer.remove(no)

    # 옷 가져온 사람꺼 빌리기
    for lent in reserve:
        if lent - 1 > 0 and lent - 1 not in answer:
            answer.append(lent - 1)
        elif lent + 1 <= n and lent + 1 not in answer:
            answer.append(lent + 1)
    return len(answer)


print(solution(n, lost, reserve))
