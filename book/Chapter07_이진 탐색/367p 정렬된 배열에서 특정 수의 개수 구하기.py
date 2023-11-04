def count_value(lst, x):
	n = len(lst)
	
	a = first_index(lst, 0, n-1, x)
	b = last_index(lst, 0, n-1, x)
	
	return b - a + 1

def first_index(lst, start, end, target):
	if start > end:
		return None

	mid = (start + end) // 2			
	
	# 0 또는 target > lst[mid-1]인 이유는 target의 가장 작은 인덱스를 찾기위해서다.
	if (mid == 0 or target > lst[mid-1]) and lst[mid] == target:
		return mid
	elif lst[mid] >= target:
		return first_index(lst, start, mid-1, target)
	else:
		return first_index(lst, mid+1, end, target)

def last_index(lst, start, end, target):
	if start > end:
		return None
	
	mid = (start + end) // 2
	
	if (mid == N-1 or target < lst[mid+1]) and lst[mid] == target:
		return mid
	elif lst[mid] > target:
		return last_index(lst, start, mid-1, target)
	else:
		return last_index(lst, mid+1, end, target)
	
	


N, x = map(int, input().split())
lst = list(map(int, input().split()))

count = count_value(lst, x)

if count == 0 :
	print(-1)
else:
	print(count)