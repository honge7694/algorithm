import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

# graph 생성
graph = [[INF] * (N+1) for _ in range(N+1)]

# a == b 0으로 초기화
for a in range(N+1):
	for b in range(1, N+1):
		if a == b:
			graph[a][b] = 0

# graph 값 입력
for _ in range(M):
	a, b = map(int, input().split())
	graph[a][b] = 1

# 점화식
for k in range(1, N+1):
	for a in range(1, N+1):
		for b in range(1, N+1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
			

result = 0
for i in range(1, N+1):
	count = 0
	for j in range(1, N+1):
		if graph[i][j] != INF or graph[j][i] != INF:
			count += 1
	if count == N:
		result += 1

print(result)


"""
6 6
1 5
3 4
4 2
4 6 
5 2
5 4
"""