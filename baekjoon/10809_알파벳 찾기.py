import string

S = input()

alpha = {}
for s in string.ascii_lowercase:
    alpha[s] = -1

for idx, value in enumerate(S):
    if alpha[value] == -1:
        alpha[value] = idx
        
for i in alpha.values():
    print(i, end=' ')

