N = 4
stages = [4, 4, 4, 4, 4]


def solution(N, stages):
    answer = []
    fail_rate = {}  # 실패율 결과 담을 딕셔너리
    clear = len(stages)  # 스테이지에 도달한 플레이어 수

    for i in range(1, N + 1):
        if clear != 0:  # 스테이지 도달한 사람 수가 존재한다면
            remain = stages.count(i)  # 해당 숫자가 리스트에 몇 개 있는지 세기
            fail_rate[i] = remain / clear  # 남은 유저 / 스테이지에 도달한 플레이어 수
        else:
            fail_rate[i] = 0
        clear = clear - remain  # 최종 스테이지 깬 길이에서 이미 값을 구한 사람들의 수 빼기

    # 최종 정답을 위해 튜플로 실패율을 만들고 비교한 뒤 정렬
    # [(3, 0.5), (4, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0.0)]
    result = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)

    # 최종 튜플 중 인덱스만 최종 정답에 더하기
    for x, y in result:
        answer.append(x)

    return answer


print(solution(N, stages))
