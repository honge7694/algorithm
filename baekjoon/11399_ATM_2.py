import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))
result = 0
time.sort()

for i in range(N):
	for j in range(0, i+1):
		result += time[j]

print(result)

