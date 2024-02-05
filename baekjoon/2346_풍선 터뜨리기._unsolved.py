from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
balloons = deque(map(int, input().split()))
balloons = deque([(idx, value) for idx, value in enumerate(balloons)])
result = []
nextBalloon = ()

while True:
	if not balloons:
		break
	# 첫 풍선
	if not result:
		boom = balloons[0] # 풍선 찾고,
		result.append(boom[0]+1) # 풍선 인덱스 등록
		nextBalloon = balloons[boom[1]] # 다음 터질 풍선
		balloons.popleft() # 풍선 터치기
	elif len(balloons) == 1:
		result.append(balloons[0][0]+1) # 풍선 인덱스 등록
		balloons.pop()
	else:
		boom = balloons.index(nextBalloon) # 현재 터질 풍선 인덱스 찾고,
		result.append(nextBalloon[0]+1) # 풍선 인덱스 등록
		if (boom + nextBalloon[1]) < len(balloons): # index out of range
			nextBalloon = balloons[boom + nextBalloon[1]] # 다음 터질 풍선
		else:
			nextBalloon = balloons[(boom + nextBalloon[1]) % len(balloons)]
		balloons.remove(balloons[boom]) # 풍선 터치기

print(' '.join(map(str, result)))


# 1, 2, 3, 4, 5
# 2, 3, 4, 5, 1
# 3, 4, 5, 1
# 이런식이면 원형 연결리스트 => 덱
# 동그라미를 만들고 계속 돌려야한다 = 덱
