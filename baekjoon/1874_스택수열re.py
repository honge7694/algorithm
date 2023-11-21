import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

result = [] # +, -를 담을 리스트
stack = [] # num을 담을 리스트
count = 1 # 수열의 수와 스택에 담긴 값 비교할 count
temp = True

for num in nums:
	# 반복되는 수열의 수는 담지않도록 count <= num을 담음
	while count <= num:
		stack.append(count)
		result.append('+')
		count += 1
    
	if num == stack[-1]: # 입력한 값과 스택의 마지막 값 비교
		stack.pop()
		result.append('-')
	else:
		temp = False
		break

if temp == True:
	[print(i) for i in result]
else:
	print("NO")
