triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    n = len(triangle)  # 5
    # 이중 포문 돌리기
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:  # 만약 왼쪽 끝의 변에 위치해있으면
                triangle[i][j] += triangle[i - 1][j]  # 바로 우측 상방향의 값과 더한 후 기록
            elif i == j:  # 삼각형의 우측변에 위치한 경우
                triangle[i][j] += triangle[i - 1][j - 1]  # 왼쪽 대각선의 값과 더해서 기록한다.
            else:  # 그 외 양쪽 대각선의 값을 받아야 하는 경우, 더한 값 중에서 최대 값을 기록한다.
                triangle[i][j] = max(
                    triangle[i][j] + triangle[i - 1][j - 1],
                    triangle[i][j] + triangle[i - 1][j],
                )
    return max(triangle[n - 1])  # 최종적으로 마지막 리스트에서 최대값을 출력한다.


print(solution(triangle))
