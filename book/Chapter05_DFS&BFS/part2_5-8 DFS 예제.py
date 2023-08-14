def dfs(graph, start, visited):
    # 처음 방문 노드
    visited[start] = True

    # 방문 노드 출력
    print(start, end=' ')

    # 노드와 연결된 다른 노드를 재귀적으로 방문
    for graph_node in graph[start]:
        if not visited[graph_node]:
            dfs(graph, graph_node, visited)

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

visited = [False] * 9

dfs(graph, 1, visited)