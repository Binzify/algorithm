import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())  # N=참가한 학생 수 K=방 최대 수용 인원
m_room = [0] * 7  # 남자들 방, 인덱스 맞추기
w_room = [0] * 7  # 여자들 방, 인덱스 맞추기

for _ in range(N):
    sex, grade = map(int, input().split())
    if sex == 0:
        w_room[grade] += 1
    else:
        m_room[grade] += 1

room_cnt = 0
for i in w_room:
    if 0 < i <= K:
        room_cnt += 1
    else:
        room_cnt += i // K
        i = i % K
        if i % K > 0:
            room_cnt += 1
for j in m_room:
    if 0 < j <= K:
        room_cnt += 1
    else:
        room_cnt += j // K
        if j % K > 0:
            room_cnt += 1

print(room_cnt)
