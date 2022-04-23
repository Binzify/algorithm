import sys

sys.stdin = open('input.txt')


def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


T = int(input())
for tc in range(1, T + 1):
    S = int(input())  # 총 숫자의 개수
    special_l = [0] * S  # 숫자의 개수만큼의 빈 리스트
    numbers = list(map(int, input().split()))

    sort_l = bubble(numbers)  # 정렬된 리스트
    # 정렬된 리스트를 S//2만큼 슬라이싱을 해준다. 그럼 5개씩 나옴!!
    small = sort_l[: (S // 2)]  # -5 애초에 5개씩 뽑아서 정렬
    large = sort_l[(S // 2) :]  # 5

    # 분리를 완료했다면 for 문으로 특별한 정렬을 진행해준다.
    # 작은 경우에는 2칸씩 띄면서 1번부터 S까지 2칸씩 띄며 차례대로 입력
    # 큰 경우에는 0번부터 S-2(range로하면 S-1)까지 2칸씩 띄면서 차례대로 입력
    put_s = 0
    put_l = -1  # 오름차순이기 때문에 뒤에서부터 빼오기
    for sm in range(1, S, 2):
        special_l[sm] += small[put_s]
        put_s += 1

    for lg in range(0, S - 1, 2):
        special_l[lg] += large[put_l]
        put_l -= 1

    a = special_l[:10]  # 10개까지만 출력이기에

    print(f'#{tc} {" ".join(map(str, a))}')
