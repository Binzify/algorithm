import sys

sys.stdin = open('input.txt')

n = int(input())
# n 이 1 인 경우를 받아내기 위해서...
stairs = [0 for _ in range(301)]
memo = [0 for _ in range(301)]

for i in range(n):
    stairs[i] = int(input())

# 메모이제이션, 계단 3개를 오를 수 있는 경우 중 큰 값을 넣기 (첫 시작 계단, 시작계단+1칸만 오른 경우와 2칸에서 시작하는 경우 비교 후 큰 값, 한칸+두칸과 두칸+한칸 중 큰 값)
memo[0] = stairs[0]  # 1번 계단 오르는 경우
memo[1] = (max(stairs[0]+stairs[1],stairs[1]))  # 2번 계단 오르는 경우
memo[2] = (max(stairs[0]+stairs[2], stairs[1]+stairs[2]))  # 3번 계단 오르는 경우

# 이미 계단 3개 오른 상태이므로 3부터 마지막 갯수까지 for 문 돌리기
for i in range(3, n):
    memo[i]=max(stairs[i] + memo[i-2], stairs[i] + memo[i-3] + stairs[i-1])
    # 기존 값에서 다음 오를 계단의 위치 + 기존 메모이제이션 한 리스트에서 한칸 또는 두칸의 상태인 경우 중에서 큰 값 넣기

print(memo[n-1])