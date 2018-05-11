
def maximum_element_in_stack():

	'''

	MAXIMUM ELEMENT OF STACK


	You have an empty sequence, and you will be given  queries. Each query is one of these three types:

	1 x  -Push the element x into the stack.
	2    -Delete the element present at the top of the stack.
	3    -Print the maximum element in the stack.
	Input Format

	The first line of input contains an integer, . The next  lines each contain an above mentioned query. (It is guaranteed that each query is valid.)

	Constraints 
	 
	 1 <= n <= 10^5
	 1 <= x <= 10^9
	 1 <= query type <= 3 

	Output Format

	For each type  query, print the maximum element in the stack on a new line.


	Key to solution - naive solution will work but will time out. need to keep track of Heap for 


	'''


	from heapq import heappush, heappop

	stack = []
	stackMaxHeap = []
	stackDeleteHeap = []

	for i in range(int(input())):
	    nums = list(map(int, input().split()))

	    if nums[0] == 1:
	        stack.append(nums[1])
	        heappush(stackMaxHeap, -nums[1])
	    elif nums[0] == 2:
	        heappush(stackDeleteHeap, -stack.pop())
	    elif nums[0] == 3:
	        if stackDeleteHeap:
	            while stackMaxHeap[0] == stackDeleteHeap[0]:
	                heappop(stackMaxHeap)
	                heappop(stackDeleteHeap)
	                if not stackDeleteHeap:
	                    break
	        print(-stackMaxHeap[0])

def isBalanced(s):

	'''
	input is a string of brackets - (), {}, []

	Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

	A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

	By this logic, we say a sequence of brackets is considered to be balanced if the following conditions are met:

	It contains no unmatched brackets.
	The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
	Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print YES on a new line; otherwise, print NO on a new line.

	'''
    expectationStack = []
    
    for i in range(0, len(s)):
        
        if s[i] == '(':
            expectationStack.append(')')
            continue
        elif s[i] == '{':
            expectationStack.append('}')
            continue
        elif s[i] == '[':
            expectationStack.append(']')
            continue
            
        if len(expectationStack) == 0:
            return 'NO'
    
        if s[i] == ')':
            x = expectationStack.pop()
            if s[i] != x:
                return 'NO'
            else:
                continue
        elif s[i] == '}':
            x = expectationStack.pop()
            if s[i] != x:
                return 'NO'
            else:
                continue
        elif s[i] == ']':
            x = expectationStack.pop()
            if s[i] != x:
                return 'NO'
            else:
                continue
    
    if len(expectationStack) > 0:
        return 'NO'

    return 'YES'

def isBalancedHackerRank(s):
	bracket_map = {'}': '{', ')': '(', ']': '['}
    stack = []
    for b in s:
        if b in bracket_map.values():  # opening
            stack.append(b)
        elif b in bracket_map.keys():  # closing
            if not stack or stack.pop() != bracket_map[b]:
                return "NO"
    if not stack:
        return "YES"
    else:
        return "NO"

# next - redo isBalanced() with dictionary approach

nextthing()


