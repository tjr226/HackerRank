class Node(object):

	def __init__(self, name=None, data=None, next=None):
		'''
		creates new node
		next is the next node
		'''
		self.data = data
		self.next = next
		self.name = name
	
	def has_cycleHR(head):
		cycle=False
		slow=head
		fast=head
		while head and head.next:
			print("heads", head.name, head.next.name)
			print("fast and slow", slow.name, fast.name)
			slow=slow.next
			fast=fast.next.next
			if slow==fast:
				cycle=True
				break
			
		return cycle

node4 = Node('node4', 1)
node3 = Node('node3', 1, node4)
node2 = Node('node2', 1, node3)
node1 = Node('node1', 1, node2)

# node4.next = node2
print(node1.has_cycleHR())