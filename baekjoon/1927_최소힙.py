import sys
input = sys.stdin.readline
import heapq

a = []
N = int(input())

for _ in range(N):
	num = int(input())
	
	if num == 0:
		if len(a) == 0:
			print(0)
		else:
			print(heapq.heappop(a))
		
	else :
		heapq.heappush(a, num)
	