class Person:
	# given by Hacker Rank
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
        

class Student(Person):
    #   this was correct
    
    def __init__(self, firstName, lastName, id, scores):
        Person.__init__(self, firstName, lastName, id)
        self.scores = scores

    def calculate(self):
        grade = sum(self.scores)/len(self.scores)
         
        if grade < 40:
            return "T"
        elif grade < 55:
            return "D"
        elif grade < 70:
            return "P"
        elif grade < 80:
            return "A"
        elif grade < 90:
            return "E"
        elif grade <= 100:
            return "O"
     