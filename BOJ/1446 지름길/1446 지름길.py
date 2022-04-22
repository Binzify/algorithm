import sys
sys.stdin = open('input.txt')

N, D = map(int,input().split())
inf = 10001
highway = [[] for _ in range(inf)]  # 고속도로 방향 그래프 만들어주기(무방향 아님)
for _ in range(N):
    s, e, w = map(int,input().split())  # 시작, 도착, 지름길(가중치)
    highway[s].append((e, w))  # 출발 지점에 도착지점과 지름길을 넣어둔다.

drive = [i for i in range(D+1)]  # 세준이가 가야하는 거리를 0부터 도착지점까지 리스트로 만든다
for i in range(D+1):  # 도착지까지 운전하며 확인하기
    if i != 0:  # 0은 출발지점이라 자기 자신이 거리이므로
        drive[i] = min(drive[i], drive[i-1]+1)
    # 만약 i가 지름길 리스트에 존재한다면
    if len(highway[i]) > 0:
        for end, shortcut in highway[i]:  # 고속도로 인덱스에 저장된 끝과 지름길 튜플을 꺼내서
            if end <= D and drive[end] > drive[i] + shortcut:  # 마지막이 최종 지점을 넘지 않고, 끝지점 값보다 출발점 + 지름길 값이 작다면
                drive[end] = drive[i] + shortcut  # 현재까지의 거리 + 지름길 저장해준다.

print(drive[D])
