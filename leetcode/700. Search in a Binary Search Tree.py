class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		

class Solution:
	def __init__(self):
		self.root = None
		self.result = []
		
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
		
	def searchBST(self, root, val):
		def dfs(node):
			if not node:
				return None

			dfs(node.left)
			dfs(node.right)
			
			if node.val == val:
				self.result.append(node.val)
				if node.left is not None:
					self.result.append(node.left.val)
				if node.right is not None:
					self.result.append(node.right.val)

		dfs(root)
		return self.result
	
	
lst = [4, 2, 7, 1, 3]
s1 = Solution()
s1.make_tree_by(lst, 0)
print(s1.searchBST(s1.root, 2))