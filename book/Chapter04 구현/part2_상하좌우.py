"""
1. 조건 : x가 1미만, N초과 되면 멈춤, y가 1미만, N초과 되면 멈춤.
2. 입력받은 N 만큼 이동계획을 받는다.
3. N만큼 반복하며, 변화하는 x, y에 값을 더한다.
4. 조건에 맞지않으면 더하지 않는다.
"""

import sys

N = int(sys.stdin.readline())
plans = sys.stdin.readline().split()
x, y = 1, 1
move_x, move_y = 0, 0

moves = ['L', 'R', 'U', 'D']
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

for plan in plans:
    for index, move in enumerate(moves):
        if move == plan:
            move_x = x + mx[index]
            move_y = y + my[index]
            
            if move_x < 1 or move_x > N or move_y < 1 or move_y > N:
                continue
            x, y = move_x, move_y
    # move_x, move_y = x, y

sys.stdout.write(str(x))
sys.stdout.write(" ")
sys.stdout.write(str(y))
