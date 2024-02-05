from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
	text = input().split()
	
	if text[0] == "push_front":
		queue.appendleft(text[1])
	elif text[0] == "push_back":
		queue.append(text[1])
	elif text[0] == "pop_front":
		if not queue:
			print("-1")
		else:
			print(queue.popleft())
	elif text[0] == "pop_back":
		if not queue:
			print("-1")
		else:
			print(queue.pop())
	elif text[0] == 'size':
		print(len(queue))
	elif text[0] == 'empty':
		if queue:
			print(0)
		else:
			print(1)
	elif text[0] == 'front':
		if queue:
			print(queue[0])
		else:
			print(-1)
	elif text[0] == 'back':
		if queue:
			print(queue[-1])
		else:
			print(-1)
