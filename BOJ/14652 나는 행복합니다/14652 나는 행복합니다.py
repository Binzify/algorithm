n, m, k = map(int,input().split())
cnt = 0

for i in range(n-1):
    for j in range(m-1):
        cnt += 1
        if cnt == k:
            print(i, j)