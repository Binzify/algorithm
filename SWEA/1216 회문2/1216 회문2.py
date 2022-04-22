import sys


sys.stdin = open('input.txt')

# 회문 판별용 함수를 정의한다.
# 회문 함수에 100x100으로 가득한 판별문을 넣으면 작동한다.
# 가로 비교 : 0번칸과 99번칸, 1번칸과 98번칸으로 이동, 즉 왼쪽은 1칸씩 증가, 오른쪽은 감소
# 인덱스를 증가, 감소하는 방식으로 찾아본다. 필요한 건 0 에서 99까지 가는것과 99에서 0까지 오는것
# 근데 회문은 중앙을 기점으로 양쪽이 같은지를 판별하기 때문에, 0~49, 99~50 까지만 하면된다.
# 이에 대한 조건을 걸어주면 될 듯 인덱스 왼쪽이 오른쪽을 넘어가게 된다면 멈춘다.
# 열과 관련된 회문은 전치를 사용해서 풀 것이므로 행에 대해서 하나만 판별하는 함수를 만들고자함
def pd(case):
    for r in range(100, 0, -1):  # 100에서 1까지 100번 돌면서 아래에 영향 최종적으로 개수
        for i in range(100):  # 0부터 올라가는 인덱스, 행을 중심으로 0
            for j in range(100-r+1):  # 100-100+1 > 100-99+1 => 0 > 1 > 2 >....
                if case[i][j] == case[i][j+r-1]:  # 맨 뒤에랑 비교하는 것 0 과 99 비교하기
                    rightside = j+r-1
                    while case[i][j] == case [i][rightside] and j <= rightside:  # 두 문자열이 같고, 왼쪽이 오른쪽을 넘지 않으면
                        j += 1
                        rightside -= 1
                    if j < rightside:  # 왼쪽이 오른쪽을 넘었다는 것은 회문의 길이가 제일 길다는 의미가 됨
                        continue
                    else:  # 100개에서부터 범위를 줄여서 나가기 때문에 r개의 길이의 회문을 돌렸을 때 찾은 것이 됨
                        length = r  # 그래서 해당 r을 얻음
                        return length


for _ in range(10):  # 10번의 시도
    tc = int(input())  # 첫 숫자받기
    case = [input() for _ in range(100)]
    p_case = pd(case)  # 첫번째를 함수화 시킴
    case2 = list(map(list, zip(*case)))  # 전치 시키기
    case2 = [''.join(a) for a in case2]  # 열을 행으로 보기 위해 정렬함
    p_case2 = pd(case2)  # 두번째를 함수화 시킴

    max_len = 0  # 최고 구하기 위한 비교
    if p_case > p_case2:
        max_len = p_case
    else :
        max_len = p_case2

    print(f'#{tc} {max_len}')




