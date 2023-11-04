def insertionSortList(head):
	
	for i in range(1, len(head)):
		for j in range(1, i+1):
			temp = i - j
			
			if head[temp] > head[temp+1]:
				head[temp], head[temp+1] = head[temp+1], head[temp]
			else:
				break
	
	return head


head = [4, 2, 1, 3]

print(insertionSortList(head))