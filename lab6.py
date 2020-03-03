from lab6_p1 import Node



class LinkedList:
	def __init__(self, head = None, tail = None):
		self.head = head
		self.size = size
		sel.tail  = tail


	def getSize(self, head):
		return(self.size)

	def setSize(self, s):
		self.size = s


	def getHead(self, head):
		return(self.head)

	def setHead(self, h):
		self.head = h


	def getTail(self, tail):
		return(self.tail)

	def setTail(self, t):
		self.tail = t


	def isEmpty(self):
		if(self.getSize() == 0):
			return(True)
		return(False)


	def addNode(self, d):
		newNode = Node(data = d)

		if(self.isEmpty()):
			self.setHead(newNode)
		else:
			#temp_tail = self.getTail()
			self.getTail().setnextPointer(newNode)
		self.setTail(newNode)
		self.setSize(self.size + 1)


def main():

	LL = LinkedList()
	print(LL.getSize())

	LL.addNode(3000)

	#checking
	print(LL.getTail().getData())

if __name__ == '__main__':
	main()