print("hiiiiiiiiiiiiii")

import numpy as np
import pandas as pd

# class Animal:
#     def __init__(self,name,type_of):
#         self.name = name
#         self.type_of = type_of

#     def display(self):
#         print(f"{self.name }/{self.type_of} .....")

# obj = Animal("Cheetah",'omin')
# obj.display()

# class Animal:
#     def display(self,name,type_of):
#         self.name = name
#         self.type_of = type_of

# obj = Animal()
# print(obj.display("Cheetah",'omin'))
# name="llll"
# class Calculator:
#     def __init__(self,name):
#         self.name = name
#     def add(self, x, y):
#         print(name)
#         # print(self.x)
#         return x + y
    
# obj = Calculator("vh")
# print(obj.add(1,2))

# class MyClass:
#     def __init__(self, value):
#         self.__value = value

#     def __display(self):
#         print("Value:", self.__value)


# # Creating an object using the constructor
# obj = MyClass(42)

# # Accessing the "private" attribute (although it's not strictly enforced)
# # print(obj.__value)  # Output: 42

# # # Calling the "public" method
# # obj.__display()  # Output: Value: 42


# # def wrapper_func(func):
# #     def inner_func():
# #         print("inner function")
# #         return func()
# #     print("wrapper function")
# #     return inner_func()
 
# # @wrapper_func
# # def new_func():
# #     print("new function")


# # class BankAccount:
# #     def __init__(self, account_number, balance):
# #         self._account_number = account_number
# #         self._balance = balance

# #     def deposit(self, amount):
# #         self._balance += amount

# #     def withdraw(self, amount):
# #         if amount <= self._balance:
# #             self._balance -= amount
# #         else:
# #             print("Insufficient funds.")

# #     def get_balance(self):
# #         return self._balance

# #     def get_account_number(self):
# #         return self._account_number


# # # Creating a bank account object and interacting with it through public methods
# # account = BankAccount("123456789", 1000)
# # account.deposit(500)
# # account.withdraw(200)

# # print("Account Number:", account.get_account_number())
# # print("Balance:", account.get_balance())

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side

    
# class Rectangle(Shape):
#     def __init__(self, length,breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         return self.length * self.breadth




# Attempting to create an instance of the abstract base class directly will raise an error.
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract methods area

# Creating instances of concrete subclasses
# square = Square(5)
# r = Rectangle(2,5)
# print(r.area())
# print("Area of Square:", square.area())  # Output: Area of Square: 25


# input_text = 'hello world' 
# output_text = 'drwolh'

# op = input_text[::2]
# print(op[::-1])

# first_class  = 3number(10,20,23)
# op = (5,20+23)

# class addition:
#     def __init__(self,b,c):
#         self.b = b
#         self.c = c
#     def calc(self):
#         total = self.b + self.c
#         return total
    
# class operation(addition):
#     def __init__(self,b,c):
#         self.b = b
#         self.c = c
#     def divide(self):
#         return self.b//2


# # obj = addition(10,20)
# # print(obj.calc())

# newobj = operation(100,200)
# print(newobj.divide())
# print(newobj.calc())
# # class user_opertion(addition):
# #     pass 

# def sort():
#     list1 = [1,3,2,5,4]
#     n =len(list1)
#     swap = True

#     while swap:
#         swap = False
#         for i in range(1,n):
#             if list1[i-1] > list1[i]:
#                 list1[i-1],list1[i] = list1[i],list1[i-1]
#                 swap = True

#     print(list1)

# obj = sort()
# mylist = [1,2,3,5]
# list1 = map(lambda x:x**2,mylist)

# # list1 = [n**2 for n in range(1,11)]
# print(list(list1))


# regex_expression = r'(\d(1,3)\.(3))$'

# def reverse_list(lst):
#     i=0
#     j=len(lst)-1
#     while i < j:
#         lst[i],lst[j] = lst[j],lst[i]
#         i=i+1
#         j=j-1
#     return lst

# lst = [1,2,4,5,9]
# obj = reverse_list(lst)
# print(obj,'=============obj')

# def max_and_min_numbers(lst):
#     max_number = lst[0]
#     min_number = lst[0]
#     for ele in lst:
#         if ele > max_number:
#             max_number = ele
#         if ele < min_number:
#             min_number = ele
#     return max_number,min_number
# lst = [3,1,5,8,9]
# obj = max_and_min_numbers(lst)
# print(obj,type(obj))

# def remove_duplicates(lst):
#     i=0
#     while i <len(lst):
#         item = lst[i]
#         if lst.count(item) > 1:
#             lst.remove(item)
#         else:
#             i=i+1

#     return lst
# lst = [1,3,1,2,5]    
# obj = remove_duplicates(lst)
# print(obj)


# def two_pointers_sort(lst):
#     n = len(lst)
#     swapped = True

#     while swapped:
#         swapped = False
#         for i in range(1,n):
#             if lst[i-1] > lst[i]:
#                 lst[i-1],lst[i] = lst[i],lst[i-1]
#                 swapped = True
#         n=n- 1

#     return lst
    


# lst= [1,3,2,5,9,7]
# obj = two_pointers_sort(lst)
# print(obj)


# def count_frequency(lst):
#     freq_dict = {}
#     for item in lst:
#         freq_dict[item] = freq_dict.get(item, 0) + 1
#     return freq_dict

# lst = [1,2,1,3,3,2,4]
# obj = count_frequency(lst)



n=5
 
# for i in range(0,n):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()

# i=1
# while i < n:
#     print(i*str(i),end="")
#     print()
#     i=i+1

   

# def sort_list(list3):
#     n=len(list3)

#     swap=True

#     while swap:
#         swap=False
#         for i in range(1,n):
#             if list3[i-1]  > list3[i]:
#                 list3[i-1],list3[i] = list3[i],list3[i-1]
#                 swap =True
#             n=n-1
#     return list3
# list3  = [1, 3, 5, 7, 2, 4, 6, 8]
# obj = sort_list(list3)
# print(obj)

# ip_string = "A4B1D3"
# # op= "AEBCDG"
# result = ""

# for ele in ip_string:
#     if ele.isalpha():
#         previous = ele
#     else:
#         result = result + previous + chr(ord(previous)+int(ele))

# print(result)


# ip_string = "A4B1D3"
# op = 'AAAABDDD'
# result = ""

# for ele in ip_string:
#     if ele.isalpha():
#         previous = ele
#     else:
#         result = result + previous*int(ele)


# print(result)

# ip_string = 'AAAABDDD'
# # op = "A4B1D3"
# result = ""
# count = 1

# for i in range(1,len(ip_string)):
#     if ip_string[i] == ip_string[i-1]:
#         count=count+1
#     else:   
#         result = result + ip_string[i-1]+str(count)
#         count=1
# result = result + ip_string[-1]+str(count)
# print(result)

#####prime number
# ip= int(input("Enter the number: "))

# if ip == 1:
#     print("not prime")

# elif ip > 1:
#     for i in range(2,ip):
#         if ip%i == 0:
#             print("not prime")
#             break

#     else:
#         print("prime")




#####find substring count
def count_string():
    ip_string = "abaababab"
    sub = "ab"
    count = 0
    i=0

    while i < len(ip_string):
        if ip_string[i:i+len(sub)] == sub:
            print(count)
            count=+1
            i=i+len(sub)
        else:
            i=+1
    return count

obj = count_string()
print(obj)


def count_substring_occurrences(main_string, substring):
    count = 0
    for i in range(len(main_string)):
        if main_string[i:i+len(substring)] == substring:
            count += 1
    return count

main_string = "abcabcdabdabcd"
substring = "abc"

occurrences = count_substring_occurrences(main_string.lower(), substring.lower())
print(f"The substring '{substring}' appears {occurrences} times.")





















































































































































