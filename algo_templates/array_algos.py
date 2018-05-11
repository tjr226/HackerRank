def minimumAbsoluteDifference(arr):
	# returns the lowest absolute difference between two integers in an array
	# mistakes - not paying attention and returning maximum absolute difference
	# other challenge - starting with nested loops, O(n^2). timed out
	# needed to sort array first then do one pass, O(n lg n + n), that worked
    minDiff = float('Inf')
    
    arr.sort()
    
    for i in range(0, len(arr)-1):
        newDiff = abs(arr[i] - arr[i + 1])
        
        if newDiff < minDiff:
            minDiff = newDiff
            
    return minDiff