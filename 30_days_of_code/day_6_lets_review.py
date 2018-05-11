
N = input()
N = int(N)

phone_book = {}

for x in range(N):
	inputString = input()
	# print(inputString)
	splitList = inputString.split(" ")
	# print(splitList)
	name = splitList[0]
	number = splitList[1]
	
	phone_book[name] = number

while 1 == 1:
	inputQuery = input()

	if inputQuery in phone_book:
		print(inputQuery, "=", phone_book[inputQuery],sep="")
	else:
		print("Not found")