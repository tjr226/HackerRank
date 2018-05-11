 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
	   self.data = data
	   self.next = next_node
	   self.prev = prev_node


	def SortedInsert(head, data):
		''' 
		insert a node into a sorted ascending doubly linked list
		go to the node that will be one AFTER where we want to insert
		(might have been easier to stop one earlier)
		'''
	  
		# handle null case
		if head is None:
			return Node(data)
		
		# handle case where data needs to be inserted at beginning
		if head.data > data:
			newHead = Node(data, head)
			head.prev = newHead
			return newHead
		
		# only triggered if one node and head.data <= data
		if head.next is None:
			newNode = Node(data, None, head)
			head.next = newNode
			return head
		
		# handle cases of lists longer than one node 
		iterNode = head
		
		# check for iterNode.next is to prevent errors, NOT to determine insertion place
		while iterNode.data < data and iterNode.next:
			iterNode = iterNode.next
			
		# handling insertion at end of list, in case where While loop was stopped because of iterNode.next = None    
		if iterNode.data < data:
			iterNode.next = Node(data, None, iterNode)
			return head
		
		# handling insertion in middle of list, OR where we hit end of list but data < iterNode.data
		newNode = Node(data, iterNode, iterNode.prev)
		iterNode.prev.next = newNode
		iterNode.prev = newNode
		return head


	def SortedInsertRecursive(head, data):
	    ''' 
	    insert a node into a sorted ascending doubly linked list
	    '''
	    # recursively look through all next two nodes, and insert between them if correct
	    # also handle all edge cases

	    if head is None:
	        return Node(data)
	    
	    if head.data > data:
	        newHead = Node(data, head)
	        head.prev = newHead
	        return newHead
	    
	    if head.next is None:
	        head.next = Node(data, None, head)
	        return head
	    
	    if head.data <= data and data <= head.next.data:
	        newNode = Node(data, head.next, head)
	        head.next.prev = newNode
	        head.next = newNode
	        return head
	    
	    head.next = SortedInsertRecursive(head.next, data)
	    
	    return head
        
    def SortedInsertHackerRankRecursive(head, data):
	    node = Node(data,None,None)
	    if (head == None):
	        return node
	    elif (data < head.data):
	        node.next = head
	        head.prev = node
	        return node
	    else:
	        node = SortedInsert(head.next, data)
	        head.next = node 
	        node.prev = head
	        return head

	def SortedInsertHackerRankRecursiveTwo(head, data):
	    if head.data >= data:
	        return Node(data, head, head.prev)
	    elif head.next == None:
	        head.next = Node(data, None, head)
	        return head
	    else:
	        head.next = SortedInsert(head.next, data)
	        return head

	def ReverseDoublyLinkedListTR(head):
		# edited by myself, this is second version
	    if head is None:
	        return head

	    while head.next:
	        head.next, head.prev = head.prev, head.next
	        head = head.prev  
	    head.next, head.prev = head.prev, head.next
	    return head	

	def ReverseDoublyLinkedListRecursiveTR(head):
	    if head is None:
	        return head
	    
	    head.next, head.prev = head.prev, head.next
	    
	    if head.prev:
	        return ReverseDoublyLinkedListRecursiveTR(head.prev)
	    else:
	        return head