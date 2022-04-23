import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 컨테이너 수, 트럭 수
    containers = list(map(int, input().split()))  # 컨테이너 무게 리스트
    trucks = list(map(int, input().split()))  # 트럭 적재용량 리스트
    result = 0  # 최종 운송한 무게의 합 결과값

    # 컨테이너와 트럭을 오름차순으로 정렬해 준 다음
    trucks.sort()
    containers.sort()

    while True:
        if len(containers) > 0 and len(trucks) > 0:  # 리스트 안에 원소들이 남아있다면
            if containers[-1] <= trucks[-1]:  # 적재 용량과 무게를 비교해서 가져갈 수 있으면 가져가기
                result += containers.pop()
                trucks.pop()
            else:
                containers.pop()  # 무게가 적합하지 않다면 컨테이너 물량에서 빼버린다.
        else:
            break  # 더이상 조건 충족 안하면 끝
    print(f'#{tc} {result}')
