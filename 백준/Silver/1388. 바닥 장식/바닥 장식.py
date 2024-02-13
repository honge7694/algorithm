# DFS 사용 : 문자열 패턴 매칭 등에 사용

import sys
input = sys.stdin.readline

def dfs_row(x, y):
	if x >= N or y >= M or x < 0 or y < 0:
		return 0
	
	if tiles[x][y] == '-':
		tiles[x][y] = 0 # 방문 처리
		dfs_row(x, y+1)
		return 1
	return 0

def dfs_column(x, y):
	if x >= N or y >= M or x < 0 or y < 0:
		return 0
	
	if tiles[x][y] == '|':
		tiles[x][y] = 0 # 방문 처리
		dfs_column(x+1, y)
		return 1
	return 0


N, M = map(int, input().split())
tiles = []

for _ in range(N):
	tiles.append(list(input().rstrip()))

count = 0
for i in range(N):
	for j in range(M):
		if tiles[i][j] == '-':
			count += dfs_row(i, j)
		elif tiles[i][j] == '|':
			count += dfs_column(i,j)

print(count)