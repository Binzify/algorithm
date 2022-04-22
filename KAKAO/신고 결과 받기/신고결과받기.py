def solution(id_list, report, k):
    info = {}  # 딕셔너리화 하기 {'muzi': 1, 'frodo': 2, 'apeach': 0, 'neo': 2}
    result = {}  # 최종 결과 딕셔너리화
    answer = []

    report = list(set(report))  # 중복은 1회로 치므로

    for id in id_list:
        info[id] = 0
        result[id] = 0

    for i in report:
        id, reporter = i.split()
        info[reporter] += 1

    for i in report:
        name, reporter = i.split()
        if info[reporter] >= k:
            result[name] += 1

    for key in result:
        answer.append(result[key])

    return answer