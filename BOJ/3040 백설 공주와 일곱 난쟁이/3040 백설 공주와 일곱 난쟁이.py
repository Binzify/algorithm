import sys

sys.stdin = open('input.txt')

height = 100  # 전체 키가 100이다.
total = 0  # 난쟁이들의 키를 다 합친다.
dwarfs = []  # 난쟁이들을 담는다 (우선 나부터 들어갈까)

for i in range(9):  # 9명의 난쟁이이기 때문에
    people = int(input())
    dwarfs += [people]
    total += people

# # 버블 소트로 정렬하기 (배운거 써먹기)
# for k in range(len(dwarfs) -1, 0, -1):  # 역으로 숫자를 꺼낸다, 9부터 시작
#     for j in range(k):  # 0부터 k(9)까지
#         if dwarfs[j] > dwarfs[j + 1]:
#             dwarfs[j], dwarfs[j + 1] = dwarfs[j + 1], dwarfs[j]
dwarfs.sort()

# 난쟁이의 키 전체 합이 140인데, 여기서 100을 뺀다.
remain = total - height  # dwarfs = [7 8 10 13 15 19 20 23 25] remain = 40
for num in range(9):
    if len(dwarfs) == 7:
        break
    for a in range(len(dwarfs)):  # a = 0 1 2 3 4 5 6 7 8  # num = 1 2 3 4 5 6 7 8
        if dwarfs[num] + dwarfs[a] == remain:
            c = dwarfs[num]
            d = dwarfs[a]
            if c + d == remain:
                dwarfs.remove(c)  # 그리고 남은 40을 리스트를 돌면서 인덱스를 통해 수를 비교하면서 뺀다. (2개만)
                dwarfs.remove(d)  # 즉 두 명의 난쟁이의 합이 40인 것을 찾아내면 성공(dwarfs)
for pop in dwarfs:  # 최종 난쟁이들을 뽑아낸다.
    print(pop)
