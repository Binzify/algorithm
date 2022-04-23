import sys

sys.stdin = open('2gin.txt')

tc = int(input())

# 이진탐색 함수 정의
def binary_search(P, target):  # 찾으려는 범위, 찾고자 하는 페이지 수
    start = 1  # 1페이지
    end = P  # 마지막 페이지
    cnt = 0  # 승리 조건 설정하기/ 책을 펼쳐본 횟수

    while True:  #  찾을 때 까지 반복
        mid = (start + end) // 2
        cnt += 1  # 한번 이진 탐색 시도 시 +1, 나중에 최종 펼친 횟수가 적은 사람이 우승
        if mid == target:  # 값을 찾은 경우에는 종료
            break
        else:
            if target < mid:  # 찾는 값보다 기준이 작으면 끝 페이지 기준을 중앙값으로 설정
                end = mid

            else:
                start = mid  # 찾는 값보다 기준이 크면 시작 페이지 기준을 중앙값으로 설정
    return cnt  # 최종 펼쳐본 횟수를 출력한다.


for t in range(1, tc + 1):
    P, Pa, Pb = map(int, input().split())

    # 각 함수 적용시키기
    A = binary_search(P, Pa)
    B = binary_search(P, Pb)

    #  책을 펼친 횟수가 적은 사람을 찾아낸다.
    if A > B:
        print(f'#{t} B')
    elif A < B:
        print(f'#{t} A')
    else:
        print(f'#{t} 0')
