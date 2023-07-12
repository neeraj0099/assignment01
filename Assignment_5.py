#!/usr/bin/env python
# coding: utf-8

# 1. What does an empty dictionary's code look like?
# 
# Ans.
# In Python, an empty dictionary is represented by a pair of curly braces '{}'
# 
# Example:-
# empty_dict = {}

# 2. What is the value of a dictionary value with the key 'foo' and the value 42?
# 
# Ans.
# the value of a dictionary can be accessed using the corresponding key. In this case, if the dictionary has a key 'foo' with the value 42.
# Example:-
# my_dict = {'foo': 42}
# value = my_dict['foo']
# print(value)  # Output: 42
# 

# 3. What is the most significant distinction between a dictionary and a list?
# 
# Ans.
# Structure:
# 
# Dictionary: A dictionary is an unordered collection of key-value pairs. Each key in the dictionary must be unique, and it is used to access its corresponding value. Keys are typically immutable types like strings or numbers, while values can be of any type.
# 
# List: A list is an ordered collection of elements. The elements in a list are indexed by their position, starting from 0. The elements can be of any type and can be duplicated.
# 
# Accessing Elements:
# 
# Dictionary: Dictionary elements are accessed using their keys. You can retrieve the value associated with a particular key by using square brackets ([]) and providing the key.
# 
# List: List elements are accessed using their indices. You can retrieve the element at a specific position by using square brackets ([]) and providing the index.
# 
# Ordering:
# 
# Dictionary: Dictionaries are unordered, which means there is no inherent order to the key-value pairs. The elements are stored based on their hash values, and the order of insertion may not be preserved.
# 
# List: Lists are ordered, and the order of elements is maintained. The elements are stored based on their position/index.
# 
# Mutability:
# 
# Dictionary: Dictionaries are mutable, which means you can modify, add, or remove key-value pairs.
# 
# List: Lists are mutable, allowing you to modify, add, or remove elements at specific indices.

# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# 
# Ans.
# If  try to access spam['foo'] and spam is {'bar': 100}, will encounter a KeyError because the key 'foo' does not exist in the dictionary spam.
# 
# Example:-
# spam = {'bar': 100}
# value = spam['foo']

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 
# Ans.
# spam = {'cat': 5, 'dog': 3, 'bird': 2}
# 
# 'cat' in spam:
# key_check = 'cat' in spam
# print(key_check)  # Output: True
# 
# 'cat' in spam.keys():
# keys_check = 'cat' in spam.keys()
# print(keys_check)  # Output: True

# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 
# Ans.
# spam = {'animal': 'cat', 'color': 'blue', 'fruit': 'apple'}
# 
# 'cat' in spam:
# key_check = 'cat' in spam
# print(key_check)  # Output: False
# 
# 'cat' in spam.values():
# value_check = 'cat' in spam.values()
# print(value_check)  # Output: True
# 

# 7. What is a shortcut for the following code? if 'color' not in spam:spam['color'] = 'black'
# 
# Ans.
# A shortcut for the given code that checks if the key 'color' is present in the dictionary spam and sets its value to 'black' if it's not can be achieved using the dict.setdefault() method.
# 
# Example:-
# spam = {'animal': 'cat', 'fruit': 'apple'}
# spam.setdefault('color', 'black')
# print(spam) #output {'animal': 'cat', 'fruit': 'apple', 'color': 'black'}

# In[2]:


spam = {'animal': 'cat', 'fruit': 'apple'}
spam['color'] = 'black'
print(spam)


# In[3]:


spam = {'animal': 'cat', 'fruit': 'apple'}
spam.setdefault('color', 'black')
print(spam)


# 8. How do you "pretty print"  dictionary values using which module and function?
# 
# Ans.
# "pretty print" dictionary values using the pprint module and its pprint() function. The pprint module provides a way to format and display complex data structures in a more readable and organized manner.
# 
# Example:-
# import pprint
# 
# my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3','key4': 'value4', 'key5': 'value5', 'key6': 'value6'}
# 
# pprint.pprint(my_dict)
# #output 
# {'key1': 'value1',
#  'key2': 'value2',
#  'key3': 'value3',
#  'key4': 'value4',
#  'key5': 'value5',
#  'key6': 'value6'}

# In[10]:


import pprint

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3','key4': 'value4', 'key5': 'value5', 'key6': 'value6'}

pprint.pprint(my_dict)


# Thank you****

# In[ ]:





# In[ ]:




