#VERSION ONE


class Solution:
    # Write your code here
    
    def __init__(self):
        self.char_stack = []
        self.char_queue = []
    
    def pushCharacter(self, char):
        # to be implemented
        
    def enqueueCharacter(self, char):
        # to be implemented
        
    def popCharacter(self):
        # to be implemented
        
    def dequeueCharacter(self):
        # to be implemented

# VERSION TWO

class Solution:
    # Write your code here
    
    def __init__(self):
        self.char_stack = []
        self.char_queue = []
    
    def pushCharacter(self, char):
        self.char_stack.insert(0,char)
        
    def enqueueCharacter(self, char):
        self.char_queue.append(char)

    def popCharacter(self):
        self.char_stack.pop(0)
        
    def dequeueCharacter(self):
        self.char_queue.pop(0)

# VERSION THREE - WORKS

class Solution:
    # Write your code here
    
    def __init__(self):
        self.char_stack = []
        self.char_queue = []
    
    def pushCharacter(self, char):
        self.char_stack.insert(0,char)
        
    def enqueueCharacter(self, char):
        self.char_queue.append(char)

    def popCharacter(self):
        return self.char_stack.pop(0)
        
    def dequeueCharacter(self):
        return self.char_queue.pop(0)
