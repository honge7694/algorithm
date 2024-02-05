import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
	x1, y1, r1, x2, y2, r2 = map(int, input().split())
	distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 두 원의 거리
	
	if distance == 0 and r1 == r2: # 동심원 및 반지름 같음 (위치 무한개)
		print(-1)
	elif abs(r1-r2) == distance or r1 + r2 == distance: # 내접, 외접
		print(1)
	elif abs(r1-r2) < distance < (r1+r2): # 두 원이 두점에서 교차
		print(2)
	else:  # 만나지 않음
		print(0)