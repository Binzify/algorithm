import sys

sys.stdin = open('input.txt')


def binary_search(n):
    global cnt
    start = 0  # A 리스트 첫번째 인덱스 번호
    end = N - 1  # 리스트 A 길이의 -1 : 마지막 인덱스번호
    move = 0  # 이미 이동했는지 확인하기 -1 : 왼쪽이동 / 1 : 오른쪽 이동

    while start <= end:
        mid = (start + end) // 2
        if n == A[mid]:  # 해당하는 값을 찾은 경우
            cnt += 1  # 횟수를 하나 세어주고 끝내기
            break
        elif n < A[mid]:  # 만약 찾는 값보다 기준이 작으면, 끝 페이지 기준을 중앙 안쪽으로
            # 더 이상 움직일 왼쪽이 없거나 이미 왼쪽으로 이동한 상태이면 종료하기 (값이 없어서 왼쪽으로 이동해서 값을 찾는데 없다면)
            if move == -1:
                break
            else:
                move = -1
                end = mid - 1
        else:  # 반대로 오른쪽도 동일하게 해줌
            if move == 1:
                break
            else:
                move = 1  # 오른쪽 이동 표시하기
                start = mid + 1  # 반대라면 첫 시작지점을 중앙 다음칸으로 이동

    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0
    # 정렬한 상태로 A를 저장하기
    A.sort()

    for i in B:
        binary_search(i)
    print(f'#{tc} {cnt}')
