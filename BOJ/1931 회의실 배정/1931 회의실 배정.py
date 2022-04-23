import sys

sys.stdin = open('input.txt')

N = int(input())
conference = []

for _ in range(N):
    start, end = map(int, input().split())
    conference.append((start, end))

# 시작과 종료 지점이 같은 경우에는 우선 종료시점 중 시작 지점을 기준으로 정렬한다.
conference.sort(key=lambda x: (x[1], x[0]))

end_time = conference[0][1]
cnt = 1  # 첫 회의를 기준으로 잡으면서 횟수 카운트

for s, e in conference[1:]:
    if end_time <= s:
        cnt += 1
        end_time = e
    else:
        continue

print(cnt)
