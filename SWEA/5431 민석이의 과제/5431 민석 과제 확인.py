import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc+1):
    N, K = map(int, input().split())  # N 수강생 수 K 낸 사람 수
    students = []
    check = list(map(int, input().split()))  # 낸 학생들의 번호

    for i in range(1,N+1):  # 수강하는 학생들의 목록을 만들어준다.
        students.append(i)  # [1 2 3 4 5]

    for num in check:  # 낸 학생들을 빼내는 체킹
        students.remove(num)  # 리스트 목록에서 제거한다.

    print(f'#{t}', *students)

