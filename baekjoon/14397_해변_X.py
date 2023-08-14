"""
단위 정육각형 이루어져 있는 지도가 주어졌을 때, 
해변의 길이를 구하는 프로그램을 작성하시오.

해변은 정육각형의 변 중에서 한 쪽은 물인데, 한 쪽은 땅인 곳을 의미한다.

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 50)
둘째 줄부터 N개의 줄에 지도가 주어진다. '.'은 물, '#'은 땅이다.
"""

def dfs(x, y):
    global result 
    if x >= N or x < 0 or y >= M or y < 0: # 범위 밖 확인
        return False

    if beach[x][y] == '.':
        beach[x][y] = 1 # 현재 노드 방문

        # 상, 하, 좌, 우 확인
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    if beach[x][y] == '#':
        result += 1
    return False

N, M = map(int, input().split())
beach = []

for _ in range(N):
    beach.append(list(input()))

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
