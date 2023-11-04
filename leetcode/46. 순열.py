import sys 
sys.setrecursionlimit(10**6) 

def input(): 
	return sys.stdin.readline().strip()

def dfs(path):
	if len(path) == len(nums):
		result.append(path)
		return
	
	for i in range(len(nums)):
		if nums[i] not in path:
			dfs(path + [nums[i]])


nums = [1, 2, 3]
result = []
dfs([])
print(result)

