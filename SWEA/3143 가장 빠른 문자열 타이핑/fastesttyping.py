import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc+1):
    A, B = input().split()  # A : aaaaa B : aa
    la = len(A)
    lb = len(B)
    cnt = 0  # 문자열을 치는 횟수
    tp = 0  # 입력할 위치 인덱스 typing position

    # 입력할 위치의 인덱스가 A문자의 길이를 넘지 않을 때까지 진행 (넘으면 타이핑 초과)
    while tp != la :
        if A[tp:tp+lb] == B:  # 첫번째 글자가 맞으면, 입력위치부터 B길이까지 슬라이싱 비교
            cnt += 1  # 입력 횟수는 1 증가시키고
            tp += lb  # 다음 입력할 인덱스는 B 글자의 다음부터 시작한다.
        else:
            cnt += 1  # 만약 자동완성단어랑 다르다면
            tp += 1  # 다음 타이핑 위치로 이동한다.

    print(f'#{t} {cnt}')
