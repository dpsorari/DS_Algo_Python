class Node(object):
	"""docstring for ClassName"""
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
		print(self.data);
		if self.right : 
			self.right.printInorder()

	def lookup(self,value,parent=None):
		# returns self, parent 
		if value == self.data : 
			return self , parent
		elif value < self.data : 
			if self.left : 
				return self.left.lookup(value,self) 
			else : return self.left , parent 
		elif value > self.data :
			if self.right : 
				return self.right.lookup(value,self)
			else : 
				return self.right , parent
	def delete(self, value, parent=None):
		if self.data==value : 
			if parent==None:
				
root= Node(30)
insertList = [5,64,21,23,52,1,14,41,31]

for x in insertList: 
	root.insert(x)

root.printInorder()

node , parent = root.lookup(31)
print (node.data , parent.data )

