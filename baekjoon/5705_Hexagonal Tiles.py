import sys
input = sys.stdin.readline
INF = int(1e9)


while True:
	node = int(input())
	
	if node == 0:
		break
	
	# tiles = [ i for i in range(node+1)]
	
	# graph 그리기
	graph = [[INF] * (node+1)  for _ in range(node+1)]
	
	# graph 값 넣기
	for i in range(3, node+1):
		if i >= 3 and i <= node - 2: # 시작 2개와 끝 2개 빼고
			for j in range(i-2, i+3):
				graph[i][j] = 1
		# elif i >= 3 and i < node - 2:
		else:
			for j in range(i-2, i+1):
				graph[i][j] = 1
			
				
	# i == j = 0
	for i in range(1, node+1):
		graph[i][i] = 0
	
	for i in range(1, node+1):
		for j in range(1, node+1):	
			print(graph[i][j], end=' ')
		print("")
	# 점화식
	# graph



