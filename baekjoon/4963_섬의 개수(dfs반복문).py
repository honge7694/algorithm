import sys


def dfs(height, width):
    stack = [(height, width)]

    while stack:
        y, x = stack.pop()

        if y >= h or y < 0 or x >= w or x < 0:
            continue
        
        if graph[y][x] == 1:
            # 방문 처리
            graph[y][x] = 0

            # 상하좌우 
            stack.append((y-1, x))
            stack.append((y+1, x))
            stack.append((y, x-1))
            stack.append((y, x+1))

            # 대각선
            stack.append((y-1, x-1)) # 왼쪽 위
            stack.append((y-1, x+1)) # 오른쪽 위
            stack.append((y+1, x-1)) # 왼쪽 아래
            stack.append((y+1, x+1)) # 오른쪽 아래



while True:
    w, h = map(int, sys.stdin.readline().split())

    # 종료 조건
    if w == 0 & h == 0:
        break
    
    # 지도 초기화
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1

    sys.stdout.write(str(result))
    sys.stdout.write('\n')

