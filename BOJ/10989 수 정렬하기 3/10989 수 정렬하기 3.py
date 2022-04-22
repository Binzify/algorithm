import sys
N = int(sys.stdin.readline())

numbers = [0] * 10001

for _ in range(N):
    number = int(sys.stdin.readline())
    numbers[number] += 1
    # 숫자 표시 리스트에 확인시키기
for i in range(10001):
    if numbers[i] != 0:  # 만약 해당하는 숫자가 존재한다면
        for j in range(numbers[i]):  # 해당하는 숫자가 존재하는 수만큼 돌면서
            print(i)  # 해당 숫자를 출력한다.