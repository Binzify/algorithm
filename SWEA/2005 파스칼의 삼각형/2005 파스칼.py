import sys


sys.stdin = open('input.txt')
# 메모이제이션 쓰고 싶었는데 memo에 뭘 넣어야 하는지 어려운 것 같습니다.
# 코드가 중복으로 돌지 않도록 하는 개념은 이해했는데 구현이 어렵습니다 ..ㅠㅠ

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]

    for i in range(N):  # 0 1 2 3
        for j in range(i+1):  # j는 i의 범위 +1 만큼, 0일때 0이여야 하므로, 1이면 0,1...
            if i == j :  # 양 끝에는 1로 감싸져있다.
                board[i][j] = 1
            else:  # 그 외에는 대각선 방향에서 숫자를 가져와서 더한다.
                board[i][j] = board[i-1][j-1] + board[i-1][j]

    print(f'#{t}')
    for i in range(N):  # 이중 포문 풀어주기
        for j in range(i+1):
            if board[i][j] != 0:
                print(board[i][j], end=' ')  # 숫자 간 공백
        print()  # 두번째 포문 돌고 다음 행에 입력
