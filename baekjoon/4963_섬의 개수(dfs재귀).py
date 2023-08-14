"""
RuntimeError: RecursionError: maximum recursion depth exceeded 에러 발생
재귀 대신 반복문을 사용하여 DFS 알고리즘을 구현하는 것이 좋음

"""

import sys
from collections import deque


def dfs(height, width):
    if width >= w or width < 0 or height >= h or height < 0:
        return False

    if graph[height][width] == 1:
        # 방문 처리
        graph[height][width] = 0

        # 상하좌우 대각선 확인
        dfs(height-1, width)
        dfs(height+1, width)
        dfs(height, width-1)
        dfs(height, width+1)
        dfs(height-1, width-1) # 왼쪽 위 대각선
        dfs(height-1, width+1) # 오른쪽 위 대각선
        dfs(height+1, width-1) # 왼쪽 아래 대각선
        dfs(height+1, width+1) # 오른쪽 아래 대각선

        return True
    return False


while True:
    w, h = map(int, sys.stdin.readline().split())

    # 종료 조건
    if w == 0 and h == 0:
        break
    
    # 지도 생성
    graph = []
    for _ in range(h):
        # 땅 초기화
        graph.append(list(map(int, sys.stdin.readline().split())))

    result = 0

    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    sys.stdout.write(str(result))
    sys.stdout.write('\n')


