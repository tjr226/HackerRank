class Node(object):

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	# BIG ASSUMPTION: These are minimum binary trees, AKA binary search trees

	def preOrder(root):
		# python2 implementation
		# prints all data points in nodes starting at top of tree
		print root.data,
		if root.left:
			preOrder(root.left)
		if root.right:
			preOrder(root.right)

	def postOrder(root):
		#python2 implementation
		# prints all data points in nodes starting at bottom of tree
		if root.left:
			postOrder(root.left)
		if root.right:
			postOrder(root.right)
		print root.data,

	def inOrder(root):
		# python 2 implementation
		# prints all nodes in order of their value
	    
	    if root.left:
	        inOrder(root.left)
	    print root.data,
	    if root.right:
	        inOrder(root.right)

	def heightTR(root):
		# returns height of tree
	    
	    if not root.left and not root.right:
	        return 0
	    
	    leftHeight, rightHeight = 0, 0
	    if root.left:
	        leftHeight = 1 + heightTR(root.left)
	    if root.right:
	        rightHeight = 1 + heightTR(root.right)
	    return max(leftHeight, rightHeight)
	
	def heightHR(root):
	    # returns height of tree

	    if root is None:
	        return -1
	    
	    return max(1 + heightHR(root.left), 1 + heightHR(root.right))


	def topViewTR(root):
		# python2 solution
		# this is my solution, I don't see anything better in the forums
		# the way they structured this question - print the "outside" nodes from left to right, ignore "inside" nodes that eventually extend past outside
		# other people will want to see "actual" top down, in case inside nodes extend past outside

	    topDownList = []
	        
	    if root.left:
	        leftSide = root.left
	        while leftSide:
	            topDownList.insert(0, leftSide.data)
	            leftSide = leftSide.left
	    
	    # print(topDownList)
	    while root:
	        topDownList.append(root.data)
	        root = root.right
	        
	    for x in topDownList:
	        print x,

	def levelOrderTR(root):
		# breadth first search

	    queue = [root]
	    
	    while len(queue) > 0:
	        x = queue.pop(0)
	        print x.data,
	        a, b = x.left, x.right
	        if a:
	            queue.append(a)
	        if b:
	            queue.append(b)

	def insertTR(r,val):
		# insert values into min binary search tree
	    if r is None:
	        return Node(val)
	    
	    if r.data >= val:
	        if r.left:
	            r.left = insertTR(r.left, val)
	        else:
	            r.left = Node(val)
	            
	    elif r.data < val:
	        if r.right:
	            r.right = insertTR(r.right, val)
	        else:
	            r.right = Node(val)
	    
	    return r

	def insertHR(r,val):
		# cleaned up version, idea came from HR forums
		# once you add "r is None" check at beginning of function, you don't need to redo later on
	    if r is None:
	        return Node(val)
	    
	    if r.data >= val:
	        r.left = insertHR(r.left, val)
	    elif r.data < val:
	        r.right = insertHR(r.right, val)
	    
	    return r

	def decodeHuffTR(root , s):
	    decoded = ''
	    while len(s) > 0:
	        tempTree = root
	        while tempTree.left:
	            nextChar = s[0]
	            if len(s) > 1:
	                s = s[1:]
	            else: 
	                s = ''
	            if int(nextChar) == 1:
	                tempTree = tempTree.right
	            elif int(nextChar) == 0:
	                tempTree = tempTree.left
	                
	        decoded = decoded + tempTree.data
	    print decoded

	def decodeHuffRecursive(root , s):
		# recursive version but not that much cooler
	    
	    tempTree = root
	    while tempTree.left:
	        nextChar = s[0]
	        if len(s) > 1:
	            s = s[1:]
	        else: 
	            s = ''
	        if int(nextChar) == 1:
	            tempTree = tempTree.right
	        elif int(nextChar) == 0:
	            tempTree = tempTree.left
	            
	    sys.stdout.write(tempTree.data)
	    if len(s) > 0:
	        decodeHuffRecursive(root, s)


# next two functions are used to solve "Lowest Common Ancestor" problem
# re-wrote level Order Traversal for practice
	def levelOrderTraversal(root):
	    ''' 
	    input: root of a binary tree
	    output: list that has all nodes in tree in level order traversal (breadth first)
	    '''
	    stack = []
	    stack.append(root)
	    
	    returnList = []
	    
	    while len(stack) > 0:
	        tempNode = stack.pop(0)
	        returnList.append(tempNode)
	        
	        if tempNode.left:
	            stack.append(tempNode.left)
	        if tempNode.right:
	            stack.append(tempNode.right)
	    
	    return returnList
	    
	    

	def lca(root , v1 , v2):
		'''
		input: one root node of a binary tree. two integer values (NOT two more nodes)
		assumption: any root of binary tree has both integer values in some nodes
		assumption: v1 != v2
		output: lowest root node that includes both values in it's decendents - the root can have one of the values
		'''
	    nodeList = levelOrderTraversal(root)
	    lowestCommonAncestor = root
	    for node in nodeList:
	        newNodeList = levelOrderTraversal(node)
	        newDataList = [x.data for x in newNodeList]
	        if v1 in newDataList and v2 in newDataList:
	            lowestCommonAncestor = node
	        
	    return lowestCommonAncestor