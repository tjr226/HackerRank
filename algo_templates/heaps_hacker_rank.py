from heapq import heappush, heapify, heappop


def qheap1():
    '''
    implementation of Hacker Rank challenge QHEAP1 by dcod5
    input: first line is number of queries q
        each next line contains queries of type "1 v", "2 v", "3"
        v is value. only distinct elements will be in the heap.
        queries:
        1 v = insert value v into heap
        2 v = delete value v from heap
        3 = print minimum of heap

    output: none from this function, but print the min of the heap if query is 3

    challenge: deleting value v from heap is not free because it may not be the root

    ideas:
    solution 1: heapify after each delete, this was correct but timed out
    solution 2: only heapify if the root was affected, thus changing what we would have to print next time.
        commenters think this works in some languages, but my implementation was buggy and not clear
    solution 3 (simple, is fast enough, this is what I used):
        maintain two heaps, heap of inserted values and heap of values to be deleted.
        query 1, insert into values heap. query 2, insert into deletion heap.
        query 3- check if the root of the values heap should be deleted. delete if necessary from both value and delete heaps.
            print root of values heap after confirming it's not in the deletion heap

    '''


    q = int(input().strip())

    valheap = []
    delheap = []

    for i in range(q):
        
        lst = list(map(int, input().strip().split(' ')))
        
        if i == 0:
            # sets the root to be the first value on the first query
            root = lst[1]
        
        if lst[0] == 1:
            heappush(valheap, lst[1])
        elif lst[0] == 2:
            heappush(delheap, lst[1])
        elif lst[0] == 3:
            
            while delheap and valheap:
                if valheap[0] == delheap[0]:
                    heappop(valheap)
                    heappop(delheap)
                    continue
                    
                if valheap[0] != delheap[0]:
                    break
            
            print(valheap[0])

def cookies(k, A):
    ''' 
    input: int k, list of ints A
    requirement: all A must >= k
    if any A not >= k, combine smallest element of A (a) and second smallest element of A (b) into new element c = a + 2*b

    output: return -1 if you cannot fulfill the requirement combining ints in A to make sure they're all >= k
    output: return count of combinations you had to do to make all elements >= k if you can fulfill the requirement
    '''

    if len(A) == 0:
        return -1
    
    if len(A) == 1:
        if A[0] < k:
            return -1
        
    operations = 0
    heapify(A)
    
    while A[0] < k:

        a = heappop(A)
        b = heappop(A)
        heappush(A, a + 2*b)
        operations += 1
   
        if len(A) == 1:
            if A[0] < k:
                return -1
            else:
                break
        
    return operations


# running median problem
# given a list of ints, return a running list of the median as you add each one

# helper functions

# mistake and how I found it
# if i was between roots, and the total length was odd
# i was comparing i to the maxHeap root
# but we want it to be less than or equal to the minHeap root
# this is correct

def totalLengthEven(minH, maxH):
    totalLength = len(minH) + len(maxH)
    if totalLength % 2 == 0:
        return True
    else:
        return False
    
def median(minH, maxH):
    if totalLengthEven(minH, maxH):
        return (minH[0] + -maxH[0])/2
    else:
        return minH[0]
    
def runningMedian(a):
    # input: list of ints a
    # output: list of medians
    minH, maxH, medianList = [], [], []
    
    for i in a:
        # print("i is", i, "is totalLengthEven?", totalLengthEven(minH, maxH))
        if len(minH) == 0:
            medianList.append(i)
            heappush(minH, i)
            continue
        
        if len(maxH) == 0:
            tempList = [i, heappop(minH)]
            heappush(minH, max(tempList))
            heappush(maxH, -min(tempList))
            medianList.append(median(minH, maxH))
            continue
        
        if totalLengthEven(minH, maxH):
            if i >= -maxH[0]:
                heappush(minH, i)
            else:
                heappush(minH, -heappop(maxH))
                heappush(maxH, -i)
        else:
            if i <= minH[0]:
                heappush(maxH, -i)
            else:
                heappush(maxH, -heappop(minH))
                heappush(minH, i)
        
        medianList.append(median(minH, maxH))
        
        
        # print("maxHeap root is", -maxH[0], "minHeap root is", minH[0])
    
    return medianList


# new problem - minimize average waiting time of people who order pizzas
# input - a list of lists, each list is of form [arrival time, cook time]
# goal is to minimize average waiting time
# to do this, you want to always cook the pizza with SHORTEST cook time available
# two insights:
#    heapq can accept tuples where the first value is the sorting value, i.e. (1, 4) - arrival time is 1, cook time is 4
#    reverse minheap key values - first create minHeap of customers by arrival time. then reverse the tuple and sort them by cook time

def minimumAverage(customers):

    totalCustomers = len(customers)
    totalWaitTime = 0
    time = 0
    
    custH, readyH = [], []
    
    for c in customers:
        heappush(custH, (c[0], c[1]))
    
    while custH or readyH:
        if len(custH) > 0:
            while custH[0][0] <= time:
                x = heappop(custH)
                y = (x[1], x[0])
                heappush(readyH, y)
                
                if len(custH) == 0:
                    break
        
        if len(readyH) > 0:
            nextPizza = heappop(readyH)
            
            totalWaitTime += nextPizza[0] + (time - nextPizza[1])
            time += nextPizza[0]
        else:
            time = custH[0][0]
                
    
    return totalWaitTime//totalCustomers