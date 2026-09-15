# 🟢 Problem 01 — Student Profile
# Create a class called Student that represents a student.

# The class should have:
# name
# age
# major

# Add a method called introduce() that prints the student's information in a readable format.

# Example
# student = Student("Ahmed", 20, "Computer Science")

# student.introduce()
# Expected Output
# Name: Ahmed
# Age: 20
# Major: Computer Science
# Requirements
# Use a constructor (__init__).
# Store the information as instance attributes.
# Create and use at least two different Student objects.

class Student :
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Name : {self.name}\nAge : {self.age}\nMajor : {self.major}"
    
s1 = Student("John Doe", 20, "Business Administration")

s1.age = 22
s2 = Student("Ahmed Abdullatif", 20, "Computer Science")

print(s1.introduce())
print(s2.introduce())