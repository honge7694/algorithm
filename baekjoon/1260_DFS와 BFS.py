import sys
from collections import deque

def dfs(v):
    # 첫번째 노드 방문
    dfs_visited[v] = True
    sys.stdout.write(str(v))
    sys.stdout.write(' ')

    # 방문하지 않은 노드 and graph[v][i] True
    for i in range(N+1):
        if not dfs_visited[i] and graph[v][i]:
            dfs(i) # dfs 탐색
    

def bfs(v):
    # queue 선언
    queue = deque([v])
    # bfs_visited 처음 방문
    bfs_visited[v] = True

    while queue:
        node = queue.popleft()
        sys.stdout.write(str(node))
        sys.stdout.write(' ')
        for i in range(1, N+1):
            # 방문하지 않은 노드 and graph[node][i] True
            if not bfs_visited[i] and graph[node][i]:
                queue.append(i)
                bfs_visited[i] = True

N, M, V = map(int, sys.stdin.readline().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a][b] = True
    graph[b][a] = True

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

dfs(V)
sys.stdout.write('\n')
bfs(V)
