### THIS WORKS BUT IS TOO SLOW
# I was proud of the insight to limit the inner loop by starting bitwise comparisons at 2^x - 1, but that wasn't enough

# next steps... maybe switch from For loops to While loops?
# work done, but it did not solve the calculation from timing out (still correct though)

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    temp_max = 0
    real_min = k
    
    for i in range(1,n):
        maxTwoExponent = 2
        while maxTwoExponent < n/2:
            maxTwoExponent *= 2
        # print(maxTwoExponent)
        for j in range(max(i+1, maxTwoExponent - 1), n + 1):
            # print(i,j)
            bitwise = i & j
            if (bitwise > temp_max) and (bitwise < k):
                temp_max = bitwise
    
    print(temp_max)


### next version

for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    
    temp_max = 0
    real_min = k
    maxTwoExponent = 2
    while maxTwoExponent < n/2:
            maxTwoExponent *= 2
    
    i = 1
    while i < n:
        
        
        # print("i is", i)
        # print("maxTwoExponent is", maxTwoExponent)
        j = i + 1
        while j < min(2*k, n + 1):
            
            # print(i,j)
            # print(i,j)
            bitwise = i & j
            
            if (bitwise > temp_max) and (bitwise < k):
                temp_max = bitwise
                max_bitwise_pair = (i, j)
            j += 1
                
        i += 1
    
    print(temp_max)
    # print(max_bitwise_pair)
