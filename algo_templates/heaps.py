class MinHeap(object):
	# invariant: only one value out of place at any one time
	# this heap implementation is equipped to handle ints and floats
	# heap starts at index 1 for ease of coding, value at index 0 is None

	# Someday/maybe bonus functions:
	# limit inputs to ints and floats
	# test invariants for siftUp and siftDown to make sure they aren't run at incorrect times

	def __init__(self):
		self.array = [None]

	def findMin(self):
		if self.array[1]:
			return self.array[1]
		else:
			return None

	def printHeap(self):
		print(self.array)


	def insert(self, value):
		# inserts one value at a time
		# assumes that inputs are integers
		# rep invariant - only one value is out of place at any one time
		# adds value to end of array, then sifts it up if necessary

		self.array.append(value)
		self.siftUp()

	def siftUp(self):
		# up heapify - bubble up
		# assumes that ONE element is out of place - the last 

		if len(self.array) <= 2:
			return		

		currentIndex = len(self.array) - 1
		parentIndex = currentIndex // 2

		while self.array[parentIndex] > self.array[currentIndex]:
			self.array[parentIndex], self.array[currentIndex] = self.array[currentIndex], self.array[parentIndex]
			currentIndex = parentIndex
			parentIndex = currentIndex // 2

			if currentIndex == 1:
				break

	def deleteMin(self):
		self.array[1] = self.array.pop()
		self.siftDown()

	def extractMin(self):
		min = self.array[1]
		self.deleteMin()
		return min

	def siftDown(self):
		# down heapify - bubble down
		# assumes that ONE element is out of place - the first

		currentIndex = 1
		maxIndex = len(self.array) - 1

		while self.indexChildrenAreLess(currentIndex) == True:

			# handle case where we only have a left child
			if currentIndex*2 == maxIndex:
				self.array[currentIndex], self.array[maxIndex] = self.array[maxIndex], self.array[currentIndex]
				break

			# determines left and right child values
			leftChildValue = self.array[currentIndex*2]
			rightChildValue = self.array[currentIndex*2 + 1]

			# picks whether to switch with left or right
			if leftChildValue < rightChildValue:
				indexToSwitch = currentIndex*2
			else:
				indexToSwitch = (currentIndex*2) + 1

			#switches values
			self.array[currentIndex], self.array[indexToSwitch] = self.array[indexToSwitch], self.array[currentIndex]

			currentIndex = indexToSwitch

	def indexChildrenAreLess(self, index):
		# used in siftDown function to check whether to siftDown again
		# input: index in heap array
		# output: true if either the left or right value is less than the current index value
		# output: false if both left and right values are greater than the index value, or if there are no children

		indexValue = self.array[index]

		maxIndex = len(self.array) - 1
		maxIndexValue = self.array[maxIndex]

		# print("index value is", indexValue)
		if index*2 > maxIndex:
			return False

		if index*2 == maxIndex:
			if indexValue > maxIndexValue:
				return True
			return False

		leftChildValue = self.array[index*2]
		rightChildValue = self.array[index*2 + 1]

		if indexValue > leftChildValue or indexValue > rightChildValue:
			return True

		return False



	def minHeapTest(self):
		# returns True of min heap property is met
		# returns False if min heap property is not met

		for i in range(1, len(self.array)-1):
			iChildrenIndices = self.getIndexChildrenThatExist(i)

			for j in iChildrenIndices:
				if self.array[i] > self.array[j]:
					return False

		return True

	def getIndexChildrenThatExist(self, index):
		# returns list of children if they exist
		# used in minHeapTest()

		children = []
		maxIndex = len(self.array) - 1

		leftIndex = 2*index
		rightIndex = 2*index + 1

		if leftIndex <= maxIndex:
			children.append(leftIndex)

		if rightIndex <= maxIndex:
			children.append(rightIndex)

		return children


def main():
	newHeap = MinHeap()

	newHeap.insert(20)
	print(newHeap)
	newHeap.printHeap()
	newHeap.insert(30)

	for x in range(9, 4, -1):
		newHeap.insert(x)

	moreNums = [66, 33, 12, 4, 3]

	for x in moreNums:
		newHeap.insert(x)

	newHeap.printHeap()

	print("minHeapTest", newHeap.minHeapTest())
	newHeap.array[1] = 11

	newHeap.printHeap()
	newHeap.siftDown()
	newHeap.printHeap()

	print("minHeapTest", newHeap.minHeapTest())
	newHeap.deleteMin()
	newHeap.printHeap()
	print("minHeapTest", newHeap.minHeapTest())
	print(newHeap.extractMin())
	newHeap.printHeap()

	for x in range(23, 27):
		newHeap.insert(x)

	print("minHeapTest", newHeap.minHeapTest())
	newHeap.deleteMin()

	newHeap.printHeap()

	print("minHeapTest", newHeap.minHeapTest())

main()