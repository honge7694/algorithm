import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
temp = 0

for i in range(len(arr)):
	for j in range(i+1, len(arr)):
		for k in range(j+1, len(arr)):
			temp = arr[i] + arr[j] + arr[k]
			if result < temp <= M:
				result = temp
print(result)
	