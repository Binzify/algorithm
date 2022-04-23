import sys


sys.stdin = open('input.txt')

# 혹시나 모를 내장함수 막힌 경우를 위하여!
def bubble(lst):
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


n, m = map(int, input().split())
row = [0, n]
col = [0, m]

cut = int(input())
for _ in range(cut):
    arrow, num = map(int, input().split())
    if arrow == 0:
        col.append(num)
    else:
        row.append(num)

bubble(row)
bubble(col)

cutrow = []
cutcol = []
for i in range(len(row) - 1):
    cutrow.append(row[i + 1] - row[i])
for i in range(len(col) - 1):
    cutcol.append(col[i + 1] - col[i])

bestpiece = 0
for a in cutrow:
    for b in cutcol:
        if bestpiece < a * b:
            bestpiece = a * b
# 최종적으로 가장 큰수들끼리 곱하면 된다.
print(bestpiece)

'''
n, m = map(int,input().split())
row = [0,n]
col = [0,m]

cut = int(input())
for _ in range(cut):
    arrow, num = map(int,input().split())
    if arrow == 0:  # 가로 자른다는 것은 열을 기준로 자른다는 것이므로 열 리스트에 넣는다.
        col.append(num)
    else:  # 세로로 자른다는 것은 행을 기준으로 자르는 것이므로 행 리스트에 넣는다.
        row.append(num)

row.sort()  # 정렬을 해줘야 큰 수에서 작은수를 빼는 식을 구현할 수 있다. (뒤-앞)
col.sort()

# 총 3번(가로로 2번, 세로로 1번) 잘렸기 때문에 종이의 가로는 2개, 세로는 3개가 나온다.
cutrow = []  # 가로 2개 [4, 6]
cutcol = []  # 세로 3개 [2, 1, 5]
for i in range(len(row)-1):
    cutrow.append(row[i+1]-row[i])  # 큰수 - 작은수 = 잘려진 조각의 가로 길이
for i in range(len(col)-1):  # 큰수 - 작은수 = 잘려진 조각의 세로 길이
    cutcol.append(col[i+1]-col[i])

# 최종적으로 가장 큰수들끼리 곱하면 된다.
print(max(cutrow)*max(cutcol))
'''
