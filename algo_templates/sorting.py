def printInsertionSortSteps(n, arr):
    ''' 
    input: array of ints, n is length of arr
    output: print arr after each step of insertion sort
    
    lessons learned:
        - use append for ints, extend for iterables
        - you can modify the variables that are passed into a function
        - print() natively contains a newline

    big O analysis:
        - outer loop is n, inner loop is n, main loop is n^2
        - append() in python is amortized worst case 0(1) - it may be O(n) or worse if you have to extend the array
        - extend() is O(k). k is number of items in the container.
        - so, we checked append() and extend() runtimes to confirm that inner loop is O(n)
        - printing is n^2

    '''
    
    
    for i in range(1 , n):
        for j in range(0,i):
            if arr[i] < arr[j]:
                tempArr = []
                tempArr.extend(arr[:j])
                tempArr.append(arr[i])
                tempArr.extend(arr[j:i])
                tempArr.extend(arr[i+1:])
                arr = list(tempArr)
                break
        
        for a in arr:
            print(a, end=" ")
        
        print()


def insertion_sort_WHILE_implementation(l):
    # different way of doing insertion sort - relies on Loop Invariants
    # in this case, invariant is only one number being incorrectly sorted in l[:i]
    # print statements helpful to see how 
    for i in range(1, len(l)):
        # print(l)
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           
           l[j+1] = l[j]
           j -= 1
           # print(l, key)
        l[j+1] = key

    # one-liner to print ints in arr in expected "1 2 3 4 5" HackerRank formatting
    print(" ".join(map(str,l)))

