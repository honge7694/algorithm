import sys
input = sys.stdin.readline

def search(lst, budget):
	start = 1
	end = max(lst)
	
	while start <= end:		
		total = 0
		mid = (start + end) // 2
		
		for x in lst:
			# 제출 예산 or 책정된 예산을 더한다.
			total += min(x, mid)
		
		# total(지방 총 예산) 값이 정부 예산보다 적다.
		if total <= budget:
			start = mid + 1

		# total(지방 총 예산) 값이 정부 에산보다 많다.
		elif total > budget:
			end = mid - 1
	
	return end
	



# N = int(input())
# cities = list(map(int, input().split()))
# budget = int(input())
cities = [120, 110, 140, 150]
budget = 485

print(search(cities, budget))