import sys

sys.stdin = open('sample_input.txt')


def brute_force_for(a, b):  # 브루트포스 함수
    N = len(b)  # 전체 텍스트 10
    M = len(a)  # 찾을 텍스트 4
    cnt = 0
    # 시작 위치 컨트롤
    for i in range(N - M + 1):  # 10-4+1 7
        for j in range(M):  # 4
            if b[i + j] != a[j]:  # 전체 텍스트의 문자가 찾는 문자와 같지 않으면
                break  # 종료!
        else:  # 찾았다면
            cnt += 1  # 카운트를 1 늘린다.
            return cnt
    return 0  # 없으면 0을 배출!


tc = int(input())
for t in range(1, tc + 1):
    word_a = input()
    word_b = input()

    print(f'#{t} {brute_force_for(word_a, word_b)}')
