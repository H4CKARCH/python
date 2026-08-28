class Person:

    def __init__(self, name, age):

        self.name = name

        self.age = age

    def displayData(self):

        print("In parent class displayData method")

        print("Name:", self.name)

        print("Age:", self.age)

        print("\n")


class Employee(Person):

    def __init__(self, name, age, id):

        # Calling constructor of super class
        super().__init__(name, age)


        self.empId = id


    def displayData(self):

        print("In child class displayData method")

        print("Name:", self.name)

        print("Age:", self.age)

        print("Employee ID:", self.empId)


# Person class object
person = Person("Creestu Achari", 20)

person.displayData()


# Employee class object
emp = Employee("Creestu Achari", 20, "25KP1A0479")

emp.displayData()
