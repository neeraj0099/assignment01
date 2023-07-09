#!/usr/bin/env python
# coding: utf-8

# 1. Explain what inheritance is in object-oriented programming and why it is used.
# 
# Ans.
# In object-oriented programming (OOP), inheritance is a mechanism that allows a class to inherit or acquire the properties, methods, and behavior of another class. The class that is being inherited from is called the "parent class" or "superclass," while the class that inherits from it is called the "child class" or "subclass."
# Inheritance is used in OOP for several reasons: Code Reusability, Modularity and Organization, Polymorphism, Specialization and Generalization, Code Extensibility.
# 
# 

# 2. Discuss the concept of single inheritance and multiple inheritance, highlighting their differences and advantages.
# 
# Ans.
# Single Inheritance:
# Single inheritance allows a class to inherit from a single parent class or superclass.
# The child class inherits all the attributes and methods from the parent class and can extend or override them as needed.
# Example: Class ChildClass inherits from a single parent class ParentClass.
# Advantages of Single Inheritance: Simplicity, Reduced Complexity, Clearer Design.
# 
# Multiple Inheritance:
# Multiple inheritance allows a class to inherit from multiple parent classes or superclasses.
# The child class inherits attributes and methods from all the parent classes simultaneously.
# Example: Class ChildClass inherits from multiple parent classes ParentClass1, ParentClass2, and ParentClass3.
# Advantages of Multiple Inheritance: Code Reusability, Flexibility, Expressive Modeling.

# 3. Explain the terms "base class" and "derived class" in the context of inheritance.
# 
# Ans.
# Base Class (Superclass): A base class, also known as a superclass or parent class, is the class from which other classes inherit. It serves as the foundation or source of attributes, methods, and behaviors that can be inherited by other classes.
# 
# Derived Class (Subclass): A derived class, also known as a subclass or child class, is a class that inherits properties and behaviors from a base class. The derived class extends or specializes the base class by adding its own attributes and methods or by overriding the inherited ones.

# 4. What is the significance of the "protected" access modifier in inheritance? How does it differ from "private" and "public" modifiers?
# 
# Ans.
# Private Access Modifier:
# Private members are accessible only within the class that defines them.
# They are not visible or accessible to subclasses or external code.
# Private members are typically used to encapsulate implementation details and internal workings of a class, hiding them from other classes.
# 
# Protected Access Modifier:
# Protected members are accessible within the class that defines them, as well as by subclasses derived from that class.
# They are not directly accessible to code outside the class hierarchy (i.e., external code or unrelated classes).
# Protected members provide a level of encapsulation, allowing subclasses to access and utilize them while preventing direct access from external sources.
# Protected members facilitate code reuse and specialization within the inheritance hierarchy.
# 
# Public Access Modifier:
# Public members are accessible from anywhere, including within the class, by subclasses, and by external code.
# They have no restrictions on accessibility and can be accessed by any part of the codebase.
# Public members represent the interface or contract of a class, exposing its functionalities to other classes or modules.
# 

# 5. What is the purpose of the "super" keyword in inheritance? Provide an example.
# 
# Ans.
# In inheritance, the super keyword is used to refer to the parent class or superclass. It allows access to the methods and attributes of the superclass, enabling the subclass to extend or override them. The super keyword is primarily used to invoke the superclass's methods or constructors from the subclass, providing a way to reuse and build upon the existing functionality.
# 
# Example:-
# 
# class Animal:
#     def __init__(self, name):
#         self.name = name
# 
#     def make_sound(self):
#         print("Animal makes a sound")
# 
# 
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
# 
#     def make_sound(self):
#         super().make_sound()
#         print("Dog barks")
# 
# 
# #Create an instance of Dog
# my_dog = Dog("Buddy", "Labrador")
# 
# #Access attributes from the superclass
# print(my_dog.name)    # Output: Buddy
# 
# #Invoke methods from the superclass
# my_dog.make_sound()
# #Output:
# #Animal makes a sound
# #Dog barks

# In[1]:


'''6. Create a base class called "Vehicle" with attributes like "make", "model", and "year". 
Then, create a derived class called "Car" that inherits from "Vehicle" and 
adds an attribute called "fuel_type".Implement appropriate methods in both classes.'''

#Ans.
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")


# In[2]:


#Create an instance of the Car class
my_car = Car("Toyota", "C12", 2023, "EV")


# In[3]:


#Access and display attributes from the base class
my_car.display_info()


# In[ ]:





# In[12]:


'''7. Create a base class called "Employee" with attributes like "name" and "salary."
Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
attribute called "department" for the "Manager" class and "programming_language"
for the "Developer" class.'''

#Ans.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: Rs.{self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# In[13]:


# Create instances of the Manager and Developer classes
manager1 = Manager("N Nirmal", 80000, "HR")
developer1 = Developer("Neeraj N", 60000, "Python")


# In[17]:


# Access and display attributes from the base class
manager1.display_info()


# In[16]:


developer1.display_info()


# In[18]:


'''8. Design a base class called "Shape" with attributes like "colour" and "border_width."
Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
the "Circle" class.'''

#Ans.

class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        print(f"Colour: {self.colour}")
        print(f"Border Width: {self.border_width}")


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width

    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"Radius: {self.radius}")


# In[19]:


# Create instances of the Rectangle and Circle classes
rectangle1 = Rectangle("Red", 2, 10, 5)
circle1 = Circle("Blue", 1, 7)


# In[20]:


# Access and display attributes from the base class
rectangle1.display_info()


# In[21]:


circle1.display_info()


# In[ ]:





# In[27]:


'''9. Create a base class called "Device" with attributes like "brand" and "model." Derive
two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
"screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.'''

#Ans.

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size}")


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity}")


# In[28]:


# Create instances of the Phone and Tablet classes
phone1 = Phone("Apple", "iPhone 12", 6.1)
tablet1 = Tablet("Samsung", "Galaxy Tab S7", 8000 )


# In[29]:


# Access and display attributes from the base class
phone1.display_info()


# In[30]:


tablet1.display_info()


# In[ ]:





# In[31]:


'''10. Create a base class called "BankAccount" with attributes like "account_number" and
"balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
"BankAccount." Add specific methods like "calculate_interest" for the
"SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class.'''

#Ans.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Balance: Rs{self.balance}")


class SavingsAccount(BankAccount):
    def calculate_interest(self, interest_rate):
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Interest added: Rs{interest}")

    def display_info(self):
        super().display_info()
        print("Account Type: Savings Account")


class CheckingAccount(BankAccount):
    def deduct_fees(self, fee_amount):
        self.balance -= fee_amount
        print(f"Fees deducted: Rs{fee_amount}")

    def display_info(self):
        super().display_info()
        print("Account Type: Checking Account")


# In[32]:



# Create instances of the SavingsAccount and CheckingAccount classes
savings_account = SavingsAccount("SA001", 5000)
checking_account = CheckingAccount("CA001", 3000)


# In[33]:


# Access and display attributes from the base class
savings_account.display_info()
savings_account.calculate_interest(0.05)
savings_account.display_info()


# In[34]:


checking_account.display_info()
checking_account.deduct_fees(50)
checking_account.display_info()


# In[ ]:


# thank you***

