# self is a pointer in python that point the object or instance of a class
# see the example below


class Employee:
    def printdetails(self):
        return f"my name is: {self.name}\n my sallary is: {self.sallary}\n my role is: {self.role}"
ismail=Employee()
raheem=Employee()

ismail.name="ismail"
ismail.sallary="2000"
ismail.role="student"

raheem.name = "raheem"
raheem.sallary = "2000"
raheem.role = "instructor"

print(ismail.printdetails())
print(raheem.printdetails())



