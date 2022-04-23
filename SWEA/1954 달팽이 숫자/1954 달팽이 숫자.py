import sys

sys.stdin = open('input.txt')

tc = int(input())
# 고정으로 적용되니까 for 문 바깥에 설정. 달팽이의 이동
dx = [1, 0, -1, 0]  # (y축을 기점으로 움직일 땐 (y,0) x 축일 땐 (0,x)
dy = [0, 1, 0, -1]  # 달팽이가 이동하는 우,하,좌,상의 순서대로 놓음 delta i/delta j

for t in range(1, tc + 1):
    N = int(input())
    road = [[0] * N for _ in range(N)]  # 달팽이가 이동할 배열을 만든다.
    x = y = 0  # 달팽이가 있을 위치를 0, 0 으로 지정해둠
    move = 0  # 조이스틱처럼 달팽이를 이동시킨다고 생각함! (0 1 2 3 => 우 하 좌 상)

    for snail in range(1, N * N + 1):  # 달팽이가 돌아가야 하지 않나?
        road[y][x] = snail  # 달팽이의 첫 시작지점인 0, 0 에 1을 입력
        # 입력 후 우측으로 이동해야하기 때문에 dy, dx의 인덱스값을 더해서 이동
        y += dy[move]  # 조이스틱처럼 움직일 것이라고 했으니 dy, dx[0] 우측으로 이동!
        x += dx[move]  # 그러면 (0, 1)의 값을 받아서 달팽이가 우측으로 이동한다.
        # 이 때 주어진 상황에 맞추어 조이스틱 이동, 조건에 걸리면 방향 전환
        '''
        어떠한 조건이 없으면 계속 이제 같은 방향으로만 이동할 것이다. 조건설정
        벽나가는 경우, 숫자 이미 있는 경우 음수 또는 N 일 경우, 간 인덱스 값의 적힌 수가 0 이상인 경우
        '''
        if x < 0 or y < 0 or x >= N or y >= N or road[y][x] > 0:
            # 조건에 걸려서 재정비할 시간이 필요함. 달팽이를 진행시키지 않고 원상복구
            y -= dy[move]
            x -= dx[move]
            # 다시 이전 자리로 돌아온 달팽이에게 새로운 방향을 제안해줌
            move += 1  # 방향 전환시켜줌
            if move == 4:  # 방향이 0,1,2,3 밖에 없어서 4가 되면 다시 0으로 초기화
                move = move % 4
            y += dy[move]  # 이동값 적용
            x += dx[move]

    print(f'#{t}')
    for numbers in road:  # 이중 리스트에서 각 리스트를 한개씩 뽑아온다 [ , , , , , ] 이런 식으로 출력!
        print(*numbers)
        # 그냥 numbers로 출력하면 리스트에 담김 언패킹 연산자로 사용!
