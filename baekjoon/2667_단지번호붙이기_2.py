import sys
input = sys.stdin.readline

N = int(input())

# 지도 생성
graph = []
for i in range(N):
	graph.append(list(map(int, input().strip())))
print()
for i in range(len(graph)):		
	print(graph[i])
