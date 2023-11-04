import heapq
import sys
input = sys.stdin.readline


N = int(input())
heap = []

for _ in range(N):
	M = int(input())
	
	if M == 0:
		if len(heap) == 0:
			print(0)
		else:
			# 제일 작은 수를 pop
			print(heapq.heappop(heap))
			
	else:
		heapq.heappush(heap, M)