import sys


sys.stdin = open('input.txt')


def onoff(num):  # 스위치 조작하는 함수
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return


N = int(input())  # 스위치의 개수
switch = [2] + list(
    map(int, input().split())
)  # 받는 숫자랑 스위치 위치 숫자랑 동일하게 만들기 위해 앞에 연관없는 1개의 수를 넣음

students = int(input())  # 스위치 조작할 학생들의 수
for stud in range(students):
    gender, number = map(int, input().split())
    if gender == 1:
        for i in range(
            number, N + 1, number
        ):  # 남자는 배수로 가는데, 주어진 수를 리스트범위(N개 +1내가 추가한)만큼 배수대로 감
            onoff(i)
    else:  # 여자일 때 여자는 받은 번호 위치의 -1과 +1이 같으면 스위치를 바꾸고 그렇지 않으면 받은 번호만 바꾼다.
        onoff(number)
        for j in range(N + 1 // 2):  # 반을 잘라서 비교해도 됨 (회문)
            if number + j > N or number - j < 1:  # 인덱스 범위를 벗어나는 경우라면
                break  # 본인 스위치만 바꾸고 끝내버린다.
            if switch[number - j] == switch[number + j]:  # 양쪽의 스위치 상태가 같다면
                onoff(number - j)
                onoff(number + j)
            else:  # 양쪽 스위치 상태가 같지 않으면 끝
                break

# 스위치 개수가 100개까지 나오는데 20개씩 잘라서 출력한다.
for p in range(1, N + 1):  # 나는 1개를 추가해놔서 1부터 N+1이 범위가 된다.
    print(switch[p], end=' ')
    if p % 20 == 0:  # 20개가 넘어가면 한 줄 추가하기
        print()
