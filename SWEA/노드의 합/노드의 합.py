import sys


sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # 노드 개수, 리프노드 개수, 출력해야할 노드
    tree = [0]*(N+1)  #인덱스 0 사용하지 않음  [0, 0, 0, 3, 1, 2]

    for i in range(M):  # 리프노드 개수만큼 돌려서 트리를 완성시킨다. 위에는 합이 들어갈 것이기에 0으로 설정
        node, num = map(int,input().split())
        tree[node] = num

    # 만약 짝수의 노드가 존재한다면 리스트 수를 맞춰줘야하므로 배열 리스트 추가
    if N % 2 == 0:
        tree.append(0)

    for idx in range(N//2, 0, -1):
        tree[idx] = tree[idx*2] + tree[(idx*2)+1]

    print(f'#{tc} {tree[L]}')