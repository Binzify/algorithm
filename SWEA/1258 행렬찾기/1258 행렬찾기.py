import sys


sys.stdin = open('input.txt')

'''
행과 열을 기준으로 0이 아닌 수들을 계산하여 행, 열 리스트에 각각 담는다.
0이 아닌경우 카운트를 1개씩 올리고, 0인 경우 그 당시의 카운트를 각각 행,열 리스트에 담는다.
튜플로 행과 열을 저장한 이후에 튜플을 행을 기준으로 오름차순 정렬한다.
행과 열을 각각 뽑다가 만약에 행과 열이 같은 경우에는 한 개의 수만 리스트에 담고 넘어간다.
그렇게 담은 리스트를 최종적으로 언패킹하여 출력한다.
'''
# 행과 열을 저장하기 위해 만들 함수
def rowcol(lst):
    global rowlist, collist
    cnt = 0  # 행과 열을 체크할 변수
    # 행
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 0:
                rowlist += [cnt + 1]  # 행을 검사했을 때 0이 나오면 사각형의 총 크기가 끝이 난 것이므로 저장
            else:
                cnt += 1


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    container = [list(map(int, input().split())) for _ in range(n)]
    rowlist = []  # 행의 길이를 담을 리스트
    collist = []  # 열의 길이를 담을 리스트
    rowcol = []  # 최종적으로 행과 열의 묶음을 담을 리스트 (최종출력)

    print(f'#{tc}', *rowcol)
