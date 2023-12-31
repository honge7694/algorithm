import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 테스트 케이스의 개수
T = int(input())

for _ in range(T):
	N = int(input()) # 탐사 공간의 크기
	graph = []
	for _ in range(N):
		graph.append(list(map(int, input().split())))
	
	# 최단 거리 테이블을 초기화
	distance = [[INF] * N for _ in range(N)]
	
	x, y = 0, 0 # 시작 위치 (0, 0)
	# 시작 노드로 가기위한 비용은 (0, 0) 위치의 값으로 설정하여, 큐에 삽입
	q = [(graph[x][y], x, y)]
	distance[x][y] = graph[x][y]
	
	while q:
		# 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
		dist, x, y = heapq.heappop(q)
		
		# 현재 노드가 이미 처리된 적이 있는 노드라면 무시
		if distance[x][y] < dist:
			continue
		
		# 현재 노드와 연결된 다른 인접한 노드들을 확인
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			
			# 맵의 범위를 벗어나는 경우 무시
			if nx < 0 or nx >= N or ny < 0 or ny >= N:
				continue
			
			cost = dist + graph[nx][ny]
			# 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
			if cost < distance[nx][ny]:
				distance[nx][ny] = cost
				heapq.heappush(q, (cost, nx, ny))
		

	print(distance[N - 1][N - 1])

"""
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1 
5 8 3 2 4 8 3
7 4 8 4 8 3 4
"""