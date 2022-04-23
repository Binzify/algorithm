import sys

sys.stdin = open('input.txt')


def BFS(S):
    q = [S]
    v[S] = 1
    while q:
        new = q.pop(0)  # 큐에 집어넣은 값을 활용하여
        for i in nodes[new]:  # 연결되어 있는 노드들을 탐색하여
            if v[i] == 0:  # 해당 거리가 방문하지 않은 곳이라면
                v[i] = v[new] + 1  # 이전 지점에 표시된 거리의 +1을 해준다.
                q.append(i)  # 그리고 새로운 큐 목록에 넣어준다.


for tc in range(1, 11):
    C, S = map(int, input().split())
    nums = list(map(int, input().split()))
    nodes = [[] for _ in range(101)]
    v = [0] * 101  # 방문처리한 목록을 사용하기 위해 함수가 아닌 외부에 처리를 한다.

    for i in range(0, C, 2):  # 2칸씩 확인하기
        nodes[nums[i]].append(nums[i + 1])

    BFS(S)

    v_max = max(v)  # 방문한 거리 중 가장 긴 거리
    maxnum = 0  # 긴 거리에 해당하는 숫자 중에서 가장 큰 숫자 저장
    for i in range(len(nodes)):  # 비상연락망의 길이만큼 돈 다음에
        if (
            v[i] == v_max and maxnum < i
        ):  # 만약 해당 방문 기록의 숫자 중에서 가장 먼 번호가 있다면, 그것을 최대값이랑 비교해서
            maxnum = i  # 정답으로 처리한다.
    print(f'#{tc} {maxnum}')
