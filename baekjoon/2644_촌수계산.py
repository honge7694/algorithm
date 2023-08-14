import sys
from collections import deque

node = int(sys.stdin.readline())
people1, people2 = map(int, sys.stdin.readline().split())
edge = int(sys.stdin.readline())
result = []

graph = [[0] * (node+1) for _ in range(node+1)]

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0] * (node+1)

def dfs(v, num):
    num += 1
    visited[v] = 1

    if v == people2:
        result.append(num)
    
    for i in range(node+1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i, num)

dfs(people1, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)


