import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

# graph 그리기
graph = [[INF] * (V+1) for _ in range(V+1)]

# a == b 그래프 0 초기화
for a in range(1, V+1):
	for b in range(V+1):
		if a == b: 
			graph[a][b] = 0

# graph 값 넣기
for _ in range(E):
	u, v, w = map(int, input().split())	
	graph[u][v] = w
	

# 점화식
for k in range(1, V+1):
	for a in range(1, V+1):
		for b in range(1, V+1):
			graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# graph 출력
for i in range(1, 2):
	for j in range(1, V+1):
		if graph[i][j] == INF:
			print("INF")
		else:
			print(graph[i][j])