import sys


sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dec = input().split()  # 받은 카드덱
    newdec = []  # 새로 섞은 덱, 최종 출력
    dec_a = dec[: N // 2]  # 절반을 나눈 덱
    dec_b = dec[N // 2 :]  # 절반을 나눈 덱 ( 홀수면 a덱 보다 한 장 더 많이 있다)

    if N % 2 == 1:  # 전체 카드 수가 홀수인 경우
        for i in range(N // 2):  # 몫만큼 돌면 된다. 이미 절반씩 나누었기 때문에
            newdec.append(dec_a[i])
            newdec.append(dec_b[i + 1])
        if len(newdec) != N:  # 만약 새로운 덱이 기존의 덱의 개수와 맞지 않다면
            newdec.append(dec_b[0])  # 남은 하단 덱의 카드를 추가한다.
    else:  # 짝수인 경우
        for i in range(N // 2):  # 몫만큼 돌면 된다. 이미 절반씩 나누었기 때문에
            newdec.append(dec_a[i])
            newdec.append(dec_b[i])
    print(f'#{tc}', *newdec)
