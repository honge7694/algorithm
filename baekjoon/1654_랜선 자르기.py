import sys
input = sys.stdin.readline


K, N = map(int, input().split())
LAN = []
for _ in range(K):
	LAN.append(int(input()))

start = 1 # zero division error 걸릴 수 있어서 1로줘야함
end = max(LAN)


while start <= end:
	mid = (start + end) // 2
	count = 0 # 랜선 수
	
	for x in LAN:
		count += x // mid # 분할하여 더하기
	

	if count < N:
		end = mid - 1
	else:
		start = mid + 1

print(end)
	