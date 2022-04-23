import sys

sys.stdin = open('input.txt')

# 베이비 진 확인하기
def babygin(lst):
    for i in range(len(lst)):  # 리스트 길이만큼 돌아서
        if lst[i] == 3:  # Run이라면
            return 1  # 1 반환하여 트루

    for i in range(8):  # 0부터 7까지 돌기 (2장씩 추가 확인하므로 인덱스 범위 안벗어나도록 함)
        if lst[i] and lst[i + 1] and lst[i + 2]:
            return 1
    return 0


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    # 0~9까지의 숫자에 맞는 인덱스를 추가하기 위해 +1 해줌
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0

    # 카드 배분하기 => 베이비진 확인하기 => 우승자 확인
    for i in range(len(cards)):
        if i % 2 == 0:
            player1[cards[i]] += 1
            if babygin(player1):
                winner = 1
                break
        else:
            player2[cards[i]] += 1
            if babygin(player2):
                winner = 2
                break

    print(f'#{tc} {winner}')
