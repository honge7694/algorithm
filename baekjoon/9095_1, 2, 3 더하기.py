import sys 
sys.setrecursionlimit(10**6) 

def input(): 
	return sys.stdin.readline().strip()

def dfs(target, path):
	global count
	
	# 백트래킹
	if target == 0:
		result_path.append(path)
		count += 1
		return
	if target < 0:
		return
	
	# 재귀를 통해, target을 빼고, path를 구한다.
	for i in range(len(nums)):
		dfs(target-nums[i], path+[nums[i]])


T = int(input()) # 테스트케이스 입력
nums = [1, 2, 3]
for _ in range(T):
	target = int(input())
	count = 0
	result_path = [] # 무엇을 더했는지 확인용
	dfs(target, [])
	print(count, result_path)
