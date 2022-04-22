import sys

sys.stdin =open('input.txt')

def bubblesort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())  # 2 2 2
    person = list(map(int, input().split())) # 1 2
    eat = 0  # 손님들이 사간 붕어빵의 개수 (양수이면 판매가 정상적으로 이루어진 것, 0이면 판매 불가함)

    # 도착하는 사람들의 시간을 오름차순으로 정렬한다.
    bubblesort(person)
    # 붕어빵 사러 온 사람들 체크하기
    for p in person:  # 사람들의 목록에서 차례대로 꺼내서
        make = (p//M)*K  # 방문할 때 존재하는 붕어빵의 개수 = (방문자의 방문시각//생성 걸리는 시간)*한번에 만들어지는 수 !!
        if make-eat > 0:  # 왔는데 붕어빵의 갯수가 있다면
            eat += 1  # 붕어빵 하나 팔렸습니다.
        else:  # 먹으러 왔는데 붕어빵이 없다면
            eat = 0  # eat을 0으로 만들어서 Impossible로 측정한다.
            break

    if eat > 0:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')


