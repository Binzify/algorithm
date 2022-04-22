import sys


sys.stdin = open('sample_input.txt')

def in_order(N):
    global cnt
    if N:
        in_order(ch1[N])
        cnt +=1
        in_order(ch2[N])
    return cnt


T = int(input())
for tc in range(1, T+1):
    E, N = map(int,input().split())  # 간선 수, 시작 번호
    arr = list(map(int,input().split()))
    V = E+2  # E + 2 ( 1개는 0 인덱스 1개는 불러오는 숫자에 맞는 인덱스 맞추기)
    ch1 = [0]*V  # 왼쪽 자식 노드
    ch2 = [0]*V  # 오른쪽 자식 노드
    cnt = 0

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c


    print(f'#{tc} {in_order(N)}')
