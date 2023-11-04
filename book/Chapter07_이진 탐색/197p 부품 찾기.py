def search(lst, target, start, end):
	if start > end:
		return False
	
	mid = (start + end) // 2
	
	if lst[mid] == target:
		return True
	elif lst[mid] > target:
		return search(lst, target, start, mid-1)
	else:
		return search(lst, target, mid+1, end)


N = int(input())
shop = list(map(int, input().split()))

M = int(input())
guest = list(map(int, input().split()))

result = []
shop.sort()
for g in guest:
	if search(shop, g, 0, len(shop)-1):
		result.append(True)
	else:
		result.append(False)

print(result)