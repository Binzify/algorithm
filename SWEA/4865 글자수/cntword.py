import sys


sys.stdin = open('sample_input.txt')

tc = int(input())
for t in range(1, tc + 1):
    str_a = list(input())  # 동일한 스펠링을 지워버린다.
    dic_a = dict.fromkeys(str_a, 0)  # 각 단어를 딕셔너리 화 {'X': 0, 'Y': 0, 'P': 0, 'V': 0}
    str_b = list(input())
    print(dic_a)

    for spell in str_b:  # str_b에서 목록을 빼서 딕셔너리의 키값과 비교 # 10번 돌리기
        for a in dic_a.keys():  # dic_a 에서 꺼내기
            if a == spell:
                dic_a[a] += 1

    max_spell = 0  # 최대 글자수 출력하기
    for s in str_a:
        if max_spell < dic_a.get(s):  # .get(key) 는 value 소환
            max_spell = dic_a.get(s)

    print(f'#{t} {max_spell}')  # 딕셔너리의 value 값으로 반환

    # max_spell = max(dic_a, key = dic_a.get)  # 최대 많이 등장한 스펠링을 출력한다.
