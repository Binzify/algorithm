import sys


sys.stdin = open('sample_input.txt')


def bubblesort(lst):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    subject = list(map(int, input().split()))
    bubblesort(subject)  # [80, 90, 100]
    maxscore = 0  # 최종 성적의 합을 구하기 위한 저장변수

    back = -1
    for _ in range(K):  # 어차피 K번 돌기 때문에 계속 빼주어도 인덱스 범위 넘지 않는다.
        maxscore += subject[back]
        back -= 1  # 맨 뒤의 값을 하나 더했으면 다음의 뒤로 이동한다.

    print(f'#{tc} {maxscore}')
