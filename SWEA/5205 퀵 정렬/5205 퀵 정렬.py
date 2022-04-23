import sys

sys.stdin = open('sample_input.txt')


def quick_sort(lst):
    if len(lst) <= 1:  # 만약에 리스트가 하나 또는 그 이하의 원소만 갖게 된다면 (본인만 포함된 것이므로) 종료
        return lst

    # pivot(비교 원소), end (비교 원소 외의 모든 구간)을 지정해준다.
    pivot, end = lst[0], lst[1:]
    left = []
    right = []
    for lr in end:  # 피봇 이외의 지점을 순회하면서
        if lr <= pivot:  # 비교할 원소보다 작거나 같다면 왼쪽(작은 리스트)에 넣어주기
            left.append(lr)
        else:  # 크다면 오른쪽에 넣어주기
            right.append(lr)
    # 이렇게 정렬된 리스트를 다시 재귀를 통해서 왼쪽도 정렬, 그리고 피봇의 위치, 그리고 오른쪽 정렬시키도록 한다.
    return quick_sort(left) + [pivot] + quick_sort(right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc} {quick_sort(arr)[N//2]}')
