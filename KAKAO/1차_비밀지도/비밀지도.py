n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    answer = []
    # n x n 배열의 지도이므로
    for i in range(n):  # 행 표시할 range
        secret_map = ''  # 두 지도를 동시에 합치는 방식 / 한 줄 채우고 초기화
        for j in range(n): # 열 표시
            if arr1[i] & (1 << j) | arr2[i] & (1 << j):  # 해당 배열에서 꺼낸 숫자와 j번째의 비트가 1인지 확인하기
                # 9 가 1001 이고 30이 11110 인데 이 두 개를 한번에 확인하여 벽을 표시해준다.
                secret_map += '#'  # 1이 있으면 벽이므로
            else:
                secret_map += ' '  # 0 이면 공백
        # 두번째 for 문이 다 돌면 정답 리스트에 넣어주기
        # 그대로 넣어주면 결과값이 반대로 나와서 역방향으로 넣어주기 (첨부터 저장할 때 방법이없나?)
        answer.append(secret_map[::-1])
    return answer

print(solution(n, arr1, arr2))