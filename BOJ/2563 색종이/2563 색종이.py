import sys

sys.stdin = open('input.txt')

# 100*100 도화지 만들기
paper = [[0] * 100 for _ in range(100)]

N = int(input())  # 색종이의 개수

for _ in range(N):  # 왼쪽과 오른쪽 변에서 떨어진 거리를 받는다.
    left_side, right_side = map(int, input().split())

    # 만들어지는 색종이의 크기가 10*10 배열이기 때문에 왼+10, 오+10 까지 1을 채워넣는다.
    for left in range(left_side, left_side + 10):
        for right in range(right_side, right_side + 10):
            paper[left][right] += 1


count = 0  # 넓이를 채운 1 또는 그 이상을 카운트하기 위해 만든 빈 변수
for height in paper:  # 도화지 세로 줄을 하나씩 뺀다. [0 * 100] 으로 이루어진 한 줄
    for width in height:  # 도화지의 가로 줄을 하나씩 뺀다. 0 0 0 0 0 0 0 << 요로코롬 한 개씩 빼본다.
        if width > 0:  # 그 중 1이상 속해있으면 넓이로 카운트한다.
            count += 1

print(count)  # 최종 카운트 값을 뺀다.
