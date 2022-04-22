import sys

sys.stdin = open('sample_input.txt')

# 탐색하면서 합을 빨리 구하면 끊어버리기
def exchange(stop):  # 정류장 시작점 받기
    global change_cnt, tmp
    # 만약 정류장의 위치가 배터리 리스트 길이보다 크거나 같다면 (도착했다면)
    if stop >= len(battery):
        if tmp <= change_cnt:  # 기존 최소 교체횟수보다 더 적은 경우가 있다면
            change_cnt = tmp   # 최솟값을 변경해준다.
        return

    # 확인할 필요 없이 기존 설정되어있던 최소 교체값이 더 작은거라면, 그냥 종료
    if tmp >= change_cnt:
        return

    # 정류장 번호 + 해당 정류장에 위치한 배터리량 = 도착한 정류장에서부터 현재 위치의 정류장까지 내려오면서 합을 확인하기
    for i in range(stop + battery[stop], stop, -1):
        tmp += 1  # 임시로 교체 횟수를 세는 변수의 값을 하나씩 늘려주고
        exchange(i)  # 계속 재귀로 돌아보면서 위에 조건에 걸리는지 확인한다.
        tmp -= 1  # 돌아오면 해당 경우가 아니므로 교체 횟수를 다시 원상복귀한다.

T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    N = arr[0]  # 정류장의 개수
    battery = arr[1:]  # 배터리가 위치한 정류장 리스트
    tmp = 0  # 버스정류장을 돌면서 몇번 교체했는지 저장할 변수
    change_cnt = 9999  # 기존 설정되어있는 교체 횟수 (정답출력)
    exchange(0)  # 0번 정류장에서 출발한다.
    print(f'#{tc} {change_cnt-1}')  # 첫 출발지점은 빼준다.