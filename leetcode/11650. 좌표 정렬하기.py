# 참고하기 : https://herbi1411.tistory.com/entry/BOJ-%EC%A2%8C%ED%91%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B011650-PYTHON

import sys
input = sys.stdin.readline

def quick_sort(lst, start, end):
	def partition(part, ps, pe):
		pivot = part[pe]
		i = ps - 1
		for j in range(ps, pe):
			if part[j] <= pivot:
				i += 1
				part[i], part[j] = part[j], part[i]
		part[i+1], part[pe] = part[pe], part[i+1]
	
		return i+1
	
	if start >= end:
		return None
	
	p = partition(lst, start, end)
	quick_sort(lst, start, p-1)
	quick_sort(lst, p+1, end)
	
	return lst

N = int(input())
lst = []
for _ in range(N):
	lst.append(list(map(int, input().split())))

quick_sort(lst, 0, N-1)

for i in lst:
	print(' '.join(map(str, i)))