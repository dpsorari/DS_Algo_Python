class Node(object):
	"""Basic operations with a binary search Tree"""
	def __init__(self, value):
		self.left = None
		self.right = None
		self.data =value

	def insert(self, value):
		if(value < self.data) :
			if self.left : 
				self.left.insert(value)
			else : self.left = Node(value)

		elif(value > self.data) :
			if self.right : 
				self.right.insert(value)
			else : self.right = Node(value)

	def printInorder(self):
		if self.left :
			self.left.printInorder() 
		print(self.data , end = ' | ')
		if self.right : 
			self.right.printInorder()

	def lookup(self,value,parent=None):
		# returns self, parent 
		if value == self.data : 
			return self , parent
		elif value < self.data : 
			if self.left : 
				return self.left.lookup(value,self) 
			else : return None , None 
		elif value > self.data :
			if self.right : 
				return self.right.lookup(value,self)
			else : 
				return None , None
	def countChild(self,parent) :
		count =0
		if parent.left : count+=1
		if parent.right : count+=1

		return count 

	def find_successor(self, node):
		currentNode=node.right
		while currentNode.left is not None:
			currentNode=currentNode.left
		return currentNode	

	def delete(self, value ,parent=None):
		node, parent = self.lookup(value,parent)
		if node is None : 
			return  self
		children= self.countChild(node)
		
		if children == 0 :
			if parent is None:
				del node
				return None 
			if parent.left is node: 
				parent.left=None
			else : parent.right = None
			
			del node
			
		elif children==1: 
			if parent is None:
				parent =node
				node= node.left if node.left else node.right
				del parent
				return node

			elif node.left :
				if parent.left is node : 
					parent.left =node.left
				else :
					parent.right= node.left
			else :
				if parent.left is node : 
					parent.left =node.right
				else :
					parent.right= node.right
		
			del node

		else :
			suc = self.find_successor(node)
			temp= suc.data
			suc.data =node.data
			node.data=temp
			node.right=node.right.delete(suc.data,node)

		return self 

