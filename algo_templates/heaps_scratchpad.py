	def getIndexChildrenThatExist(self, index):
		# returns list of children if they exist

		children = []
		maxIndex = len(self.array) - 1

		leftIndex = 2*index
		rightIndex = 2*index + 1

		if leftIndex <= maxIndex:
			children.append(leftIndex)

		if rightIndex <= maxIndex:
			children.append(rightIndex)

		return children
