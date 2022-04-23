sugar = int(input())
move = 0

while sugar >= 0:
    if sugar % 5 == 0:
        move += sugar // 5
        print(move)
        break
    sugar -= 3
    move += 1
else:
    print('-1')
