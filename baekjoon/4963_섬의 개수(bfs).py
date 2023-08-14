import sys
from collections import deque


def bfs(height, width):
    dheight = [-1, 1, 0, 0, -1, -1, 1, 1] 
    dwidth = [0, 0, -1, 1, -1, 1, -1, 1]

    queue = deque()
    queue.append((height, width))

    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny = y + dheight[i] 
            nx = x + dwidth[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny,nx))



while True:
    w, h = map(int, sys.stdin.readline().split())

    # 종료 조건
    if w == 0 & h == 0:
        break

    # 지도 생성
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    # 결과
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    sys.stdout.write(str(result) + '\n')