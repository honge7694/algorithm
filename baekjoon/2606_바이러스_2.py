import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

def dfs():
	# 방문 처리
	visited[v] = True
	
	

# 컴퓨터 
computer = [[False] * (N+1) for _ in range(N+1)]

# 컴퓨터간 연결
for _ in range(M):
	a, b = map(int, input().split())
	computer[a][b] = True
	computer[b][a] = True

# 방문
visited = [False] * (N+1)

for i in range(N):
	for j in range(N):
		if dfs()

