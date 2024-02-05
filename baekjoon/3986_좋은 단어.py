import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
stack = []
result = 0

for word in words:
	for char in word:
		if stack and char == stack[-1]:
			stack.pop()
		else:
			stack.append(char)
	else:
		if not stack:
			result += 1
		stack = []
print(result)