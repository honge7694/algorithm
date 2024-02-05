import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	x, y = map(int, input().split())
	distance = y - x
	
	n = 0
	
	while True:
		if distance <= n*(n+1):
			break
		n += 1
	
	# 총 이동 거리가 n의 제곱보다 작거나 같을 때
	if distance <= n**2:
		print(n*2-1)
	# 총 이동 거리가 n의 제곱보다 클 때
	else:
		print(n*2)
