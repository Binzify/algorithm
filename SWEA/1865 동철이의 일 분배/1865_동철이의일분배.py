import sys

sys.stdin = open('input.txt')

def dfs(percent, worker):  # 확률 계산, 직원
    global result

    # 가지치기 : 만약 구한 확률이 0퍼센트보다 아래라면 (확률이 아예 없다면) 종료
    if percent <= result:
        return

    if worker == N:  # 모든 직원들이 일을 다 하는 경우 최종 결과랑 비교
        if result <= percent:  # 만약 percent가 더 크다면
            result = percent
        return
    # 재귀로 각 일을 더하는 과정을 계속한다.
    for i in range(N):  # 전체 순회하면서
        if visited[i] == 0:  # 방문 안한경우
            visited[i] = 1  # 방문표시 해주고
            dfs(percent*success[worker][i]*0.01, worker+1)  # 확률값 * 일 확률*0.01 (바로 백분율 표시), 다음직원 확인
            visited[i] = 0  # 끝나면 원상복구해서 다음 행에서 확인할수 있도록 방문을 비운다.


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    success = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N  # 방문표시 리스트
    result = 0
    dfs(1, 0)  # 1 == 100.00000% 이므로
    answer = format(result*100,'.6f')
    print(f'#{tc} {answer}')