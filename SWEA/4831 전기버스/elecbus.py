import sys
sys.stdin = open('elec_input.txt')

# 1. 버스는 첫 출발시에 충전이 되어있으므로 K만큼 이동할 수 있다.
# 2. 처음 버스는 0번 정류장에 서있지만, 사실상 1칸 이동한 걸로 계산.
# 3. 버스가 도착하거나 또는 지나칠 때 충전소가 있으면 다음 충전소까지의 거리를 계산해
# 다음 K번 안에 도착하지 못한다면 충전을 한다.
# 4. 종점에 딱 맞춰서 도착하거나, 배터리가 떨어지기 전에 도착하면 종료하고 충전회수를 반환
# 5. 종점에 도착하기 전에 배터리가 다 닳면 0 반환

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))  # 충전소
    # 충전기가 있으면 T, 아니면 F (정류장이 0번부터 시작하니 N+1)
    stations = [True if n in chargers else False for n in range(N + 1)]

    # 총 충전 횟수 / 마지막 충전한 위치 인덱스 초기화
    charge_count = 0
    last_charge = 0

    # 시작과 동시에 현 위치 갱신 -> 최대로 일단 갈 수 있을 만큼 가자
    current = K

    # 종착에 도착하지 않았을 때까지 계속 반복 (같거나 큰 경우가 종점을 도착하거나 그이상으로 간 경우)
    while current < N:
        # 3. 한칸씩 뒤로 가다, 마지막 충전위치에 도착했다면 (계속 뒤로 가다가 내가 마지막으로 충전 했던 곳으로 돌아왔다면? 이는 갈 수 없음을 의미)
        if last_charge == current:
            charge_count = 0  # Fail
            break

        # 1. 현 위치에서 충전 가능하다면 (True면 => 충전기가 있으면)
        if stations[current]:
            last_charge = current  # 마지막 충전위치 갱신
            charge_count += 1  # 충전횟수 +1
            current += K  # 또 최대전진

        # 2. 현 위치 충전 불가능하면
        else:
            current -= 1  # 1칸 전으로(충전소 나올때까지 뒤로가기)

    ans = charge_count

    print(f'#{tc} {ans}')