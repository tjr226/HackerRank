class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next


    def insert(self,head,data): 
        if head is None:
            head = Node(data)
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)
        return head
    
    def removeDuplicates(self,head):
        current = head
        
        while current:
           potential = current.next
            
            # break in the case where the last one is NOT a duplicate
            if potential == None:
                break
            while potential.data == current.data:  
                
                potential = potential.next   
                # break in the case where the last IS a duplicate
                if potential == None:
                    break
                    
            current.next = potential
            current = current.next
        
        return head