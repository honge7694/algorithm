import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sortedCheck = True

for _ in range(M):
	int(input())
	books = list(map(int, input().split()))
	if books != sorted(books, reverse=True):
		sortedCheck = False
		break

if sortedCheck:	
	print("Yes")
else:
	print("No")
	

# warning
# 입력 받을 때 현재 값과 전값을 비교
# code 주석, 어디가 헷갈렸는지 주석.
# 왜 ㅇㅇ를 이용하여 풀었는지 남기기.