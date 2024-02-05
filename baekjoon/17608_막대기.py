import sys
input = sys.stdin.readline

N = int(input())
graph = [int(input()) for _ in range(N)]
count = 1
max_graph = graph[-1]

for stick in graph[::-1]: 
	if stick > max_graph:
		count += 1
		max_graph = stick
print(count)