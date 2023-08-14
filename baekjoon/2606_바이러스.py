import sys
from collections import deque


computer = int(sys.stdin.readline())
edge = int(sys.stdin.readline())
result = 0

graph = [[False] * (computer + 1) for _ in range(computer + 1)]

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (computer+1)

def bfs():
    global result
    queue = deque([1])
    visited[1] = True

    while queue:
        node = queue.popleft()
        for i in range(computer+1):
            if not visited[i] and graph[node][i]:
                visited[i] = True
                queue.append(i)
                result += 1

def dfs(v):
    global result
    visited[v] = True

    for i in range(computer+1):
        if not visited[i] and graph[v][i]:
            dfs(i)
            result += 1


dfs(1)
# bfs()
print(result)




