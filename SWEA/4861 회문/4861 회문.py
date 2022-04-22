import sys


sys.stdin = open('sample_input.txt')


tc = int(input())
for t in range(1, tc+1):
    N, M = map(int, input().split())  # 행, 열 (찾을 문자 길이)
    words = [input() for _ in range(N)]  # 행을 담은 문자 리스트 'GOFFAKWFSM'
    col_words = list(map(list, zip(*words)))  # 열로  출력하여 담은 문자 리스트 ['G', 'O', 'U', 'J', 'W', 'Q', 'O', 'T', 'U', 'Z']
    col_words = [''.join(a) for a in col_words]

    for i in range(N):  # N개의 행을 검색
        for j in range(N-M+1):  # 인덱스를 벗어나지 않고 원하는 길이만큼 찾기 위해
            if words[i][j:j+M] == words[i][j:j+M][::-1]:  # 문자열의 맨 앞과 맨 뒤가 같은 경우 10 반대의 10
                correct = words[i][j:j+M]
                print(f'#{t} {correct}')


            elif col_words[i][j:j+M] == col_words[i][j:j+M][::-1]:  # (열)부분 진행! 전치로 행 상태로 만들었으므로 같은 코드
                correct = col_words[i][j:j + M]
                print(f'#{t} {correct}')









