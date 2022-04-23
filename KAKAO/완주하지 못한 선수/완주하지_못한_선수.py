participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    # 참여자와 완주자는 1명 차이이므로, 이름순대로 정렬을 한 후 원소를 하나씩 비교했을 때 두 원소의 이름이 다르다면 완주하지 못한 사람이다.
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]  # 다 돌았는데도 답이 안나오면 참여자의 맨 마지막 사람 정답


print(solution(participant, completion))
