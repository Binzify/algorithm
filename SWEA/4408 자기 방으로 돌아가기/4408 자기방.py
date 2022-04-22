import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc+1):
    r = 400   # 전체 방의 개수
    hall = [0]*(r//2)  # 방이 양쪽으로 위치해있으므로 복도는 그 절반임
    N = int(input())  # 돌려보내야 하는 학생 수

    for i in range(N):  # 돌려보낼 학생 수만큼 for 문 돌기
        h, m = map(int, input().split())  # H : here 현위치 M : move 이동시킬 방번호
        if h < m :  # 현 위치방이 이동시킬 방번호보다 작다면 (이동시킬 방이 큰 수면)
            if h % 2 ==1 and m % 2 == 1:  # 홀 -> 홀번방
                for move in range(h//2, m//2 + 1):  # 해당몫값에서 홀수 번호 해당 인덱스 +1
                    hall[move] += 1  # 1에서 3번방 가면 인덱스 0,1 복도에 +가 됨
            elif h % 2 == 1 and m % 2 == 0 :  # 홀 -> 짝
                for move in range(h//2, m//2):
                    hall[move] += 1
            elif h % 2 == 0 and m % 2 == 1 :  # 짝 -> 홀
                for move in range(h//2-1, m//2+1):
                    hall[move] += 1
            else :  # 짝 -> 짝
                for move in range(h//2-1, m//2):
                    hall[move] += 1

        else:  # 현 위치의 방이 더 큰 숫자의 방이라면
            if h % 2 == 1 and m % 2 == 1:  # 홀 -> 홀번방
                for r_move in range(h//2, m//2-1, -1):  # 해당몫값에서 홀수 번호 해당 인덱스 +1
                    hall[r_move] += 1  # 1에서 3번방 가면 인덱스 0,1 복도에 +가 됨
            elif h % 2 == 1 and m % 2 == 0:  # 홀 -> 짝
                for r_move in range(h//2, m//2-2, -1):
                    hall[r_move] += 1
            elif h % 2 == 0 and m % 2 == 1:  # 짝 -> 홀
                for r_move in range(h//2-1, m//2-1, -1):
                    hall[r_move] += 1
            else:  # 짝 -> 짝
                for r_move in range(h//2-1, m//2-2,-1):
                    hall[r_move] += 1

        hour = 0  # 복도에 흔적을 남기고 가는데 중첩되는 부분에는 1이상이 표시될 것
        for h in hall:
            if h > hour:
                hour = h
    print(f'#{t} {hour}')


