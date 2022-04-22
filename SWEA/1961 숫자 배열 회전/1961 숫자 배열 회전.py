import sys


sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    # 전치써서 90도씩 돌려서 완성하기
    arr90 = list(map(list, zip(*arr[::-1])))  # [7, 4, 1] 이런 식으로 출력됨 이를 문자열로 변환하여 741 이렇게 바꾸기
    arr180 = list(map(list, zip(*arr90[::-1])))
    arr270 = list(map(list, zip(*arr180[::-1])))


    print(f'#{tc}')
    for i in range(N):  # 첫 줄, 두번째 줄, 세번째 줄 이렇게 배열만큼 줄의 위치에 맞게 문자열로 변환한 붙인 값을 출력함
        print(''.join(map(str, arr90[i])), end=' ')  # 741(1) 852(2) 963(3)
        print(''.join(map(str, arr180[i])), end=' ')  # 987(1) 654(2) 321(3)
        print(''.join(map(str, arr270[i])), end=' ')  # 369(1) 258(2) 147(3)
        print()  # 다음 출력 간격
