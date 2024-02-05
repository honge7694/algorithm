import sys
input = sys.stdin.readline

N, GAME = list(input().split())

play = [input().strip() for _ in range(int(N))]
play = set(play)

if GAME == "Y" :
	print(len(play))
elif GAME == "F" :
	print(len(play) // 2)
elif GAME == "O" :
	print(len(play) // 3)