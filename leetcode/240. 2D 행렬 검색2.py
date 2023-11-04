def search(lst, target, start, end):
	if start > end:
		return False
	
	mid = (start + end) // 2
	
	# mid와 target이 같은 경우 
	if lst[mid] == target:
		return True
	# mid가 target보다 큰 경우
	elif lst[mid] > target:
		return search(lst, target, start, mid-1)
	# mid가 target보다 작은 경우
	else:
		return search(lst, target, mid+1, end)

lst = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17, 24],[18,21,23,26,30]]
target = 5
temp = True

for l in lst:
	if search(l, target, 0, len(l)-1):
		print(True)
		break