from collections import Counter, defaultdict
import heapq


def kWeakestRows(mat, k):
	heap = []
	result = []
	
	for i in range(len(mat)):
		cnt = mat[i].count(1)
		heapq.heappush(heap, [cnt, i])
	
	for _ in range(k):
		result.append(heapq.heappop(heap)[1])
	
	return result

matrix = [
	[1,1,0,0,0],
	[1,1,1,1,0],
	[1,0,0,0,0],
	[1,1,0,0,0],
	[1,1,1,1,1]
]

print(kWeakestRows(matrix, 3))

