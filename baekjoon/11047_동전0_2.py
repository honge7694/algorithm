import sys
input = sys.stdin.readline

N, K = map(int, input().split())
count = 0
coins = []

for _ in range(N):
	coins.append(int(input()))

# 역순으로 동전 빼기
for coin in reversed(coins):
	if K // coin > 0:
		count += K // coin
		K %= coin

print(count)
