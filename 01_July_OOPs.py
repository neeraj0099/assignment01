#!/usr/bin/env python
# coding: utf-8

# 1. The primary goal of Object-Oriented Programming (OOP)?
# 
# Ans.
# The main goal of Object-Oriented Programming (OOP) in Python is to help Programmers write programms in a structured and organized way. It does this by breaking down the code into different objects that contain both data and instructions. This makes it easier to reuse code, maintain the programms, and make it work well even when it grows bigger. OOP in Python encourages dividing complex tasks into smaller, manageable parts. It also allows programmars to create new objects by borrowing characteristics from existing ones, which helps save time. Overall, OOP in Python helps create programms that is efficient, easy to understand, and can adapt to changes.
# 

# 2. What is an object in Python?
# 
# Ans.
# In Python, an object is a specific instance of a class that encapsulates both data and methods. It represents a real-world entity and provides a way to organize and manipulate information in a structured manner, promoting code reusability and maintainability.
# 
# example:-
# 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     
# #Creating Person objects
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
# 
# print (person1.name)
# print (person1.age)

# 3.What is a class in Python?
# 
# Ans.
# In Python, a class is a blueprint or template for creating objects. It defines the attributes (data) and behaviors (methods) that objects of that class will possess. Classes provide a way to structure and organize code, facilitating object creation and manipulation in an object-oriented programming.
# 
# example:-
# 
# class Person:                      #------class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     
# 
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
# 
# print (person1.name)
# print (person1.age)

# 4.What are attributes and methods in a class?
# 
# Ans.
# In a class, attributes are variables that hold data associated with each instance of the class. They represent the characteristics or properties of an object and define its state. Attributes can be accessed and modified within the class methods or by external code that interacts with the object.
# 
# In a class, methods are functions defined within the class that operate on its instances. They define the behavior or actions that objects of the class can perform. Methods can manipulate the object's attributes, interact with other objects, or provide functionality specific to the class.
# 
# example:-
# 
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         
# #Methods are functions defined within the class   
#     
#     def say_hello(self):
#         print(f"Hello, my name is {self.name}!")
#     
#     def calculate_birth_year(self):
#         current_year = 2023
#         birth_year = current_year - self.age
#         return birth_year
# 
# #Creating Person objects
# 
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)
# 
# #Accessing attributes
# 
# print(person1.name)  # Output: Alice
# print(person2.age)   # Output: 30

# 5.What is the difference between class variables and instance variables in Python?
# 
# Ans.
# In Python, class variables and instance variables are two types of variables used in classes.
# 
# Class variables are shared by all instances of a class. They are defined within the class but outside any methods. Class variables are accessed using the class name and can be used to store data that is common to all objects of the class.
# 
# Instance variables, on the other hand, are specific to each instance of a class. They are defined within the methods of the class and are unique to each object. Instance variables store data that is specific to an object and can have different values for each instance.
# 
# The main difference is that class variables are shared among all instances, while instance variables are specific to each instance of a class.
# 
# example:-
# 
# class Car:
#     # Class variable
#     manufacturer = "ABC Motors"
#     
#     def __init__(self, model):
#         # Instance variable
#         self.model = model
# 
# #Accessing class variable
# print(Car.manufacturer)  # Output: ABC Motors
# 
# #Creating instances of Car
# car1 = Car("Sedan")
# car2 = Car("SUV")
# 
# #Accessing instance variables
# print(car1.model)  # Output: Sedan
# print(car2.model)  # Output: SUV
# 
# #Modifying instance variable
# car1.model = "Hatchback"
# print(car1.model)  # Output: Hatchback
# 
# #Modifying class variable
# Car.manufacturer = "XYZ Motors"
# print(car1.manufacturer)  # Output: XYZ Motors
# print(car2.manufacturer)  # Output: XYZ Motors

# 6.What is the purpose of the self parameter in Python class methods?
# 
# Ans.
# In Python class methods, the self parameter refers to the instance of the class. It acts as a reference to the object itself, allowing access to the instance's attributes and methods within the class. By convention, the first parameter of a class method is always self. It enables the instance to interact with its own data and behavior, making it a crucial component for encapsulation and object-oriented programming in Python.
# 

# In[ ]:


'''7.For a library management system, you have to design the "Book" class with OOP
principles in mind. The “Book” class will have following attributes:
a. title: Represents the title of the book.
b. author: Represents the author(s) of the book.
c. isbn: Represents the ISBN (International Standard Book Number) of the book.
d. publication_year: Represents the year of publication of the book.
e. available_copies: Represents the number of copies available for checkout.
The class will also include the following methods:
a. check_out(self): Decrements the available copies by one if there are copies
available for checkout.
b. return_book(self): Increments the available copies by one when a book is
returned.
c. display_book_info(self): Displays the information about the book, including its
attributes and the number of available copies.'''

#Ans.

class Book:
    def __init__(self, title, author, isbn, publication_year, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.available_copies = available_copies
    
    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"A copy of '{self.title}' has been checked out.")
        else:
            print(f"Sorry, '{self.title}' is currently not available for checkout.")
    
    def return_book(self):
        self.available_copies += 1
        print(f"A copy of '{self.title}' has been returned.")
    
    def display_book_info(self):
        print("Book Information:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Available Copies: {self.available_copies}")


# Creating a book object and testing the methods
book1 = Book("the blue moon", "n.nirmal", "123456", 2000, 3)

book1.display_book_info()     # Display book information
book1.check_out()             # Checkout a copy
book1.check_out()             # Checkout a copy
book1.check_out()             # Checkout a copy
book1.check_out()             # Attempt to checkout when no copies available
book1.return_book()           # Return a copy
book1.display_book_info()     # Display updated book information


# In[30]:


''' 8. For a ticket booking system, you have to design the "Ticket" class with OOP
principles in mind. The “Ticket” class should have the following attributes:
a. ticket_id: Represents the unique identifier for the ticket.
b. event_name: Represents the name of the event.
c. event_date: Represents the date of the event.
d. venue: Represents the venue of the event.
e. seat_number: Represents the seat number associated with the ticket.
f. price: Represents the price of the ticket.
g. is_reserved: Represents the reservation status of the ticket.
The class also includes the following methods:
a. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
b. cancel_reservation(self): Cancels the reservation of the ticket if it is already
reserved.
c. display_ticket_info(self): Displays the information about the ticket, including its
attributes and reservation status.'''

#Ans.

class Ticket:
    def __init__(self, ticket_id, event_name, event_date, venue, seat_number,price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        self.is_reserved = False
    
    def reserve_ticket(self):
        if not self.is_reserved:
            self.is_reserved = True
            print(f"Ticket {self.ticket_id} has been reserved.")
        else:
            print(f"Ticket {self.ticket_id} is already reserved.")
    
    def cancel_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            print(f"Reservation for ticket {self.ticket_id} has been canceled.")
        else:
            print(f"Ticket {self.ticket_id} is not reserved.")
    
    def display_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Venue: {self.venue}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: {self.price}")
        print(f"Reservation Status: {'Reserved' if self.is_reserved else 'Not Reserved'}")

ticket1 = Ticket("AA12345", "job interviwe", "07-07-2023", "Mumbai", "A10", 5000.00)

ticket1.display_ticket_info()       # Display ticket information
ticket1.reserve_ticket()            # Reserve the ticket
ticket1.reserve_ticket()            # Attempt to reserve when already reserved
ticket1.cancel_reservation()        # Cancel the reservation
ticket1.cancel_reservation()        # Attempt to cancel when not reserved
ticket1.display_ticket_info()       # Display updated ticket information


# In[31]:


'''9. You are creating a shopping cart for an e-commerce website. Using OOP to model
the "ShoppingCart" functionality the class should contain following attributes and
methods:
a. items: Represents the list of items in the shopping cart.
The class also includes the following methods:

a. add_item(self, item): Adds an item to the shopping cart by appending it to the
list of items.
b. remove_item(self, item): Removes an item from the shopping cart if it exists in
the list.
c. view_cart(self): Displays the items currently present in the shopping cart.
d. clear_cart(self): Clears all items from the shopping cart by reassigning an
empty list to the items attribute.'''

#Ans.

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        print(f"Item '{item}' has been added to the shopping cart.")
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Item '{item}' has been removed from the shopping cart.")
        else:
            print(f"Item '{item}' does not exist in the shopping cart.")
    
    def view_cart(self):
        print("Shopping Cart:")
        if self.items:
            for item in self.items:
                print(f"- {item}")
        else:
            print("The shopping cart is empty.")
    
    def clear_cart(self):
        self.items = []
        print("The shopping cart has been cleared.")


# Creating a shopping cart object and testing the methods
cart = ShoppingCart()

cart.view_cart()            # View empty shopping cart

cart.add_item("Shirt")      # Add an item
cart.add_item("Pants")      # Add another item
cart.view_cart()            # View shopping cart

cart.remove_item("Shoes")   # Attempt to remove non-existing item
cart.remove_item("Shirt")   # Remove an item
cart.view_cart()            # View updated shopping cart

cart.clear_cart()           # Clear the shopping cart
cart.view_cart()            # View empty shopping cart


# In[ ]:


'''10. Imagine a school management system. You have to design the "Student" class using
OOP concepts.The “Student” class has the following attributes:
a. name: Represents the name of the student.
b. age: Represents the age of the student.
c. grade: Represents the grade or class of the student.
d. student_id: Represents the unique identifier for the student.
e. attendance: Represents the attendance record of the student.
The class should also include the following methods:
a. update_attendance(self, date, status): Updates the attendance record of the
student for a given date with the provided status (e.g., present or absent).
b. get_attendance(self): Returns the attendance record of the student.
c. get_average_attendance(self): Calculates and returns the average
attendance percentage of the student based on their attendance record.'''

#Ans.

class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.attendance = {}
    
    def update_attendance(self, date, status):
        self.attendance[date] = status
    
    def get_attendance(self):
        return self.attendance
    
    def get_average_attendance(self):
        total_days = len(self.attendance)
        present_days = sum(value == "present" for value in self.attendance.values())
        attendance_percentage = (present_days / total_days) * 100 if total_days > 0 else 0
        return attendance_percentage


# Creating a student object and testing the methods
student1 = Student("N Nirmal", 15, 10, "S001")

student1.update_attendance("2023-07-01", "present")
student1.update_attendance("2023-07-02", "absent")
student1.update_attendance("2023-07-03", "present")

attendance_record = student1.get_attendance()
print(attendance_record)              # Output: {'2023-07-01': 'present', '2023-07-02': 'absent', '2023-07-03': 'present'}

average_attendance = student1.get_average_attendance()
print(f"Average Attendance: {average_attendance}%")  # Output: Average Attendance: 66.66666666666666%


# In[35]:





# In[ ]:





# In[ ]:




