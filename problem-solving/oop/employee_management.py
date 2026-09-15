# 🔴 Problem 04 — Employee & Manager
# Now we're getting into actual OOP concepts. 
# Create a base class called:
# Employee
# with:
# name
# salary

# and a method:
# get_details()

# Then create two subclasses:
# Developer
# Manager
# Developer

# A Developer should have an additional attribute:
# programming_language

# Its get_details() method should display:
# Name: Ahmed
# Salary: 15000
# Role: Developer
# Programming Language: Python
# Manager

# A Manager should have:

# team_size

# Its get_details() should display something like:

# Name: Mohamed
# Salary: 25000
# Role: Manager
# Team Size: 7
# Requirements

# You must use:

# Inheritance
# super()
# Method overriding

# Create at least:

# 2 Developers
# 1 Manager

# Then store them together in one list and loop through the list calling:

# employee.get_details()
# Important

# Don't write separate code like:

# developer1.get_details()
# developer2.get_details()
# manager.get_details()

# Use a single collection and demonstrate how polymorphism works.

class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative.")
        else :
            self.name = name
            self.salary = salary

    def get_details(self):
        return f"Name: {self.name}\nSalary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}\nRole: Manager\nTeam Size: {self.team_size}\n"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_details(self):
        return f"{super().get_details()}\nRole: Developer\nProgramming Language: {self.programming_language}\n"


d1 = Developer("Ahmed", 80000, "Python")
d2 = Developer("Bob", 90000, "JavaScript")
m1 = Manager("Charlie", 120000, 10)

employees = [d1, d2, m1]
for emp in employees:
    print(emp.get_details())

# Name: Ahmed
# Salary: 80000
# Role: Developer
# Programming Language: Python

# Name: Bob
# Salary: 90000
# Role: Developer
# Programming Language: JavaScript

# Name: Charlie
# Salary: 120000
# Role: Manager
# Team Size: 10
