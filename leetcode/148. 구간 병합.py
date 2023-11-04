class ListNode:
	def __init__(self, val=None, next=None):
		self.val = val
		self.next = next
		

class LinkedList:
	def __init__(self, head=None):
		self.head = None
		
	def __str__(self):
		curr = self.head
		result = []

		while curr:
			result.append(curr.val)
			curr = curr.next
		
		return " -> ".join(map(str, result))
	
	def append(self, val):
		if not self.head:
			self.head = ListNode(val)
		else:
			curr = self.head
			
			while curr.next:
				curr = curr.next
			
			curr.next = ListNode(val)
	
	def sort_list(self):
		curr = self.head
		values = []
		
		while curr:
			values.append(curr.val)
			curr = curr.next
		
		values.sort()
		
		curr = self.head
		for val in values:
			curr.val = val
			curr = curr.next
			
		return self.head

lst = [4, 2, 1, 3]
link = LinkedList()

for i in lst:
	link.append(i)

print(link)

link.sort_list()
print(link)