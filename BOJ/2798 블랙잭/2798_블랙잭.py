from itertools import permutations  # 순열 만들기 위한 라이브러리
import sys

sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))  # 카드 리스트
    mixcards = list(permutations(cards, 3))  # 3개씩 중복되지 않는 순열을 만든다.
    answer = 0  # 합을 넣을 값
    for i in mixcards:  # 튜플들을 꺼내서 합을 구함
        if sum(i) > answer and sum(i) <= M:  # 합이 기존 최대 합보다 크면서 범위를 넘지 않으면
            answer = sum(i)  # 정답으로 넣는다
    print(answer)  # 정답 출력
