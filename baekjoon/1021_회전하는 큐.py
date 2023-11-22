import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
position = list(map(int, input().split()))
deq = deque([ i for i in range(1, N+1)])

count = 0
for i in position:
	while True:
		if deq[0] == i: # 뽑으려는 수와 위치가 같을 때
			deq.popleft()
			break
		else:
			if deq.index(i) < len(deq) / 2: # 뽑으려는 수 인덱스가 중간보다 작을 때
				while deq[0] != i: # 뽑으려는 수와 같아질 때까지 반복
					deq.append(deq.popleft()) # 맨 뒤로 보냄
					count += 1
			else:
				while deq[0] != i:
					deq.appendleft(deq.pop()) # 맨 앞으로 보냄
					count += 1

print(count)