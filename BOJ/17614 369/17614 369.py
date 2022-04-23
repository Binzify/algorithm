# 58점 부분점수... 어디서 막히는걸까?

N = int(input())
clap = 0
players = [i for i in range(1, N + 1)]

for i in players:
    if len(str(i)) == 1:
        if i % 3 == 0:
            clap += 1
    else:
        for j in str(i):
            if j in '369':
                clap += 1
