import math
import sys
input = sys.stdin.readline

num = 1
while True:
	S = input()
	
	if '-' in S:
		break
	
	stack = []
	count = 0
	
	for s in S:
		if s == '{':
			stack.append(s)
		elif s == '}': 
			if stack:
				stack.pop()
			else:
				count += 1
				stack.append('{')
	else:
		count += int(len(stack) / 2 )
		
	print(f"{num}. {count}")
	num += 1 