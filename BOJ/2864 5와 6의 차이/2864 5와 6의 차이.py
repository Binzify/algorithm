A, B = input().split()

# 가장 작은 값 : 6을 5로 계산했을 때, 가장 큰 값 : 5를 6으로 계산했을 때!!!
min_sum = int(A.replace('6','5')) + int(B.replace('6','5'))
max_sum = int(A.replace('5','6')) + int(B.replace('5','6'))

print(min_sum, max_sum)