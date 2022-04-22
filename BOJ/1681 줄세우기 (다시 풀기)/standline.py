import sys
sys.stdin = open('input.txt')

n, l = map(int, input().split())
student = []
for i in range(1, n + 1):
    student.append(i)

while True:
    for j in student:
        if str(l) in str(j):
            j = student[-1] + 1
            student.append(j)

    if str(l) not in str(student[-1]):
        break

print(student[-1])