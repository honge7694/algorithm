from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
inCar = [input() for _ in range(N)]
outCar = [input() for _ in range(N)]
inDic = {}
outDic = {}
count = 0

for idx, value in enumerate(inCar):
	inDic[value] = idx
for idx, value in enumerate(outCar):
	outDic[value] = idx

for car in inCar:
	if outDic[car] - inDic[car] < 0: 
		# 조건 : 1 2 3 4 5
		#       3 2 1 4 5
		# 3번과 2번 모두 추월 << 문제
		count += 1

print(count)

# 1등 > 5등
#