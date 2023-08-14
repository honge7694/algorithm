from collections import deque


# BFS 메서드 정리
def bfs(graph, first, visited):
    visited[first] = True

    queue = deque([first])
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for graph_node in graph[v]:
            if not visited[graph_node]:
                visited[graph_node] = True
                queue.append(graph_node)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

bfs(graph, 1, visited)