import heapq

def findKthLargest(nums, k):
	heap = []
	
	for val in nums:
		heapq.heappush(heap, -val)
		
	result = [heapq.heappop(heap) for _ in range(k)]
	
	return result[-1] * -1
	
nums = [3,2,1,5,6,4]
k = 2

print(findKthLargest(nums, k))