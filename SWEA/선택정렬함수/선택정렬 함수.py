numbers = [5,3,4,2,1]

def selection(numbers):
    for i in range(len(numbers)-1):  # 리스트의 길이 - 1 (마지막 원소 하나는 그대로 둠)
        # 최소값에 해당하는 인덱스를 0으로 놓고 시작한다.
        minidx = i
        # 그 다음 i 이후의 인덱스부터 살펴보며 더 작은 원소가 나오면 교환해줄 수 있도록 한다.
        for j in range(i+1, len(numbers)):  # 처음 선정한 인덱스부터 끝 인덱스까지 순회하며 작은 원소 찾기
            if numbers[minidx] > numbers[j]:  # 만약 현재 지정한 원소보다 크기가 작은 원소를 찾은 경우
                minidx = j  # 해당하는 인덱스 번호를 최소 인덱스로 지정해준다.
        numbers[i], numbers[minidx] = numbers[minidx], numbers[i]  # 그리고 위치를 바꿔준다.

        print(i, numbers)

selection(numbers)