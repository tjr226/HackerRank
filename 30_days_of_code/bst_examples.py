import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
	#hacker rank code to build binary search tree
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root


	def getHeight(self,root):
	    
	    if (root.right == None) and (root.left == None):
	        return 0        
	    
	    if root.right == None:
	        return self.getHeight(root.left) + 1
	    elif root.left == None:
	        return self.getHeight(root.right) + 1 
	    else:
	        return max(self.getHeight(root.right),self.getHeight(root.left)) + 1



	# breadth first print - print the root, then each layer left to right
	def levelOrder(self,root):
	        queue = []
	        
	        if root != None:
	            queue.append(root)
	            
	        while len(queue) > 0:
	            to_process = queue.pop(0)
	            
	            print(to_process.data, end=" ")
	        
	            if to_process.left != None:
	                queue.append(to_process.left)
	            
	            if to_process.right != None:
	                queue.append(to_process.right)