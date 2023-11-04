def search(lst, target, path, start, end):
	if start > end:
		return False
	
	mid = (start + end) // 2
	
	if target == 0 or sum(lst) == target:
		if sum(lst) == target:
			return lst
		return path
	
	if lst[mid] == target:
		return search(lst, target-lst[mid], path+[lst[mid]], start+1, mid+1)
	elif lst[mid] < target:
		return search(lst, target, path, mid+1, end)
	else:
		return search(lst, target, path, start, mid-1)


nums = [2, 7, 11, 15]
target = 9

print(search(nums, target, [], 0, len(nums)-1))
