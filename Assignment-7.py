#!/usr/bin/env python
# coding: utf-8

# Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
# and store the results in variables. Then print the data in the following format by calling the
# variables:
# First variable is __ & second variable is __.
# Addition: __ + __ = __
# Subtraction: __ - __ = __
# Multiplication: __ * __ = __
# Division: __ / __ = __
# 
# Ans.
# 
# #Create two int variables
# first_variable = 10
# second_variable = 5
# 
# #Perform addition, subtraction, multiplication, and division
# addition = first_variable + second_variable
# subtraction = first_variable - second_variable
# multiplication = first_variable * second_variable
# division = first_variable / second_variable
# 
# #Print the results
# print("First variable is", first_variable, "& second variable is", second_variable)
# print("Addition:", first_variable, "+", second_variable, "=", addition)
# print("Subtraction:", first_variable, "-", second_variable, "=", subtraction)
# print("Multiplication:", first_variable, "*", second_variable, "=", multiplication)
# print("Division:", first_variable, "/", second_variable, "=", division)
# 

# In[1]:


# Create two int variables
first_variable = 10
second_variable = 5

# Perform addition, subtraction, multiplication, and division
addition = first_variable + second_variable
subtraction = first_variable - second_variable
multiplication = first_variable * second_variable
division = first_variable / second_variable

# Print the results
print("First variable is", first_variable, "& second variable is", second_variable)
print("Addition:", first_variable, "+", second_variable, "=", addition)
print("Subtraction:", first_variable, "-", second_variable, "=", subtraction)
print("Multiplication:", first_variable, "*", second_variable, "=", multiplication)
print("Division:", first_variable, "/", second_variable, "=", division)


# Q.2. What is the difference between the following operators:
# (i) ‘/’ & ‘//’
# (ii) ‘**’ & ‘^’
# 
# Ans.
# 
# (i) '/' and '//':
# 
# The '/' operator is used for division. When used with two integers, it performs floating-point division and returns a floating-point result. For example, 7 / 2 would give the result 3.5.
# 
# The '//' operator is used for floor division (also known as integer division or truncating division). It performs division and rounds down the result to the nearest whole number. It always returns an integer result. For example, 7 // 2 would give the result 3.
# 
# (ii) '**' and '^':
# 
# The '**' operator is used for exponentiation. It raises the left operand to the power of the right operand. For example, 2 ** 3 would give the result 8.
# 
# The '^' operator is not used for exponentiation in Python. Instead, it is the bitwise XOR operator, which performs a bitwise exclusive OR operation on the operands. It is used to manipulate individual bits in binary representations. For example, 5 ^ 3 would give the result 6 .

# Q.3. List the logical operators.
# 
# Ans.
# and: The and operator returns True if both operands are true, otherwise it returns False.
# 
# or: The or operator returns True if at least one of the operands is true, otherwise it returns False.
# 
# not: The not operator is a unary operator that returns the opposite boolean value of its operand. If the operand is True, not returns False, and if the operand is False, not returns True.
# 

# Q.4. Explain right shift operator and left shift operator with examples.
# 
# Ans.
# Right Shift Operator (>>):
# The right shift operator shifts the bits of a number to the right by a specified number of positions. The rightmost bits are discarded, and the leftmost bits are filled with the sign bit or with zeros.
# Example:
# a = 8  # Binary representation: 00001000
# b = 2
# result = a >> b
# print(result)  # Output: 2
# #Binary representation of 2 after right shifting by 2 positions:
# #00000010
# 
# Left Shift Operator (<<):
# The left shift operator shifts the bits of a number to the left by a specified number of positions. Zeros are filled in from the right side, and any bits shifted beyond the number of available bits are discarded.
# Example:
# a = 3  # Binary representation: 00000011
# b = 2
# result = a << b
# print(result)  # Output: 12
# 
# #Binary representation of 12 after left shifting by 2 positions:
# #00001100

# In[3]:


a = 8  # Binary representation: 00001000
b = 2
result = a >> b
print(result)  # Output: 2
#Binary representation of 2 after right shifting by 2 positions:
#00000010


# In[4]:


a = 3  # Binary representation: 00000011
b = 2
result = a << b
print(result)  # Output: 12

#Binary representation of 12 after left shifting by 2 positions:
#00001100


# Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is present in the list or not.
# 
# Ans.
# 
# #Create a list of integers
# my_list = [1, 3, 5, 7, 9, 10, 12, 14, 15]
# 
# #Check if 10 is present in the list
# if 10 in my_list:
#     print("10 is present in the list.")
# else:
#     print("10 is not present in the list.")

# In[2]:


#Create a list of integers
my_list = [1, 3, 5, 7, 9, 10, 12, 14, 15]

#Check if 10 is present in the list
if 10 in my_list:
    print("10 is present in the list.")
else:
    print("10 is not present in the list.")


# In[ ]:




