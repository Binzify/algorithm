import sys
sys.stdin = open('input.txt')

cnt = 0
for i in range(1, 11):
    towers = int(input()) #아파트 수
    aparts = list(map(int, input().split())) # 아파트 층수 리스트
    cnt +=1 # 테스트 케이스 카운트

    views = 0
    for f in range(2,towers-2): #앞 뒤로 0이므로 제외한다.
        l_1 = aparts[f]-aparts[f-1] # 좌 1번과 비교
        l_2 = aparts[f]-aparts[f-2] # 좌 2번과 비교
        r_1 = aparts[f]-aparts[f+1] # 우 1번과 비교
        r_2 = aparts[f]-aparts[f+2] # 우 2번과 비교
        if l_1 > 0 and l_2 > 0 and r_1 > 0 and r_2 > 0: #모든 수가 0보다 크면 가장 작은 수의 세대를 얻는다.
            min = l_1
            a = [l_2, r_1, r_2]
            for small in a : #for 문 돌려서 최소값 만들기
                if min >= small:
                    min = small
            views += min
    print(f'#{cnt} {views}')

