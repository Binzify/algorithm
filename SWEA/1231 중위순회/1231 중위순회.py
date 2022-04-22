import sys


sys.stdin = open('input.txt')

# 문제에서 완전 이진트리이기 때문에 중간에 정점이 비어있지 않는다.

# 중위순회 (L V R)
def in_order(v):
    global result
    if v:  # 인덱스 0은 방문하지 않는다.
        in_order(ch1[v])
        result += letters[v]
        in_order(ch2[v])


for tc in range(1,11):
    v = int(input())  # 정점의 개수
    letters = [0] * (v+1)
    ch1 = [0] * (v+1)  # 왼쪽 자식
    ch2 = [0] * (v+1)  # 오른쪽 자식
    result = ''

    for i in range(v):
        word = input().split()
        if len(word) == 4:
            letters[int(word[0])] = word[1]
            ch1[int(word[0])] = int(word[2])
            ch2[int(word[0])] = int(word[3])
        elif len(word) == 3:
            letters[int(word[0])] = word[1]
            ch1[int(word[0])] = int(word[2])
        else:
            letters[int(word[0])] = word[1]
    in_order(1)
    print(f'#{tc} {result}')
