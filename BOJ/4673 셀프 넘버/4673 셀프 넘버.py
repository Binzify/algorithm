numbers = set(range(1, 10001))
new_num = set()

for i in range(1, 10001):  # 1부터 10000까지의 숫자를 돌려서
    for j in str(i):  # 해당 숫자 + 각 자리수를 더할 수 있도록 한다.
        i += int(j)  # 각 자리수대로 더한 값을 i에 입력하고 그 값을
    new_num.add(i)  # set 자료형 더하기 .add를 통해 새로운 set 집합에 넣어준다

# set 집합끼리 뺀 후 오름차순으로 정렬
# list와 다르게 집합.sort() 는 안되고 sorted()를 써야함
answer = sorted(numbers - new_num)
for i in answer:
    print(i)
