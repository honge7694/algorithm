

def maxSubArray(lst):
	result = 0
	for i in lst:
		result = max(result, result+i)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))