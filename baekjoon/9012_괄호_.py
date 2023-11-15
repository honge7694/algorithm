import sys
input = sys.stdin.readline

stack = []

T = int(input())
for _ in range(T):
	stack = []
	N = input()
	
	for n in N:
		if n == '(':
			stack.append(N)
		elif n == ')':
			if stack:
				stack.pop()
			else:
				print("NO")
				break
	else:
		if not stack:
			print("YES")
		else:
			print("NO")
	

