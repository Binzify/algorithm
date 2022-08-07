n, m, k = map(int,input().split())

print(min(m,k) + min(n-m, n-k))

# 전체에서 O 카드의 개수와 전체에서 O로 표시할 카드의 개수를 빼서 그의 최소 값을 찾으면 된다.