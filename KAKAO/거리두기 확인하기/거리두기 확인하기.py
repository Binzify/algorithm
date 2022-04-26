places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

from collections import deque

def solution(places):
    answer = []
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    checkplace(place,i,j)
            answer.append()
    return answer

def checkplace(place, x, y):
    # 사람 확인 + 테이블 및 파티션 여부 확인
    check = [(0,1),(1,0),(-1,0),(0,-1)]
    visited = [[0]*5 for _ in range(5)]
    # 좌석 탐색
    q = deque()
    q.append((x, y))
    while q:
        nx, ny = q.popleft()
        visited[nx][ny] = 1
        cnt = 0

        for dx, dy in check:
            cx = nx+dx
            cy = ny+dy
            cnt += 1
            if 0 <= cx < 5 and 0 <= cy < 5 and visited[cx][cy] == 0:
                visited[cx][cy] = 1
                if place[cx][cy] == 'P':
                    if cnt <= 2:
                        return 0
                elif place[cx][cy] == 'O':
                    if cnt == 1:
                        q.append([cx,cy])
    return 1


print(solution(places))