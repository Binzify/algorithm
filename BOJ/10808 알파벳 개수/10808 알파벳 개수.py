from string import ascii_lowercase

alphabet = list(ascii_lowercase)
countlist = [0]*len(alphabet)
word = input()

for i in word:
    countlist[alphabet.index(i)] += 1
    
print(*countlist)
