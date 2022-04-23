import sys


sys.stdin = open('input.txt')


def enq(key):
    global last
    last += 1
    tree[last] = key  # 완전 이진 트리 유지
    c = last  # 새로 추가된 정점을 자식으로
    p = c // 2  # 완전이진트리에서의 부모 정점 번호
    while (
        p >= 1 and tree[p] > tree[c]
    ):  # 부모존재, 최종에서 부모 노드를 쉽게 구하기 위해 노드 위치를 반대로 해두기 (원래는 p < c )
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 노드 개수
    nodes = list(map(int, input().split()))
    # 포화이진트리의 정점 번호 1~100까지 준비
    tree = [0] * (N + 1)  # 트리 구조 생성
    last = 0  # 마지막 정점 번호
    answer = 0  # 합을 담을 변수

    for node in nodes:
        enq(node)  # 완전 이진 트리 완성하기

    half = N // 2  # 완전 이진트리이므로 조상 노드를 구하는 것은 절반씩 잘라내면 알 수 있음
    for _ in range(half):
        answer += tree[half]
        half = half // 2  # 최종 노드 1번까지 갈 수 있도록 진행
    print(tree)
    print(f'#{tc} {answer}')
