from collections import deque
import sys


T = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    # queue 선언
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]

            if mx >= N or mx < 0 or my >= M or my < 0:
                continue

            # 0일시 배추 x
            if graph[mx][my] == 0:
                continue
            
            # 방문 처리
            if graph[mx][my] == 1:
                graph[mx][my] = 0
                queue.append((mx, my))
    return


for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())

    graph = [
        [0] * M for _ in range(N)
    ]

    # 배추 심은 위치 입력
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x][y] = 1 # 배추 1로 초기화

    result = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    sys.stdout.write(str(result))
    sys.stdout.write('\n')

