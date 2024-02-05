import sys
input = sys.stdin.readline

N = int(input())
result = 0

for i in range(N):
	temp = [i]
	for j in str(i):
		temp.append(int(j))
	if sum(temp) == N:
		result = i
		break

print(result)