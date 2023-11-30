import sys
from collections import deque

n, k = map(int, input().split())
deq = deque([i for i in range(1, n+1)])

res = []
while len(deq) != 0:
	for _ in range(k-1):
		# k번째까지 노드 이동
		deq.append(deq.popleft())
	# k 번째 노드 삭제 후 결과 배열에 추가
	res.append(str(deq.popleft()))

print('<', ", ".join(res), '>', sep="")
