N = 4
stages = [4, 4, 4, 4, 4]

def solution(N, stages):
    answer = []
    dict_stage = {}  # 스테이지 진행상황 정리 {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  => {1: 1, 2: 3, 3: 2, 4: 1, 5: 0}
    length = {}  # 스테이지 별 길이 {1: 0, 2: 0, 3: 0, 4: 0, 5: 0} => {1: 8, 2: 7, 3: 4, 4: 2, 5: 1}
    fail_rate = {}  # 실패율 정리 {1: 0, 2: 0, 3: 0, 4: 0, 5: 0} =>
    
    # 딕셔너리 생성
    for i in range(1, N+1):
        dict_stage[i] = 0
        length[i] = 0
        fail_rate[i] = 0
    
    # 스테이지 진행상황 정리하기
    for stage in stages:
        if 1 <= stage <= N:
            dict_stage[stage] += 1
        else:
            continue
    
    # 스테이지 별 길이, 실패율 저장하기
    for i in range(1, N+1):
        length[i] = len(stages)
        while True:
            if i in stages:
                stages.remove(i)
            else:
                break
        fail_rate[i] = (dict_stage[i]/length[i])
    
    # 최종 정답을 위해 튜플로 실패율을 만들고 비교한 뒤 정렬
    # [(3, 0.5), (4, 0.5), (2, 0.42857142857142855), (1, 0.125), (5, 0.0)]
    result = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)
    
    # 최종 튜플 중 인덱스만 최종 정답에 더하기
    for x, y in result:
        answer.append(x)
        
    return answer

print(solution(N, stages))