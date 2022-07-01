import sys

sys.stdin = open('input.txt')

n,m = map(int,input().split())
fish = []
for _ in range(n):
    fish.append(input())

for i in range(n):
    print(fish[i][::-1])