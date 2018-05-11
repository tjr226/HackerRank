

def separateNumbers(s):
	''' 
	challenge: check if a string is "beautiful"
		beautiful strings are concatenated positive ints where each integer increases by one (1234, 99100101, 888889890, etc)
		rules: at least two ints in the string. no leading zeros
		length of string is 1 <= len(s) <= 32
		between 0 and 9 integers in the string
		print "YES (first int)" if true, i.e. YES 2 or YES 99
		print "NO" if false
	
	insight: build the string and compare against the original, intead of attempting to process the string or pass over the string


	'''
    if len(s) < 2:
        print("NO")
        return
    if s[0] == 0:
        print("NO")
        return
    
    maxInitialIntLength = len(s)//2
    
    currentInitialIntLength = 1
    
    
    while currentInitialIntLength <= maxInitialIntLength:
        currentString = ''
        iterInt = int(s[0:currentInitialIntLength])
        initialInt = int(s[0:currentInitialIntLength])
        
        while len(currentString) < len(s):
            currentString = currentString + str(iterInt)
            iterInt +=1
        
        # print(currentString)
        if currentString == s:
            print("YES", initialInt)
            return
        
        currentInitialIntLength += 1
    
    print("NO")
    return