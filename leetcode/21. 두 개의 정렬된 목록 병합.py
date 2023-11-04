class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
class LinkedList:
	
	def __init__(self, head=None):
		self.head = head
		
	def __str__(self):
		curr = self.head
		result = []

		while curr:
			result.append(curr.val)
			curr = curr.next
		
		return " -> ".join(map(str, result))
	
	def mergeTwoLists(self, list1, list2):
		dummy = ListNode()
		current = dummy
		
		while list1 and list2:
			if list1.val < list2.val:
				current.next = list1
				list1 = list1.next
			else:
				current.next = list2
				list2 = list2.next
			current = current.next
		
		while list1:
			current.next = list1
			list1 = list1.next
			current = current.next
		while list2:
			current.next = list2
			list2 = list2.next
			current = current.next
		
		
		return LinkedList(dummy.next)
	
	def append(self, val):
		if not self.head:
			self.head = ListNode(val)
		else:
			curr = self.head
			
			while curr.next:
				curr = curr.next
			
			curr.next = ListNode(val)
		

lst1 = [1, 2, 4]
lst2 = [1, 3, 4]
a = LinkedList()
b = LinkedList()
for i in lst1:
	a.append(i)
for j in lst2:
	b.append(j)

merged = a.mergeTwoLists(a.head, b.head)
print(merged)



