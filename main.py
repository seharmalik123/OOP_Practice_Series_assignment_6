# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return(f"Name: {self.name}, Marks: {self.marks}")

# Creating an instance of Student
student1:Student = Student("Alice", 85)
student2:Student = Student("Bob", 90)
print("Student 1 Details:", student1.display())
print(student1.name, student1.marks)
print("Student 2 Details:", student2.display())


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to     manage and display the count.

class Counter:
    count = 0  # Class variable to keep track of object count

    def __init__(self):
        Counter.count += 1  # Increment the count whenever a new object is created

    @classmethod
    def display_count(cls):
        return(f"Total objects created: {cls.count}")
    
obj1:Counter = Counter()
obj2:Counter = Counter()
obj3:Counter = Counter()
print(Counter.display_count())  # Display the count of objects created


# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand= brand  # Public variable

    def start(self):  # Public method
        return(f"{self.brand} car started.")
    
car:Car = Car("Toyota")
print(car.brand)  # Accessing public variable
print(car.start())  # Calling public method


# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"  # Class variable

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # Change the class variable

bank1:Bank = Bank()
print(bank1.bank_name)  # Accessing class variable
bank2:Bank = Bank()
print(bank2.bank_name)  # Accessing class variable
Bank.change_bank_name("XYZ Bank")  # Changing the bank name using class method
print(bank1.bank_name)  # Accessing class variable after change
print(bank2.bank_name)  # Accessing class variable after change


# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b  # Static method to add two numbers
print(MathUtils.add(5, 10))  # Calling static method without creating an instance


# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).
    

class Logger:
    def __init__(self):
        print("Logger object created.")  # Constructor message

    #def __del__(self):
    #    print("Logger object destroyed.")  # Destructor message

log:Logger = Logger()  # Creating an instance of Logger
del log


# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

emp1:Employee = Employee("John Doe", 50000, "123-45-6789")
print(emp1.name)  # Accessing public variable
print(emp1._salary)  # Accessing protected variable (not recommended, but possible)
print(emp1._Employee__ssn)  # Accessing private variable (will raise an AttributeError) but can be accessed using name mangling no error wiil be raised


# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name  # Constructor to set the name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Calling the base class constructor
        self.subject = subject

teacher:Teacher = Teacher("Alice", "Mathematics")
print(f"Teacher Name: {teacher.name}, Subject: {teacher.subject}")  # Accessing attributes from both classes


# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Abstract

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width  # Implementing the abstract method


rect1:Rectangle = Rectangle(5, 10)
print(f"Area of Rectangle: {rect1.area()}")  # Calling the implemented method


# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.


class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

    def bark(self):  # Instance method
        return(f"{self.name} says Woooofff!")
    
dog:Dog = Dog("Buddy", "Golden Retriever")
print(dog.bark())  # Calling the instance method