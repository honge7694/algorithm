import sys
input = sys.stdin.readline

N = input().strip()
number = [0] * 10

for i in N:
	i = int(i)
	if i == 6 or i == 9:
		if number[6] > number[9] :
			number[9] += 1
		else:
			number[6] += 1
	else :
		number[i] += 1

print(max(number))



"""
number = dict()
count = 0

for i in str(N):
	if i in number:
		if i == '9' or i == '6':
			number[i] += 0.5 
		else:
			number[i] += 1
	else:
		if i == '9' or i == '6':
			number[i] = 0.5
		else:
			number[i] = 1

print(int(max(number.values())))
"""