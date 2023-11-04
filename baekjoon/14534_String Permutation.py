def dfs(path):
	if len(L) == len(path):
		print(path)
		return
	
	for i in range(len(L)):
		if L[i] not in path:
			dfs(path+L[i])

T = int(input())

for i in range(T):
	L = input()
	print(f"Case # {i+1}:")
	dfs("")

