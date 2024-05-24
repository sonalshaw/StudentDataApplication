class Student:

    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getIdNumber(self):
        return self.idNumber