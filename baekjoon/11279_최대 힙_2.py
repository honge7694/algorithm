import heapq
import sys
input = sys.stdin.readline


N = int(input())
result = []

for _ in range(N):
	x = int(input())
	
	if x == 0:
		if len(result) == 0:
			print(0)
		else:
			print(heapq.heappop(result) * -1)
	else:
		heapq.heappush(result, (x * -1))
	
	