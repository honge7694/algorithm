import sys, math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
	x, y = map(int, input().split())
	distance = y - x
	move_count = 0 # 이동 횟수
	
	num = math.floor(math.sqrt(distance))
	num_square = num ** 2
	num_square_plus = math.sqrt(num_square)
	
	if distance > num_square + num_square_plus: # ex) x, y = 0, 7
		move_count = 2 * num + 1 
	elif distance > num_square and distance <= num_square + num_square_plus: # ex) x, y = 0, 6
		move_count = 2 * num
	elif distance == num_square: # ex) x, y = 0, 4
		move_count = 2 * num - 1
		
	if distance <= 3:
		count = distance
	
	print(move_count)

