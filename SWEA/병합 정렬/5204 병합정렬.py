import sys
sys.stdin = open('input.txt')

def merge_sort(lst):
    global cnt
    if len(lst) <= 1:
        return lst

    mid = len(lst)//2  # 병합 정렬을 위해 중앙을 잘라주기
    s_lst = merge_sort(lst[:mid])  # 작은 수를 정렬한 리스트
    b_lst = merge_sort(lst[mid:])  # 큰 수를 정렬한 리스트
    # 만약 작은 리스트와 큰 리스트를 다 정렬한 후, 합치기 전 교수님이 주어진 조건이 몇번이나 등장하는지 확인
    if s_lst[-1] > b_lst[-1]:  # 작은 리스트의 마지막과 큰 리스트의 마지막 비교했을 때 큰 경우
        cnt += 1

    merge_lst = []  # 병합할 리스트
    s = b = 0  # 인덱스 넘버링
    while s < len(s_lst) and b < len(b_lst):  # 리스트를 순회하면서 값을 비교하기
        if s_lst[s] < b_lst[b]:  # 만약 작은 리스트의 값보다 큰 리스트의 값이 크다면
            merge_lst.append(s_lst[s])
            s += 1
        else:
            merge_lst.append(b_lst[b])
            b += 1
    # 위의 와일문을 돌고 남은 값에 대해서 최종 병합 리스트에 추가해주기기
    merge_lst += s_lst[s:]
    merge_lst += b_lst[b:]
    return merge_lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    # 출력 : 머지소트함수에서의 중간값과 결과를 출력
    merge_lst = merge_sort(lst)
    print(f'#{tc} {merge_lst[N//2]} {cnt}')


'''
시간초과 뜨는 기존 함수
# 병합 정렬 안 함수 병합 구현
def merge(left, right):
    result = []
    # left, right 중 하나라도 존재하면
    while left or right :
        # left 와 right 모두 존재하는 경우
        if left and right :
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        # 왼쪽만 존재한다면 남은 것에 대한 처리
        elif left:
            result.append(left.pop(0))
        # 오른쪽만 존재한다면
        elif right:
            result.append(right.pop(0))
    return result

# 병합 정렬 구현
def merge_sort(a):
    global cnt
    # 기본 파트
    if len(a) == 1: return a
    # 유도 파트
    else:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        
        left = merge_sort(left)
		right = merge_sort(right)
		
		if left[-1] > right[-1]:
		    cnt += 1
        
        return merge(left, right)
'''