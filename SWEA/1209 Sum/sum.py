import sys
sys.stdin = open('input.txt')

for i in range(10):  # 테스트 케이스 10개
    tc = int(input())
    area = [list(map(int, input().split())) for _ in range(100)]  # 100*100 배열
    best = 0  # 전체중에서 최고 값을 계속 저장해나간다.
    # 행의 합을 계속 최고 수를 저장하도록 만든다.


    for r in range(len(area)):
        row = 0
        for c in range(len(area[0])):
            row += area[r][c]  # area 0행부터 99행까지 합
        if row > best:
            best = row



    # 열의 합도 최고 수를 저장하도록 함
     for ca in range(len(area[0])): # len(area[0]) => area의 열의 길이
         col = 0
        for ra in range(len(area)):
            col += area[ra][ca]  # area 0열부터 99열까지 합
            if col > best:
                best = col


    # 대각선의 합 구하는 코드
    right_crs = 0
    left_crs = 0
    left_down = 0
    for crs_right in range(len(area)):  # 0 1 2 3 4 5 6 >> 99
        right_crs += area[crs_right][crs_right]
        if right_crs > best:
            best = right_crs

    for crs_left in range(len(area)-1, -1, -1):  # 99 98 97 96 ... 0
        left_crs += area[crs_left][left_down]
        left_down += 1
        if left_crs > best:
            best = left_crs



    # for mix in range(4-1, 0, -1):  # 버블소트
    #     for max_sum in range(mix):
    #         if best[max_sum] > best[max_sum+1]:
    #             best[max_sum], best[max_sum+1] = best[max_sum+1], best[max_sum]


    print(f'#{tc} {best}')  # 최종 정답 출력