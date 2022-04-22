import sys
sys.stdin = open('input.txt')

tc = int(input())  # 테스트 케이스
for t in range(1, tc+1):
    N, M = map(int, input().split())   # N : 파리 사는 지역 크기, M : 파리채 크기
    area = []  # 파리 지옥을 받아들일 리스트
    for i in range(N):  #  N*N 이기에 N만큼의 리스트를 받아들임
        area.append(list(map(int, input(). split())))  # 파리들이 사는 이중 리스트 완성
        # 이제 파리채로 잡아야 함, 인덱싱으로 각 수를 파리채 안에 넣고, 그 파리채에 들어온 수를 다 더한다.
        # 다 잡고 나서 그 옆의 한칸으로 이동해서 4칸 잡기, 그리고 가로를 다 돌면 세로로 한 칸 내려와서 다시 가로 확인
        # 이 전의 잡은 파리 값과 비교해보고 값이 작다면 다른 칸 이동. 가장 큰 값을 계속 저장
    catch = [] # 구간 별 최대 값 비교를 위해 담을 잡은 파리 수 리스트
    for move_x in range(N-M+1) :  # 예를 들어 5칸에서 2칸씩 검사하면 총 4번을 해야하므로, 5-2+1 = 4 번 하도록 함
        for move_y in range(N-M+1):
            sum_flies = 0  # 잡은 파리 합친 수, 포문을 돌면서 다시 초기화 시킴.
            for x in range(M):  # 파리채 크기에 맞는 잡힌 파리들을 하나씩 삼켜낸다.
                for y in range(M):
                    sum_flies += area[move_x+x][move_y+y]  # 이동한 파리채 위치 + 파리채 크기를 더해서
                    # 파리 지옥에서의 위치를 찾아내 파리채 누른 만큼의 수를 파리 잡은 수 목록에 더한다.
            catch.append(sum_flies)

    # 리스트에서 가장 큰 파리 수를 결과로 출력합니다.
    print(f'#{t} {max(catch)}')
