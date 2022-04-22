import sys


sys.stdin = open('sample_input.txt')

def in_order(v):
    global num
    if v < N+1:
        in_order(v*2)
        nodes[v] = num
        num += 1
        in_order(v*2+1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = [0] * (N+1)  # 마지막번호까지 존재하므로 앞에 0만 있으면 된다.
    num = 1  # 노드에 넣어주는 수
    in_order(1)
    print(f'#{tc} {nodes[1]} {nodes[N//2]}')

