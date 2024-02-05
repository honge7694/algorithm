import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sites = dict()

for _ in range(N):
	site, password = input().split()
	sites[site] = password

for _ in range(M):
	site = input().strip()
	print(sites.get(site))