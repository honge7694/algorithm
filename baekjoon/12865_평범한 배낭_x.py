import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bag = []
for _ in range(N):
	bag.append(list(map(int, input().split())))

result = 0
for i in range(0, len(bag)-1):
	# K보다 무게가 작은지 확인
	if K < bag[i][0]:
		continue
	if result < bag[i][1]:
		result = bag[i][1]
	# 더 들어갈 수 있는지 확인
	for j in range(i+1, len(bag)):
		if bag[i][0] + bag[j][0] <= K and bag[i][1] + bag[j][1] > result :
			result = bag[i][1] + bag[j][1]
		
print(result)