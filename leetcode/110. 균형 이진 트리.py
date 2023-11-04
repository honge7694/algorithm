class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def __init__(self):
		self.root = None
		self.result = True
		
	def make_tree_by(self, lst, index):
		parent = None
		
		if len(lst) > index:
			value = lst[index]
			
			parent = Node(value)
			parent.left = self.make_tree_by(lst, 2 * index + 1)
			parent.right = self.make_tree_by(lst, 2 * index + 2)
		
		if index == 0:
			self.root = parent
		return parent
			
	
	def isBalanced(self, root):
		def dfs(node):
			
			if self.result == False:
				return 
			
			if node is None:
				return 0
			
			left = dfs(node.left) + 1
			right = dfs(node.right) + 1
			
			if abs(left - right) > 1:
				self.result = False
				return 0
			
			return max(left, right)
			
		dfs(root)
		return self.result
			
lst = [3,9,20,None,None,15,7]
s1 = Solution()
s1.make_tree_by(lst, 0)
print(s1.isBalanced(s1.root))