import sys
input = sys.stdin.readline
INF = int(1e9)


n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

# a == b 0으로 채우기
for a in range(1, n+1):
	for b in range(1, n+1):
		if a == b :
			graph[a][b] = 0
		else:
			continue
	
# a, b채우기
for _ in range(m):
	a, b, c = map(int, input().split())
	graph[a][b] = min(c, graph[a][b])
	# graph[a][b] = c
	# graph[b][a] = c
	
# graph 순환
for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
			
# print(graph)

for i in range(1, n+1):
	for j in range(1, n+1):
		if graph[i][j] == INF:
			print(0, end=' ')
		else:
			print(graph[i][j], end=' ')
	print('')