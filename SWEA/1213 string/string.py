import sys

sys.stdin = open('test_input.txt', encoding='utf-8')

for tc in range(10):
    t = int(input())
    word = input()  # 찾아야할 문자열
    search_w = input()  # word가 움직이며 검색할 문자열
    f_w = len(word)  # 찾아야 할 문자의 길이
    s_w = len(search_w)  # 검색하는 문자의 길이

    f = 0  # fw의 인덱스
    s = 0  # sw의 인덱스
    cnt = 0  # 문자열이 얼마나 들어있는지 카운트하기

    while f < f_w and s < s_w:  # 주어진 인덱스에서 벗어나지 않는다.
        if word[f] != search_w[s]:  # 불일치 했을 때는 위치 되돌리기
            s = s - f  # 시작했던 위치로 이동한다
            f = -1  # 찾을 문자열의 맨 앞 인덱스로
        s += 1
        f += 1  # 각각 1 씩 더해서 이전의 위치랑 원 위치를 비교한다.
        if f == f_w:  # 인덱스가 길이와 같아진다 -> 그럼 다음에 인덱스가 넘어가므로, 이는 단어를 찾았다는 의미
            cnt += 1  # 문자열이 동일하면 추가
            f = 0  # 다 찾았으면 다시 인덱스를 돌려놓고 끝난 부분부터 찾기 시작한다.

    print(f'#{t} {cnt}')
