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



test1 = 'racecar'
test2 = 'yes'

obj=Solution()   

s = test2

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    # print(s[i])
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
# print(obj.char_stack)
# print(obj.char_queue)
# print(obj.popCharacter())
# print(obj.dequeueCharacter())
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    