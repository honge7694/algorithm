import sys


T = int(sys.stdin.readline())

def bfs(x, y):
        # 범위를 벗어나면 False
        if x >= N or x < 0 or y >= M or y < 0:
            return False
        
        if graph[x][y] == 0:
            return False
        
        # 배추가 심어져 있다면
        if graph[x][y] == 1:
            # 배추 방문
            graph[x][y] = 0

            # 상하좌우 확인
            bfs(x-1, y)
            bfs(x+1, y)
            bfs(x, y-1)
            bfs(x, y+1)

            return True
        return False

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split()) # 세로, 가로, 배추위치

    graph = [
        [0] * M for _ in range(N) # 배추밭 0 초기화
    ]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split()) # 배추심은 위치 입력
        graph[x][y] = 1 # 배추 1로 초기화

    result = 0
    for i in range(N):
        for j in range(M):
            if bfs(i, j) == True:
                result += 1
    sys.stdout.write(str(result))
    sys.stdout.write('\n')
