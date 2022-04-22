import sys


sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total = 0  # 수확한 농작물의 개수 (최종 정답)
    mid = N//2  # 5//2 < 즉 중간의 조건이 있어야 점점 나아가면서 더한다.
    j = 0  # 마름모를 더할 것


    for i in range(N):  # 행을 내려가면서 열들을 더해야하므로
        if i == 0 or i == N-1:  # 만약에 맨위와 아래라면 이미 중앙을 더해놔서 계산 필요X
            total += arr[i][mid]
        elif i > 0 and i <= mid:  # 점점 마름모 늘어나는 경우 (계단형증가)
            j += 1
            for m in range(mid-j, mid+j+1):
                total += arr[i][m]
        elif i > 0 and i > mid :
            j -= 1
            for m in range(mid - j, mid + j + 1):
                total += arr[i][m]
    print(f'#{tc} {total}')