import sys
sys.stdin = open('input.txt')

# 100 * 100 짜리의 도화지 생성 [0]*100개 * 100번
area = [[0]*100 for _ in range(100)]

for _ in range(4):  # 주어지는 값을 각 좌표 시작, 끝 지점으로 받아내기
    x1, y1, x2, y2 = map(int, input().split())
    # 받은 좌표값을 area에다가 찍어버리기!
    for x in range(x1, x2):
        for y in range(y1, y2):
            area[x][y] += 1

# 1 또는 그 이상으로 채워진 도화지에서 1이상인 경우를 카운트해서 넓이를 구한다.
count = 0
# 두 개의 리스트를 빠져나오려면 어떻게 해야할까?
# 이중 리스트 중 바깥의 area 리스트를 빼낸다.
# 그리고 그 안의 빼낸 리스트를 또 빼낸다.
for i in area:
    for result in i:
        if result > 0:
            count += 1

print(count)