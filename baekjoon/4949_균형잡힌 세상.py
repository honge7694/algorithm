import sys
input = sys.stdin.readline


while True:
	text = input()
	
	# 종료 조건
	if text.rstrip() == ".":
		break
	
	stack = []
	for txt in text:
		if txt == '(' or txt == '[':
			stack.append(txt)
		elif txt == ')':
			# 스택이 존재하고, 스택의 마지막이 '('이면
			if stack and stack[-1] == '(':
				stack.pop()
			else :
				print("no")
				break
		elif txt == ']':
			if stack and stack[-1] == '[':
				stack.pop()
			else :
				print("no")
				break
	else:
		if not stack:
			print("yes")
		else:
			print("no")
	