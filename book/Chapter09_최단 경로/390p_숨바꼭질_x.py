import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

print(graph)