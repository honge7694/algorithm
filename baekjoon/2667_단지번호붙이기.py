import sys


def dfs(height, width):
    if height >= N or height < 0 or width >= N or width < 0:
        return False
    
    global apart
    
    if graph[height][width] == 1:
        # 방문 처리
        graph[height][width] = 0
        apart += 1

        # 상하좌우
        dfs(height-1, width)
        dfs(height+1, width)
        dfs(height, width-1)
        dfs(height, width+1)
        
        return True
    return False

N = int(sys.stdin.readline())

# 지도 생성
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

result = 0
apart = 0
apart_result = []
for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            result += 1
            apart_result.append(apart)
            apart = 0

sys.stdout.write(str(result) + '\n')
apart_result.sort()
[sys.stdout.write(str(apart_result[i]) + '\n') for i in range(len(apart_result))]

