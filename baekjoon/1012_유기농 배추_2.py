import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(a, b):
	queue = deque()
	queue.append((a, b))
	
	while queue:
		y, x = queue.popleft()
		
		for i in range(4):
			nx = dx[i] + x
			ny = dy[i] + y
			
			if nx >= M or nx < 0 or ny >= N or ny < 0:
				continue

            # 0일시 배추 x
			if graph[ny][nx] == 0:
				continue
			
			# 배추 확인
			if graph[ny][nx] == 1:
				graph[ny][nx] = 0
				queue.append((ny, nx))
	

T = int(input())

for _ in range(T):
	M, N, K = map(int, input().split())

	# 밭의 크기
	graph = [[0] * M for _ in range(N)]

	# 배추의 위치
	for _ in range(K):
		x, y = map(int, input().split())
		graph[y][x] = 1
	
	count = 0
	# 방문 확인
	for i in range(N): # y
		for j in range(M): # x
			if graph[i][j] == 1:
				bfs(i, j)
				count += 1
	print(count)