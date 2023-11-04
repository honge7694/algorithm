import heapq

N= int(input())

time = []
for _ in range(N):
	time.append(list(map(int, input().split())))
	
heapq.heapify(time)
for _ in range(N):
	print(' '.join(map(str, heapq.heappop(time))))