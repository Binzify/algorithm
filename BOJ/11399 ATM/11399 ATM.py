import sys

sys.stdin = open('input.txt')

N = int(input())
line = list(sorted(map(int, input().split())))
atm = []

for i in line:
    if not atm:
        atm.append(i)
    else:
        atm.append(i + atm[-1])
print(sum(atm))
