import sys
sys.stdin = open('input.txt')

tc = int(input())

for i in range(1, tc+1):
    N = int(input())
    cards = list(map(int,input())) # 카드목록
    count_card = [0]*10 # [0,0,0,0,0,0,0,0,0,0] 각 카드 갯수를 받을 리스트
    max_num = 0

    for j in range(N): # 카드 목록에서 인덱싱할 번호
        for num in range(10): # 0~9까지의 카드
                if cards[j] == num: # 카드 목록의 수와 0~9까지의 수가 같은 경우
                    count_card[num]+= 1
      # 카드 리스트에서 해당 인덱스위치의 숫자가 올라간다.

        for lot in count_card: #카운팅한 카드 개수리스트에서 수를 한개씩 빼서
            if lot >= max_num : #최대 카드 개수를 찾아 지정한다.
                max_num = lot

            a = 0  # 최대 개수의 카드 번호를 받을 변수 지정
            for k in range(10):  #0~9 카드 다시 돌리고
                if int(count_card[k]) == max_num : #각 인덱스 값을 받아서 위의 최대개수
                    a = k # 속하는 값을 a 에 넣는다.

    print(f'#{i} {a} {max_num}')
                # a = count_card.index(max_num)  # 최대 카드 개수가 위치한 인덱스(카드숫자) 가져오기
                # 어떻게 역순으로 인덱스 순회하지????;; 큰 수의 카드 번호를 빼오는 법
                # 리버스한 뒤에 그 값을 인덱스 가진 다음에 인덱스 9에서 빼는 방법도 있을듯!!!

