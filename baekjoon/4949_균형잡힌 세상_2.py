import sys
input = sys.stdin.readline


while(True):
	text = input().rstrip()
	
	if text == ".":
		break
	
	stack = []
	for char in text :
		if "(" == char or "[" == char : 
			stack.append(char)
		elif char == ')':
			if stack and stack[-1] == '(':
				stack.pop()
			else :
				print("no")
				break

		elif char == ']':
			if stack and stack[-1] == '[':
				stack.pop()
			else :
				print("no")
				break
	else :
		if stack :
			print("no")
		else :
			print("yes")
		
		
		
		
"""
while True:
    text = input()
    stack = []

    if text == ".":
        break

    for bracket in text:
        if bracket in '([':
            stack.append(bracket)
        elif bracket in ')]':
            if not stack or abs(ord(bracket) - ord(stack.pop())) > 2:
                stack.append(bracket)
                break

    print('yes' if not stack else 'no')
"""