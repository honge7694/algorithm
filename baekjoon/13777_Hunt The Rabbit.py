import sys
input = sys.stdin.readline


def search(target, start, end):
	if start > end:
		return 
	
	mid = (start + end) // 2
	print(mid, end=' ')
	
	if target == mid:
		return
	elif target > mid:
		return search(target, mid+1, end)
	else:
		return search(target, start, mid-1)

while True:
	envelopes = int(input())
	
	if envelopes == 0:
		break
	
	search(envelopes, 1, 50)
	print("")