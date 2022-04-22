N = int(input())
mt = list(map(int,input().split()))
best = answer = kill = 0

for i in mt:
    if i > best :
        best = i
        kill = 0
    else:
        kill += 1

    if answer < kill:
        answer = kill
print(answer)