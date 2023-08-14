import sys
from collections import deque


def bfs():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= N or ny < 0 or nx >= M or nx < 0:
                continue
            
            if graph[ny][nx] != -1 and graph[ny][nx] == 0:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny, nx))
    

M, N = map(int, sys.stdin.readline().split())
result = 0
queue = deque()

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append((i, j))

bfs()

if any(0 in i for i in graph):
    sys.stdout.write('-1')
else:
    result = [ max(i) for i in graph]
    sys.stdout.write(str(max(result)-1))


