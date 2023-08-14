import sys

# 세로길이 N 가로길이 M
N, M = map(int, sys.stdin.readline().split())
ice_box = []
for _ in range(N):
    ice_box.append(list(map(int, sys.stdin.readline().strip())))

print(ice_box)

def dfs(x, y):
    if x >= N or x <= -1 or y >= M or y <= -1:
        return False
    if ice_box[x][y] == 0:
        ice_box[x][y] = 1

        dfs(x+1, y) # 하
        dfs(x-1, y) # 상
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

sys.stdout.write(str(result))