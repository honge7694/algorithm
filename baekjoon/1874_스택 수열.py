import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
count = 1
stack = [] # 수열의 숫자가 들어간다.
result = []

for num in nums:
	while count <= num:
		stack.append(count)
		result.append("+")
		count += 1
		
	# stack과 num이 같으면 pop
	if stack[-1] == num:
		stack.pop()
		result.append("-")
	# 입력된 수열을 못만들 때
	else:
		print("NO")
		break

else:
	[print(i) for i in result]



