def getHeight(self,root):
    
    if (root.right == None) and (root.left == None):
        return 0        
    
    if root.right == None:
        return self.getHeight(root.left) + 1
    elif root.left == None:
        return self.getHeight(root.right) + 1 
    else:
        return max(self.getHeight(root.right),self.getHeight(root.left)) + 1