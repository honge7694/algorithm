import sys 
from itertools import permutations
sys.setrecursionlimit(10**6) 

def input(): 
	return sys.stdin.readline().strip()

def dfs():
	result = list(permutations(nums, 3))
	return result

nums = [1, 2, 3]
print(dfs())

