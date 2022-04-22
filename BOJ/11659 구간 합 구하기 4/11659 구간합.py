import sys


sys.stdin = open('input.txt')

# 직접 주어진 인덱스의 거리를 계산해서 구간합을 구하는 방식
# N, M = map(int, sys.stdin.readline().split())  # 리스트 수, 찾을 횟수
# arr = list(map(int, sys.stdin.readline().split()))  # 숫자 리스트
#
# for k in range(M):
#     result = 0  # 구간합을 더하고 출력할 변수
#     i, j = map(int, sys.stdin.readline().split())  # i부터 j까지 봐야하니까
#     if i-1 >= 0 and j < N+1:  # 인덱스 범위 안에서 살펴봐야한다.
#         if i == j :  # 마지막 엣지 케이스, i와 j 가 같은 경우를 살핀다
#             result += arr[j-1]
#         else:  # 그렇지 않은 경우에는 포문 돌려서 찾기
#             for s in range(i-1, j):  # 만약 1번째부터 3번째면 인덱스로는 0 1 2 탐색
#                 result += arr[s]
#         print(result)


# 리스트의 누적된 합들을 다 만들어둔 후 리스트 안에서 빼는 방식
N, M = map(int, sys.stdin.readline().split())  # 리스트 수, 찾을 횟수
lst = list(map(int, sys.stdin.readline().split()))  # 숫자 리스트
sum_lst = [0]  # 누적합을 더할 리스트, 인덱스 맞추기 위해 앞에 0 더해줌
sum_num = 0  # 누적합을 더할 변수

for k in lst:  # 구간합을 더하기
    sum_num += k
    sum_lst.append(sum_num)  # [0, 5, 9, 12, 14, 15]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())  # 빠르게 변수를 받아주기
    if i-1 >= 0 and j <= len(sum_lst):  # 인덱스 범위 설정
        print(sum_lst[j] - sum_lst[i-1])