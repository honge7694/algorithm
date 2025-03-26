import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
myQueue = deque([i for i in range(1, N+1)])
nums = list(map(int, input().split()))
count = 0

for num in nums:
	while(True) :
		# 같을 때
		if myQueue[0] == num:
			myQueue.popleft()
			break
		else:
			# 오른쪽 이동(원소 : 맨 뒤 -> 맨 앞)
			if myQueue.index(num) > len(myQueue) / 2:
				myQueue.appendleft(myQueue.pop())
				count += 1
			# 왼쪽 이동 (원소 : 맨 앞 -> 맨 뒤)
			else:
				myQueue.append(myQueue.popleft())
				count += 1

print(count)
