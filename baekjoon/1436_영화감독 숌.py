N = int(input())
title = '666'
count = 0
num = 0


while True:
	num += 1
	
	if title in str(num):
		count += 1
	
	if count == N:
		print(num)
		break
	