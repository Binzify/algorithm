import sys


sys.stdin = open('input.txt')

for tc in range(1, 11): # 테스트 케이스 10회
    n = int(input())  # 글자 개수 찾기
    m = 8  # 배열 m x m (8)
    rowarr = [list(input()) for _ in range(m)]  # split으로 받지 말기
    colarr = list(map(list, zip(*rowarr)))  # 전치시키기
    cnt = 0

    for i in range(m):  # 행 돌기
        for j in range(m-n+1):  # 전체배열크기 - 찾는 글자 개수 + 1 (찾는 개수만큼 돌기)
            if rowarr[i][j:j+n] == rowarr[i][j:j+n][::-1]:
                cnt += 1
            if colarr[i][j:j+n] == colarr[i][j:j+n][::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')
