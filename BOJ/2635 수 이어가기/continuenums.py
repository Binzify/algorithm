import sys

sys.stdin = open('input.txt')


num = int(input())  # 제시되는 수
numlist = []  # 이후 숫자를 담을 리스트


for num2 in range(num, 0, -1):  # 1부터 자기 자신까지 포함되어야 하므로, 큰수니까 역수로
    numlist2 = [num, num2]  # 비교 대상의 새로운 리스트
    new_num = 0  # 새로운 수를 받을 변수 설정
    idx = 1  # 인덱싱을 위한 수 설정
    while idx < len(numlist2):  # 인덱스 값이 새로운 리스트의 개수보다 작을때까지, 크면 멈춤
        # if len(numlist2) >= 2:  # 리스트 안의 변수가 2개 이상이어야 진행이 가능
        new_num = numlist2[idx - 1] - numlist2[idx]  # 앞앞 과 앞의 값을 뺀다 100 - 99
        if new_num >= 0:  # 그렇게 만든 값이 양수라면
            numlist2 += [new_num]  # 100 99 1 리스트에 더한다
            idx += 1  # 인덱싱을 위해 1을 추가해서 그 다음 과정을 거친다
            # 리스트 길이 하나를 기준으로 삼은 후 그보다 더 큰 리스트가 생기면 변경한다.
            if len(numlist) < len(numlist2):  # 새로운 리스트의 길이가 기존 리스트의 길이보다 길다면
                numlist = numlist2  # 새로운 리스트로 교체한다.
        else:
            break

print(len(numlist))  # 리스트의 길이를 출력하고
print(*numlist)  # 그 리스트에 담긴 수들을 전부 출력한다
