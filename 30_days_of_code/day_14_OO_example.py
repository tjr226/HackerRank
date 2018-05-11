class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()

    def computeDifference(self):
        mx = max(self.__elements)
        mn = min(self.__elements)
        return mx - mn
    


   def staircase(n):
    # Complete this function
    spaces = n
    
    while spaces > 0:
        spaces -= 1
        print(" "*spaces, #*(n-spaces))