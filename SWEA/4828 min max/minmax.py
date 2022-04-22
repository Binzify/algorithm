import sys
sys.stdin = open('input.txt')

tc = int(input())  # 테스트 케이스
for i in range(1, tc+1):
    N = int(input())  # 리스트에 들어가는 개수
    arr = list(map(int, input().split()))  # 리스트 만들기
    for j in range(N-1, 0, -1):  # 버블 소트 실행
        for k in range(j):
            if arr[j] < arr[k]:  # 리스트 첫번째와 두번째의 값을 비교
                arr[k], arr[j] = arr[j], arr[k] # 작은 값을 앞으로, 큰 값을 뒤로 두며 계속 진행 최종적으로 정렬되었을 때, 리스트 맨 뒤에 큰값, 그 바로 앞에 작은 값이 정렬된다.
        result = arr[-1] - arr[0]  # 오름차순 정렬된 리스트에서 가장 큰 수에서 작은수를 빼세요!
    print(f'#{i} {result}')