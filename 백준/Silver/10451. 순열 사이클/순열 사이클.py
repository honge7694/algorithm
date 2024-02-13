import sys
input = sys.stdin.readline

# 연결 요소 찾기 - dfs

def dfs(idx, value):
	numbers[idx] = -1 # 방문처리
	if numbers[value-1] != -1:
		dfs(value-1, numbers[value-1])
	return 

T = int(input())

for _ in range(T):
	count = 0
	N = int(input())
	numbers = list(map(int, input().split()))
	
	for idx, value in enumerate(numbers):
		if numbers[idx] != -1:
			dfs(idx, value)
			count += 1 

	print(count)			
