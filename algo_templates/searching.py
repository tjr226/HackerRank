def hackerlandRadioTransmitters(x, k):
    '''
    input: x is a list of ints, k is int
        x is houses at different numerical locations (location is NOT their indices), k is coverage distance of transmitters that can be placed on houses
        determine the minimum number of transmitters needed to cover all houses
    output: int of min number of transmitters
    '''
    x.sort()
    transmitters = 0
    
    while len(x) > 0:
        firstHouse = x.pop(0)
        newT = firstHouse
        transmitters += 1
        
        if len(x) == 0:
            break
        
        while x[0] <= firstHouse + k:
            newT = x.pop(0)
            if len(x) == 0:
                break
        
        if len(x) == 0:
            break
            
        while x[0] <= newT + k:
            x.pop(0)
            if len(x) == 0:
                break
    
    return transmitters



def icecreamParlor(m, arr):
    ''' 
    m is amount of money that two friends have
    arr is unsorted list of flavors. index is the flavor, value is the cost
    two friends will NOT get the same flavor
    you need to return the two flavors (indices) in increasing order (1 2, not 2 1)

    using a binary array gets us to O(n)

    '''

    binaryArray = [0]*((10**4) + 1)
    
    for i in arr:
        binaryArray[i] += 1
        
    # in binary array, index represents cost
    i = 0
    while i < (10**4):
        if binaryArray[i] > 0:
            binaryArray[i] -= 1
            if binaryArray[m - i] > 0:
                if i != (m - i):
                    firstIndex = 1 + arr.index(i)
                    secondIndex = 1 + arr.index(m-i)
                    return(min(firstIndex, secondIndex), max(firstIndex, secondIndex))
                else:
                    firstIndex = 1+ arr.index(i)
                    secondIndex = 1 + arr.index(m-i, arr.index(i) + 1)
                    return(min(firstIndex, secondIndex), max(firstIndex, secondIndex))
            binaryArray[i] += 1
        i += 1