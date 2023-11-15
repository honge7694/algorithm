def maxSubArray(lst):
	"""
	시간 복잡도 : O(n^3)
	"""
	result = lst[0]
	for i in range(len(lst)):
		for j in range(i, len(lst)):
			result = max(result, sum(lst[i : j+1]))
	
	return result
	
def dp(lst):
	"""
	시간 복잡도 : O(n)
	"""
	dp = [0] * len(lst)
	dp[0] = lst[0]
	for i in range(1, len(lst)):
		dp[i] = max(lst[i], dp[i-1] + lst[i])
	return max(dp)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [-2, -1]
print(dp(nums))