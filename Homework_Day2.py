#!/usr/bin/env python
# coding: utf-8

# In[1]:


First_Name = input("First Name: ")

Last_Name = input("Last Name: ")

Age = input("age: ")

Date_of_birth_year = input("Date of birth (just year): ")

age = input("How old are you? ")
age = int(age)
if age <18:
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street")

user_info = [First_Name, Last_Name, Age, Date_of_birth_year]
for x in user_info:
    print(x)

