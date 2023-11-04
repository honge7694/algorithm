import heapq

def maxProduct(nums):
	heap = []
	
	# 큰 값으로 만들기 위해 -를 넣어준다.
	for val in nums:
		heapq.heappush(heap, -val)
	
	result = []
	for _ in range(2):
		result.append(heapq.heappop(heap))

	return (result[0]+1) * (result[-1]+1)
		
		
	


nums = [3, 4, 5, 2]
print(maxProduct(nums))
