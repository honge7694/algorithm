import sys
input = sys.stdin.readline


N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)

while start <= end:
	mid = (start + end) // 2
	total = 0
	
	for x in trees:
		if x > mid:
			total += x - mid
	
	if total >= M:
		start = mid + 1
		result = end
	else:
		end = mid - 1

print(end)
