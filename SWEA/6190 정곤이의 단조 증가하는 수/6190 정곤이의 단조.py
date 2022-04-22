import sys


sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))  # ['2', '4', '7', '10']
    tie = []
    for i in range(N-1):
        for j in range(i+1, N):
            tie.append(arr[i]*arr[j])

    thebest = -1  # 결과가 없으면 -1 출력해야하므로
    for num in tie:
        check = 0
        num = str(num)
        if len(num) == 1:  # 결과값이 1자리수면 비교할 수가 없으므로 끝내기
            check = 1
        else:
            for k in range(len(num)-1):  # 두 자리수거나 그 이상이면 비교할 때 현재 위치에서 다음 위치만 보면 됨
                if num[k] > num[k+1]:  # 근데 만약 다음 자리 수가 작으면 단조가 아니므로 끝내기
                    check = 1
                    break

        if check == 0:  # 만약 위에 안되는 조건에 안걸렸다면?
            if thebest < int(num):  # 최대값보다 그 단조 수가 크다면
                thebest = int(num)  # 최대값 변경해주기

    print(f'#{tc} {thebest}')





