# =============( Python Notes )================
# String input 
# name = input("Enter your name: ")
# print(name)

# Integer input
# age = input("Enter your age: ")
# print(age)

# Float input
# price = float(input("Price: "))
# print(price)
# =======================================

# =======================================
# List -> Array
# a = [1, 2, 3, 4, 5]
# for i in range(len(a)):
#     print(a[i])

# List -> Array
# a = [1,2,3,4,5]
# a.append(4)
# a[0] = 123
# print(a[5])
# =======================================

# =======================================
# person = {"name": "Rafi", "age": 30}
# print(person["name"])
# print(person["age"])

# a = {1,2,3,4,5}
# a.add(7)
# a.remove(2)
# print(a)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#           print("Hi", self.name)
# p = Person("Rafi")
# p.greet()
# =======================================

# [if-else, elif method] ================
# light = input("Light color: ")
# if light == "red":
#     print("Stop")
# elif light == "green":
#     print("Go")
# else:
#     print("Wrong input")

# A = int(input("A: "))
# G = input("G/F: ")
# if (A == 5 or A == 9) and G == "M":
#     print("Yes")
# elif (A == 6 or A == 10) and G == "F":
#     print("No")
# else:
#     print("Maybe")
# =======================================

# =======================================
# sal = float(input("Salary: "))
# tax = sal * (0.1, 0.2) [sal <= 50000]
# print("Tax:", tax)

# name = "rafi"
# print(name.title())# rafi -> Rafi
# =======================================

# [Dictionary method] ===================
# menu = {
#     "Pizza" : 40,
#     "Salad" : 50,
#     "Coffe" : 60,
# }
# for item, price in menu.items():
#     print(f"{item: < 10} : {price}")
# =======================================

# =======================================
# a = "Hello"
# for i in range(len(a)):
#     print(a[i])

# a = "Hello"
# print(list(a))# ['H', 'e', 'l', 'l', 'o']

# a = list(range(5)) 
# print(a) # [0, 1, 2, 3, 4]

# b = list(range(1, 10, 2)) 
# print(b) # [1, 3, 5, 7, 9]

# b = list(range(10, 1, -1)) 
# print(b) # [10, 9, 8, 7, 6, 5, 4, 3, 2]
# =======================================


# [enumerate option]=====================
### enumerate(iterable, start=0)

# my_list = ["a", "b", "c", "d"]
# for index, value in enumerate(my_list, 1):
#     print(index, value)

# list(enumerate(["A", "B", "C"], 1))
# # Output: [(1, "A"), (2, "B"), (3, "C")]

# ===========
# my_list = [
#     {"task": "Apple"},
#     {"task": "Banana"},
#     {"task": "Salad"},
#     {"task": "Coffee"}
# ]
# # 1s way (high risk)                                  
# # for i in range(len(my_list)):               
# #     print(f"{i+1}: {my_list[i]["task"]}")   

# # 2nd way (Best practice)                                  
# for index, value in enumerate(my_list, 1):  
#     print(f"{index}: {value["task"]}")   
# =======================================



# [for loop] ============================
# a = [1,2,3,4,5,6,7,8,9]
# for item in a:
#     print(item, end=" ")
# =======================================

# [while loop] ==========================
# a = [-9,-2,3,2,4,-7,-10,11,12]
# i=0
# while i < len(a):
#     if a[i] < 0:
#         a[i] = 0
#     i+=1
# print(a) # [0, 0, 3, 2, 4, 0, 0, 11, 12]
# =======================================

# # [Set method] ========================
# a = [1,2,2,3,4,4,5,6,7,7,7]
# s = set(a)
# print(s) # {1, 2, 3, 4, 5, 6, 7}
# =======================================

# # [Union, Intersection methods] =======
# a = {1,2,3,4}
# b = {2,3,4}
# c = a.intersection(b)
# d = a.union(b)
# print(c) # {2, 3, 4}
# print(d) # {1, 2, 3, 4}
# =======================================

# # [Zip mathod] ========================
# a = [1,2,3]
# b = ["Mango", "Banana", "Apple"]
# print(dict(zip(a,b))) # {1: 'Mango', 2: 'Banana', 3: 'Apple'}
# =======================================

# # [list comprehention] ================
# nums = list(range(0,11))

# result = {i:"Even" if i%2==0 else "Odd" for i in nums}
# print(result)
# # {0: 'Even', 1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd', 6: 'Even', 7: 'Odd', 8: 'Even', 9: 'Odd', 10: 'Even'}
# =======================================

# [ map(), filter() ] ===================
#1. Map
# map(function, variable-name)
# nums = [1,2,3,4]
# sq_nums = list(map(lambda x: x*x, nums))
# print(sq_nums) # [1, 4, 9, 16]

# #2 Filter
# nums = [1,2,3,4,5,]
# evenNum = list(filter(lambda x: x%2==0, nums))
# print(evenNum) # [2, 4]
# =======================================

# [Global Method] =======================
# # default
# name = "Global"
# def outer():
#     name = "Enclosing"
#     print(name)
#     def inner():
#        name = "Local"
#        print(name)
#     inner()
# outer()
# print(name) # Enclosing Local Global

# #Apply the method
# name = "Global"
# def outer():
#     name = "Enclosing"
#     print(name)
#     def inner():
#        global name # Now it will work like Global
#        name = "Local"
#        print(name)
#     inner()
# outer()
# print(name) # Enclosing Local Local
# =======================================

# # [Reading from File] =================
# file = open('mainPy/name.txt', 'r')
# content = file.read()
# print(content) # Hello my name is Rafi (mainPy/name.txt)

# # Best practice
# with open('mainPy/name.txt', 'r') as f:
#     content = f.read()
#     print(content) # Hello my name is Rafi (mainPy/name.txt)
# =======================================

## [Changing the files text] ============
## name.txt -> 
# Hello my name is Rafi - 1
# Hello my name is Rafi - 2
# Hello my name is Rafi - 3

## main.py ->
# with open('mainPy/name.txt', 'w') as f:
#     f.write("Files text changed ")

# after run the (main.py) now (name.txt) is -> 
# Files text changed 

## Append method: 
# with open('mainPy/name.txt', 'a') as f:
#     f.write("\nFiles text added\n")
#     f.write("Files text added\n")
#     f.write("Files text added\n")

## now name.txt is ->
# Hello my name is Rafi - 1
# Hello my name is Rafi - 2
# Hello my name is Rafi - 3
# Files text added <--new added
# Files text added <--new added
# Files text added <--new added
# =======================================

# =======================================
# import os
# import pathlib

# file_path = pathlib.Path('file.txt')

# if file_path.exists():
#     print('Yes file found') # Yes file found
# =======================================


# [Image opening by path]================
# from PIL import Image # "pip install pillow"
# filePath = input("Enter your file path: ")
# Images = Image.open(filePath)
# Images.show() # open the images 
# =======================================

