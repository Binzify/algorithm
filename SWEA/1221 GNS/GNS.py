import sys
sys.stdin = open('GNS_test_input.txt')

tc = int(input())
for t in range(1, tc+1):
    A, N = input().split()
    text = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]  # 외계숫자
    alien = list(input().split())
# 1. 문자 == 문자 확인, 2. 해당 문자가 위치한 인덱스 값을 활용하여 문자 => 숫자로 전환
# 3. 숫자들을 빈 리스트에 담아서 오름차순 정렬 4. 다시 리스트에서 숫자를 꺼내면서 문자로 전환
# 5. 최종 출력 ' '.join(마지막 문자 담긴 리스트나 문자열)
    trans = []  # 문자에서 숫자로 변환된 것을 담기위한 리스트
    final = ''  # 최종 결과값
    # 1번 순서를 위해 할 것 : 외계 문자 꺼내기 -> text 리스트에서 확인하기 -> 해당 숫자 담기
    for st in alien:  # 문자대로 나오게하기
        for i in range(10):  # 0 ~ 9까지 돌리기 (인덱스값이 곧 해당하는 문자의 숫자)
            if st == text[i]:
                trans += [i]  # 2번 활동 : 문자를 숫자로 담기
    # 3번 순서 (sort /버블소트 쓰자)
    for j in range(len(trans)-1, 0, -1):  # 버블 소트 실행
        for k in range(j):
            if trans[j] < trans[k]:
                trans[k], trans[j] = trans[j], trans[k]
    # 4번 순서
    for num in trans:  # 정렬된 리스트에서 숫자를 꺼내 각각 최종 문자열에 담기
        final += text[num]
        final += (' ')

    print(f'#{t}')
    print(final)





