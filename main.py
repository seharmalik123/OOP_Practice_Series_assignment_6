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


# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable
    def __init__(self):
        Book.total_books += 1  # Incrementing the class variable

    @classmethod
    def increment_book_count(cls):
        return (f"The count of total books is {cls.total_books}")  # Class method to return the count
    
book1:Book = Book()
book2:Book = Book()
book3:Book = Book()
book4:Book = Book()
book5:Book = Book()
book6:Book = Book()
book7:Book = Book()
book8:Book = Book()
book9:Book = Book()
book10:Book = Book()
print(Book.increment_book_count())  # Calling the class method to get the count of books created


# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32  # Static method to convert Celsius to Fahrenheit
    
print(f"Temperature in Fahrenheit is: {TemperatureConverter.celsius_to_fahrenheit(25)}")  # Calling the static method to convert temperature


# 13.Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car clas

class Engine:
    def start_engine(self):
        return "Engine started."  # Method to start the engine
    
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start_engine()  # Accessing Engine's method via Car
    
car_engine:Engine = Engine()  # Creating an Engine object
my_car:Car = Car(car_engine)  # Creating a Car object with Engine
print(my_car.start_car())  # Calling the method to start the car


# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it. 

class Department:
    def __init__(self, department_name):
        self.department_name = department_name  # Department name

    def get_department_name(self):
        return self.department_name
    
class Employee:
    def __init__(self, employee_name, department):
        self.employee_name = employee_name
        self.department = department

        
department:Department = Department("HR")
employee1:Employee = Employee("john Doe", department)
print(f"Employee {employee1. employee_name} works in {employee1.department.get_department_name()} department.")


# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        return ("Class A show() method")  # Method in class A
    
class B(A):
    def show(self):
        return ("Class B show() method")  # Overriding method in class B
    
class C(A):
    def show(self):
        return ("Class C show() method")  # Overriding method in class C
    
class D(B, C):
    def show(self):
        return ("Class D show() method")  # Overriding method in class D
    
obj1:D = D()  # Creating an object of class D
print(obj1.show())  # Calling the show() method of class D


# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().
        
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)  # Calling the original function
    return wrapper

@log_function_call
def say_hello():
    return "Hello, World!"

print(say_hello())  # Calling the decorated function


# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"  # Method to be added
    
    cls.greet = greet  # Adding the method to the class
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # Constructor to set the name


person:Person = Person("Alice")  # Creating an instance of Person
#print(person.name())  # Calling the added method
print(person.greet())  # Calling the added method


# 18. Property Decorators
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter method

    @price.setter
    def price(self, value):
        self._price = value # Setter method

    @price.deleter
    def price(self):
        del self._price  # Deleter method

product1:Product = Product(1000)  # Creating an instance of Product
print(product1.price)  # Accessing the price using getter
product1.price = 1500  # Updating the price using setter
print(product1.price)  # Accessing the updated price using getter
del product1.price  # Deleting the price using deleter
print('product1 price deleted successfully!') 


# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Setting the factor

    def __call__(self, x):
        return x * self.factor  # Multiplying the input by the factor
    
factor1:Multiplier = Multiplier(5)  # Creating an instance of Multiplier
print(factor1(10))  # Calling the object like a function
print(callable(factor1))  # Checking if the object is callable


# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    pass  # Custom exception class

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")  # Raising the custom exception
    else:
        return "Age is valid."
    
try:
    result = check_age(15)  # Testing the function with an invalid age
    print(result)  # This line will not be executed if the exception is raised
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")  # Handling the custom exception

try:
    result = check_age(19)  # Testing the function with a valid age
    print(result)  # This line will be executed if the age is valid
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")


# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.


class Countdown:
    def __init__(self, start):
        self.Current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.Current <= 0:
            raise StopIteration
        else:
            current = self.Current
            self.Current -= 1
            return current
        
countdown:Countdown = Countdown(5)  # Creating an instance of Countdown
print("Countdown:")
for number in countdown:  # Iterating through the Countdown object
    print(number)  # Printing the countdown numbers

