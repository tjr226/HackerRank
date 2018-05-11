#! python3

	### FINISH ALL HR LINKED LISTS EXERCISES,
	### then do this: work on reverse linked lists recursive implementation
	

# single link
class Node(object):
	# single link
	def __init__(self, data=None, next=None):
		'''
		creates new node
		next is the next node
		'''
		self.data = data
		self.next = next


	def print_list(head):
		'''
		prints linked lists
		input: head node of a linked list
		output: data field of linked list
		'''

		if head.data == None:
			pass

		print(head.data)

		if head.next != None:
			print_list(head.next)

	def InsertAtEndTR(head, data):
		# my original solution, this worked
		# same as InsertAtEndHR(head, data) immediately below
		if head is None:
			head = Node(data)
			return head

		# i tried to delete this If statement, but it's needed to catch "head is none" errors for currentNode assignment
		if head.next is None:
			head.next = Node(data)
			return head

		curentNode = head.next

		while currentNode.next is not None:
			currentNode = currentNode.next
		currentNode.next = Node(data)

		return head

	def InsertAtEndHR(head, data):
		# python3 solution from HackerRank commenters
		if head is None:
			head = Node(data)
			return head
		else:
			head.next = Insert(head.next, data)
			return head

	def InsertAtHeadTR(head, data):
	    if head is None:
	        head = Node(data)
	        return head
	    
	    newHead = Node(data, head)
	    return newHead

	def InsertAtHeadHR(head, data):
		# vastly better implementation
    	return Node(data, head)

    def InsertNthTR(head, data, position):
	    '''
	    Insert Node at a specific position in a linked list
	    return back the head of the linked list    
	    
	    '''
    
	    if position == 0:
	        return Node(data, head)
	    
	    currentNode = head
	    
	    while position > 1:
	        currentNode = currentNode.next
	        position -= 1
	        
	    currentNode.next = Node(data, currentNode.next)
	    
	    return head


	def DeleteTR(head, position):
		# original solution
		if position == 0:
			return head.next

		currentNode = head

		while position > 1:
			currentNode = currentNode.next
			position -= 1

		# original code that worked:
		# nodeToDel = currentNode.next
		# currentNode.next = NodeToDel.next

		#cool modification
		currentNode.next = currentNode.next.next

		return head

	def DeleteNodeRecursive(head, position):
		#note: recursion requires o(n) space, regular requires o(1)
	    if position == 0:
	        return head.next
	    head.next = Delete(head.next, position - 1)
	    return head

	def ReversePrint(head):
		# good questions to ask:
		# how large is the linked list? use recursion and blow the stack?
		# do you have enough memory to create a copy?
		# do you want to optimize for space or time complexity?
		# should solution be non-destructive to the passed in list?
	    if head == None:
	        return
	    
	    reverseList = Node(head.data)
	    
	    while head.next != None:
	        head = head.next
	        reverseList = Node(head.data, reverseList)
	        
	    while reverseList.next != None:
	        print(reverseList.data)
	        reverseList = reverseList.next
	        
	    print(reverseList.data)

	def ReversePrintRecursive(head):
		# if loop necessary in case of head == None
		if head == None:
	        return
	    
	    # recursive solution - this goes in and prints the last one first, then prints all the rest as it "unravels"
	    if head.next == None:
	        print(head.data)
	        return
	    else:
	        ReversePrintRecursive(head.next)
	    print(head.data)

	def ReversePrintHackerRankRecursive(head):
		if head:
			ReversePrint(head.next)
			print(head.data)

	def Reverse(head):
	    
	    newHead = Node(head.data)

	    while head.next != None:
	        head = head.next
	        newHead = Node(head.data, newHead)

	    return newHead


	def CompareListsRecursiveTR(headA, headB):
		if headA.data != headB.data:
			return 0

		if (headA.next == None) != (headB.next == None):
			return 0

		if headA.next == None and headB.next == None:
			return 1

		return CompareListsRecursive(headA.next, headB.next)

	def CompareListsRegularTR(headA, headB):
	    while headA and headB:
	        if headA.data != headB.data:
	            return 0
	        headA, headB = headA.next, headB.next
	    
	    if headA or headB:
	        return 0
	    
	    return 1


	def MergeListsTimOriginal(headA, headB):
		''' 
		merges two sorted ascending linked lists into a single sorted ascending linked list
		'''
	    newList = Node()
	    
	    if headA == None and headB == None:
	        return None
	    
	    
	    if headA == None:
	        newList.data = headB.data
	        headB = headB.next
	    elif headB == None:
	        newList.data = headA.data
	        headA = headA.next
	    elif headA.data < headB.data:
	        newList.data = headA.data
	        headA = headA.next
	    else:
	        newList.data = headB.data
	        headB = headB.next
	    
	    nodeToReturn = newList
	    
	    if headA == None and headB == None:
	        return newList
	    
	    while headA or headB:
	        newList.next = Node()
	        
	        if headA == None:
	            newList.next.data = headB.data
	            headB = headB.next
	            newList = newList.next
	            continue            
	        elif headB == None:
	            newList.next.data = headA.data
	            headA = headA.next
	            newList = newList.next
	            continue
	        
	        if headA.data < headB.data:
	            newList.next.data = headA.data
	            headA = headA.next
	        else:
	            newList.next.data = headB.data
	            headB = headB.next
	        
	        newList = newList.next
	    
	    return nodeToReturn


	def MergeListsTimImproved(headA, headB):
		# saved many LOC by returning Node.next of an empty node
	    newList = Node()
	    
	    nodeToReturn = newList
	    
	    while headA or headB:
	        newList.next = Node()
	        
	        if headA == None:
	            newList.next.data = headB.data
	            headB = headB.next
	            newList = newList.next
	            continue            
	        elif headB == None:
	            newList.next.data = headA.data
	            headA = headA.next
	            newList = newList.next
	            continue
	        
	        if headA.data < headB.data:
	            newList.next.data = headA.data
	            headA = headA.next
	        else:
	            newList.next.data = headB.data
	            headB = headB.next
	        
	        newList = newList.next
	    
	    return nodeToReturn.next


	def MergeListsRecursiveTR(headA, headB):
	    newNode = Node()
	    
	    if headA or headB:
	    	# you need the == None checks to avoid throwing errors
	        if headA == None:
	            newNode.data = headB.data
	            headB = headB.next
	        elif headB == None:
	            newNode.data = headA.data
	            headA = headA.next
	        elif headA.data < headB.data:
	            newNode.data = headA.data
	            headA = headA.next
	        else:
	            newNode.data = headB.data
	            headB = headB.next
	            
	    if headA or headB:
	        newNode.next = MergeListsRecursive(headA, headB)
	        
	    return newNode

	def MergeListsRecursiveHR(headA, headB):
	    newNode = Node()
	    
	    
	    if headA is None:
	        return headB
	    elif headB is None:
	        return headA
	    
	    if headA.data < headB.data:
	        newNode.data = headA.data 
	        headA = headA.next
	    else:
	        newNode.data = headB.data
	        headB = headB.next
	    
	    if headA or headB:
	        newNode.next = MergeLists(headA, headB)
	        
	    return newNode

	def GetNodeTR(head, position):
	    ''' 
	    get node data of the Nth Node from the end
	    input: head (can be None for empty list), position indexed from tail (if at end of list, position = 0)
	    output: data from node at that position
	    '''
	    # this solution passes through the list to find length
	    # modifies position to be indexed at head
	    # passes through list again to find data
	    lengthFinder = head
	    length = 1
	    
	    while lengthFinder.next is not None:
	        length += 1
	        lengthFinder = lengthFinder.next
	        
	    newPosition = length - position - 1
	    dataFinder = head
	    
	    while newPosition > 0:
	        dataFinder = dataFinder.next
	        newPosition -= 1
	        
	    return dataFinder.data

	def GetNodeHR(head, position):
	    ''' 
	    get node data of the Nth Node from the end
	    input: head (can be None for empty list), position indexed from tail (if at end of list, position = 0)
	    output: data from node at that position
	    '''
	    # this solution has two pointers - one to find the end of the list
	    # second pointer is (position) nodes behind to grab the data
	    front = head
	    back = head
	    
	    while position > 0:
	        front = front.next
	        position -= 1
	        
	    while front.next is not None:
	        front = front.next
	        back = back.next
	        
	    return back.data

	def RemoveDuplicatesTjrRecursive(head):
		if head.next is None:
		    return head

		if head.next.next is None:
		    if head.data == head.next.data:
		        head.next = None
		    return head   

		# old version:		    
		# if head.data == head.next.data:
		#     head.next = head.next.next
		#     head = RemoveDuplicates(head)

		# if head.next is not None:
		#     head.next = RemoveDuplicates(head.next)

		# better:

		if head.data == head.next.data:
        	head.next = head.next.next
        	return RemoveDuplicates(head)

    	head.next = RemoveDuplicates(head.next)

		return head

	def RemoveDuplicatesHR(head):
	    if head:
	        node = head
	        while node.next:
	            if node.data == node.next.data:
	                if node.next.next:
	                    node.next = node.next.next      
	                else:
	                    node.next = None
	            else:
	                node = node.next
	        
	    return head

	def has_cycle(head):
	    node_list = []
	    
	    while head.next:
	        
	        node_list.append(head)
	        head = head.next
	        if head in node_list:
	            return 1
	    
	    return 0

	def has_cycle(head):
		# uses "tortoise and hare" solution
	    if not head:
	        return 0
	    
	    fast = head
	    slow = head
	    
	    while fast.next and fast.next.next:
	        fast = fast.next.next
	        slow = slow.next
	        if fast == slow:
	            return 1
	        
	    return 0


	def FindMergeNodeTR(headA, headB):
		# Quadratic, O(n^2)
	    while headA:
	        otherNode = headB
	        while otherNode:
	            if otherNode == headA:
	                return headA.data
	            otherNode = otherNode.next
	        headA = headA.next

	def FindMergeNodeHR(headA, headB):
		# linear time
		# works because both lists have approximate structure of (a + x), (b + x)
		# so you get to the merge point at either (A == B) steps, or (a + b + x) steps
		
	    trackerA = headA
	    trackerB = headB
	    
	    while trackerA != trackerB:
	        if trackerA.next is None:
	            trackerA = headB
	        else:
	            trackerA = trackerA.next
	        
	        if trackerB.next is None:
	            trackerB = headA
	        else:
	            trackerB = trackerB.next
	            
	    return trackerA.data



