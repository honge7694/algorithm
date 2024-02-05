import sys
input = sys.stdin.readline
import heapq

# N번째 큰수는 결국 뒤에서 N번째로 큰 수를 뽑으라는 것
# N개의 리스트를 유지하며 작은것 빼기
N = int(input())
result = []

for _ in range(N):
	numbers = map(int, input().split())
	for num in numbers:
		if len(result) < N:
			heapq.heappush(result, num)
		else:
			if result[0] < num:
				heapq.heappop(result)
				heapq.heappush(result, num)
print(result[0])

# info: N번보다 큰 수는 필요 없다. 라는 것을 눈치채야한다.










"""
n ^ 2에 모두 넣고 하면 실패 (메모리 초과)
tmp = [list(map(int, input().split())) for _ in range(N)]
heapq.heapify(tmp)
for i in range(1, len(tmp)):
	if maxNum > tmp[i][-1]:
		continue
	else :
		for j in tmp[i]:
			if count == N:
				break
			if maxNum < j :
				maxNum = j
				count += 1
"""