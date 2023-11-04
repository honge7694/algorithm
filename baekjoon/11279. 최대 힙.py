import heapq
import sys
input = sys.stdin.readline


N = int(input())
result = []

for i in range(N):
	M = int(input())
	
	if M == 0:
		if len(result) == 0:
			print(0)
		else:
			print(heapq.heappop(result) * -1)
	else:
		heapq.heappush(result, M * -1)
	

