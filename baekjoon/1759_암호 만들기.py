# 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 

import sys 
sys.setrecursionlimit(10**6) 

def input(): 
	return sys.stdin.readline().strip()

def dfs(index, path):
	if len(path) == L:
		result.append(path)
		return


	for i in range(index, C):
		if password[i] not in path:
			dfs(index+1, path+password[i])
    

result = []
L, C = map(int, input().split()) 
password = (input().split())

dfs(0, "")
print(result)
print(len(result))
