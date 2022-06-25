import sys
sys.stdin = open('input.txt')

plus, minus = map(int,input().split())
vers = []

x = plus-minus
y = int(x/2)

if y >= 0:
    vers.append(x)
    vers.append(y)
else:
    print('-1')

if len(vers)==2:
    print(*vers)
