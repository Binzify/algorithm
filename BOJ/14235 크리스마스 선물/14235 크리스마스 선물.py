import sys, heapq
sys.stdin = open('input.txt')

n = int(input())
present = []  # 선물 담을 리스트
for _ in range(n):
    a = list(map(int,input().split()))  # 개수가 여러개 충전되므로 리스트로 받기
    if a[0] == 0:  # 만약 받은 값이 0이면 (아이들 만남)
        if len(present) == 0:  # 선물 뿌리는데 없다면
            print(-1)  # -1 출력
        else:  # 있다면
            print(heapq.heappop(present))  # 우선순위 중 가장 큰 가치 주기
    else: 
        for i in range(1, a[0]+1):  # 2 3 2 들어오면 1~2까지 돌면서 (-3,3), (-2,2) 저장
            heapq.heappush(present, (-a[i], a[i]))