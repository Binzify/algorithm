import sys

sys.stdin = open('input.txt')

for i in range(1, 11):
    dump = int(input())  # 덤프를 할 수 있는 횟수
    boxes = list(map(int, input().split()))  # 블럭 층들이 담긴 리스트

    while dump:  # 덤프 횟수를 다 소진할 때까지
        high = boxes[0]  # 기준을 하나 설정함
        low = boxes[-1]  # 기준을 하나 설정함
        for box in boxes:  # 블럭
            if high < box:  # 가장 큰 블럭을 찾기 위해 여정
                high = box
            if low > box:  # 가장 작은 블럭을 찾기 위한 여정
                low = box
        boxes[boxes.index(high)] -= 1  # 가장 큰 블럭이 있는 박스의 위치를 찾은 후 값을 1 뺌
        boxes[boxes.index(low)] += 1  # 가장 작은 블럭이 있는 박스의 위치를 찾은 후 값을 1 더함
        dump -= 1  # 덤프 횟수 차감

    highest = boxes[0]  # 기준을 하나 설정함
    lowest = boxes[-1]
    for box_1 in boxes:
        if highest < box_1:  # 가장 큰 블럭을 찾기 위해 여정
            highest = box_1
        if lowest > box_1:  # 가장 작은 블럭을 찾기 위한 여정
            lowest = box_1
        result = highest - lowest  # 최고 높이 상자와 최고 낮은 상자의 값을 도출한다.

    print(f'#{i} {result}')
