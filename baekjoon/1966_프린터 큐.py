from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	N, M = map(int, input().split())
	W = deque(list(map(int, input().split())))
	W = deque([(idx, value) for idx, value in enumerate(W)])
	count = 0
	while(True):
		# 가중치가 제일 큰 수면 pop
		if W[0][1] == max(W, key=lambda x: x[1])[1]:
			count += 1
			if (W[0][0] == M):
				print(count)
				break
			else:
				W.popleft()
		# 제일 큰 수가 아니면 뒤로
		else:
			W.append(W.popleft())

