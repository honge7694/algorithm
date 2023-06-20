import sys

N = sys.stdin.readline()
row = int(N[1])
column = int(ord(N[0])) - int(ord('a')) + 1
count = 0


moves = [(-2, -1), (-1, -2), (2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2)]

for move in moves:
    next_row = row + move[1]
    next_column = column + move[0]

    if next_row > 8 or next_row < 1 or next_column > 8 or next_column < 1:
        continue

    count += 1

sys.stdout.write(str(count))

