import sys
input = sys.stdin.readline
INF = int(1e9)


# 노드, 간선
n, m = map(int, input().split())
# 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
	for b in range(1, n+1):
		if a == b:
			graph[a][b] = 0

# 간선 입력
for _ in range(m):
	# A와 B가 서로에게 가는 비용은 1이라고 설정
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1
	
# 소개팅 x와 목적지 k
x, k = map(int, input().split())

# 점화식에 따라 플로이드 위셜 알고리즘을 수행
# 점화식을 통해 k=1일떄, 2-3이 먼저 바뀌는데 이 경우는 2에서 3을 못갔지만 
# 1번 노드를 갔다가, 1번노드와 연결되어있는 3번 노드로 가서 2번의 이동으로 2-3에는 2가 들어간다.

for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
distance = graph[1][k] + graph[k][x]

# 도달 할 수 없는 경우, -1을 출력
if distance >= INF:
	print("-1")
# 도달 할 수 있는 경우, 최단 거리를 출력
else:
	print(distance)


"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
"""

