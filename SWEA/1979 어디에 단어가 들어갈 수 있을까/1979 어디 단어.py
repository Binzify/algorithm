import sys

sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    N, K = map(int, input().split())  # N = 배열 가,세 길이 K = 들어갈 단어 길이
    area = [list(map(int, input().split())) for _ in range(N)]  # NxN의 배열
    result = 0  # K단어가 들어간 칸을 체크할 변수
    # 행 확인하기
    for i in range(N):
        cnt = 0  # 1을 체크한 후, 새로운 행으로 들어가면 초기화 시킬 cnt 변수
        for j in range(N):
            if area[i][j] == 1:  # 1인지 확인
                cnt += 1  # 맞으면 1추가
            else:  # 1이 아니라면
                if cnt == K:  # 우선 cnt의 값이 K인지 확인
                    result += 1  # 맞으면 결과 +1
                cnt = 0  # 초기화
        if cnt == K:  # 맨 마지막 칸에서 끝나는 경우, K길이여도 세지 않고 끝나서 이를 추가
            result += 1  # 결과 +1

    # 열 확인하기 (행과 똑같이)
    for r in range(N):
        cnt = 0
        for c in range(N):
            if area[c][r] == 1:
                cnt += 1
            else:
                if cnt == K:
                    result += 1
                cnt = 0
        if cnt == K:
            result += 1

    print(f'#{t} {result}')
