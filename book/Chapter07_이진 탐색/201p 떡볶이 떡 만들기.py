def search(lst, target):
	start = 0
	end = max(lst)
	result = 0
	
	# 재귀보다는 반복문이 더 쉽다.
	while start <= end:
		total = 0
		mid = (start + end) // 2
		
		# 떡을 자른 후 남은 길이를 total에 더함.
		for x in lst:
			if x > mid:
				total += x - mid
		
		# 떡이 원하는 길이보다 작으면 덜 자른다.
		if total < target:
			end = mid - 1
		# 떡이 원하는 길이보다 많으면 더 자른다.
		else:
			result = mid
			start = mid + 1
		
	return result



N, M = map(int, input().split())
lst = [19, 15, 10, 17]

print(search(lst, M))