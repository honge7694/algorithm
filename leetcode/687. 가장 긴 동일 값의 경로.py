class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		

class Solution:
	def __init__(self):
		self.root = None
		self.result = 0
	
	def make_by_tree(self, lst, index):
		parent = None
		
		if len(lst) > index:
			value = lst[index]
			
			if value is None:
				return
			
			parent = Node(value)
			parent.left = self.make_by_tree(lst, 2 * index + 1)
			parent.right = self.make_by_tree(lst, 2 * index + 2)
			
			return parent
		if index == 0:
			self.root = parent
			
		return parent
	
	def longestUnivaluePath(self, root):
		def dfs(node):
			if node is None:
				return 0
			
			left = dfs(node.left)
			right = dfs(node.right)
			
			if node.left and node.left.val == node.val:
				left += 1
			else:
				left = 0
				
			if node.right and node.right.val == node.val:
				right += 1
			else:
				right = 0
			
			self.result = max(self.result, left + right)
			return max(left, right)
		
		dfs(root)
		return self.result
	

lst = [1, 4, 5, 4, 4, None, 5]
s1 = Solution()
lst_tree = s1.make_by_tree(lst, 0)
result = s1.longestUnivaluePath(lst_tree)
print(result)
