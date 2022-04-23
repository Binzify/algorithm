import sys


sys.stdin = open('input.txt')


# 오름차순 정렬(x축을 기준으로 정렬)
def bubblesort(data):
    for i in range(len(data) - 1, -1, -1):
        for j in range(i):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


N = int(input())
L_H_list = []

for i in range(N):
    L, H = map(int, input().split())
    L_H_list += [[L, H]]  # 2차원 배열
bubblesort(L_H_list)  # x축을 기준으로 오름차순 정렬

# 높이가 제일 큰거 찾기
max_H = 0
max_seq = 0
for i in range(N):
    if L_H_list[i][1] > max_H:
        max_H = L_H_list[i][1]  # 높이 저장
        max_seq = i  # 가장 높을 때의 x값 저장


# 1. 최대 높이 전(앞부터 검사) -> 높이가 이전값보다 크면 높이 변경, 작으면 그대로
total = 0  # 최종값 변수
now_H = L_H_list[0][1]  # 처음 높이 저장
for i in range(0, max_seq):
    total += now_H * (L_H_list[i + 1][0] - L_H_list[i][0])  # y값 * x값
    if L_H_list[i][1] < L_H_list[i + 1][1]:  # 값이 커지면 현재 높이 변경
        now_H = L_H_list[i + 1][1]

# 2. 최대 높이
total += L_H_list[max_seq][1] * 1

# 3. 최대 높이 후(뒤부터 검사) -> 높이가 이전값보다 크면 높이 변경, 작으면 그대로
now_H = L_H_list[-1][1]
for j in range(N - 1, max_seq, -1):
    total += now_H * (L_H_list[j][0] - L_H_list[j - 1][0])  # y값 * x값
    if L_H_list[j][1] < L_H_list[j - 1][1]:  # 값이 커지면 현재 높이 변경
        now_H = L_H_list[j - 1][1]

print(total)
