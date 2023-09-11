
##Reverse the list without using any inbuilt-function
def reverse_list(lst):
    i=0
    j= len(lst)-1
    while i < j:
        lst[i],lst[j] = lst[j],lst[i]
        i=i+1
        j=j-i
    return lst

lst = [1,2,3,4,5,9]
obj = reverse_list(lst)
print(obj,'reverse_list')

print("\n\n")


####Find max and min in the list without using any inbuilt-function
def max_min_list(lst):
    max_number = lst[0]
    min_number = lst[0]

    for ele in lst:
        if ele > max_number:
            max_number = ele
        if ele < min_number:
            min_number = ele

    return max_number,min_number


lst = [1,4,6,9,4,0,2]
obj =max_min_list(lst)
print(obj,'max_min_list')

print("\n\n")

###Remove duplicate elements from the list 
####without using any inbuilt-function
def remove_duplicates(lst):
    new_list = []

    for ele in lst:
        if ele not in new_list:
            new_list.append(ele)
    return new_list

lst = [0,1,2,2,3,2,1,5]
obj = remove_duplicates(lst)
print(obj,'remove_duplicates')

print("\n\n")

###Remove duplicate elements from the list 
####without using any inbuilt-function and new list too(Important question)
def remove_duplicates(lst):
    for ele in lst:
        if lst.count(ele) > 1:
            lst.remove(ele)
    return lst

lst = [0,1,2,2,3,2,1,5]
obj = remove_duplicates(lst)
print(obj,'remove_duplicates')

print('\n\n')

####sort the list without using any inbuilt-function
def sort_list(lst):
    n = len(lst)
    swap = True
    while swap:
        swap = False
        for i in range(0,n-1):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                swap = True
            n=n-1
    return lst
    

lst = [3,1,4,6,5]
obj = sort_list(lst)
print(obj,'sort_list')

print('\n\n')


######Find the index value from the list according
######to sum in the target
def two_sum(lst,target):
    i=0

    while i < len(lst)-1:
        j=i+1
        if lst[i] + lst[j] == target:
            return i,j
        else:
            j=j+1
        i=i+1
    return False



lst = [1,3,5,6,11] 
target = 17
obj = two_sum(lst,target)
print(obj,'two_sum')


print('\n\n')


###Find the count rotation done for sorted list 
###without using count value
def rotate_list(lst):
    number = min(lst)
    rotation = lst.index(number)

    final_lst = lst[rotation:] + lst[:rotation]

    return final_lst,rotation


lst= [4,5,6,7,1,2,3]
obj = rotate_list(lst)
print(obj,'rotate_list')

print('\n\n')


####Count the number of substring in string
def count_substring(string_ip,substring):
    count=0
    i = 0

    while i < len(string_ip)-1:
        if string_ip[i:i+len(substring)] == substring:
            count=count+1
            i=i+len(substring)
        else:
            i=i+1
    return count


string_ip = "abaababa"
substring = 'ab'
obj = count_substring(string_ip,substring)
print(obj,'count_substring')


###How to create decorator function
def decorator_func(func):
    def wrapper_func():
        print('wrapper func')
        return func()
    print("Decorator func")
    return wrapper_func

@decorator_func
def new_func():
    print("new func")

obj = new_func()

print('\n\n')


#### Constructor in python class
class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age


    def some_func(self):
        print("{}/{}".format(self.name,self.age))


obj = Employee('vijay',32)
obj.some_func()

print("\n\n")
###How to make transcation in bank
class bank_account: 
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number = account_number
        self.account_holder  = account_holder
        self.balance = balance

    def cash_deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def cash_withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("balance is too low")

    def check_balance(self):
        return self.balance


account1 = bank_account("123456789",'vijay')
account2 = bank_account("00000000",'divya')

print(f"Initial balance for {account1.account_holder}: ${account1.check_balance()}")
print(f"Initial balance for {account2.account_holder}: ${account2.check_balance()}")


deposit_ammount = 500
account1.cash_deposit(deposit_ammount)
print(f"Deposited ${deposit_ammount} into {account1.account_holder}'s account")
print(f"New balance for {account1.account_holder}:${account1.check_balance()}")


amount_with = 300
account1.cash_withdraw(amount_with)
print(f"Withdraw ${amount_with} into {account1.account_holder}'s account")
print(f"New balance for {account1.account_holder}:${account1.check_balance()}")

print("\n\n")
#data encapsulation
class Employee:  
    def __init__(self,name,age,pid):
        self.name = name
        self.age = age
        self.__pid = pid

    def __closedfunc(self):
        print(f'{self.name} /{self.age} and its private method')

    def openfunc(self):
        print(f'{self.name} /{self.age}/{self.__pid} and its open method')

obj = Employee('vj',32,2)
obj.openfunc()
###Please uncomment to see the error
# print(obj.name,'============name',obj.__pid)
# obj.__closedfunc()


print("\n\n")




###why to use super class
class parent:
    def __init__(self,x):
        self.x = 50


class child(parent):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y


obj1  = child(10,20)
print(obj1.x)
print(obj1.y)


#######method overloading
class shape:
    def identity_obj(self,a=None,b=None,c=None):

        if a != None and b != None and c != None:
            print("Triangle")

        elif a != None and b != None:
            print("rectangle")
        
        elif a != None:
            print('square or circle')

        else:
            print("not match any figure")

obj = shape()
obj.identity_obj(20,30)

print("\n\n")

##Method overloading
class do_calculation:
    def sum_calc(self,*args):
        result = 0
        if len(args) == 3:
            result = args[0] + args[1] + args[2]
            return result
        
        elif len(args) == 2:
            result = args[0] + args[1]
            return result
        
        elif len(args) == 1:
            result = args
            return result
        else:
            return result
    
obj = do_calculation()
print(obj.sum_calc(10,25,45,5))

from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def area(self,a):
        return 3.14*a*a
    

class rectange(shape):
    def area(self,a,b):
        return a*b
    
obj = circle()
print(obj.area(5))
obj1 = rectange()
print(obj1.area(10,20))

######multiple level inheritance
class A:
    def method(self):
        print("method from class A")

    def new_func(self):
         print("function from class A")

class B(A):
    def method(self):
        print("method from class B")

    
class C(B,A):
    pass


obj = C()
obj.method()
obj.new_func()

print('\n\n\n')

#######create excel sheet
import openpyxl 
workbook = openpyxl.Workbook()
sheet = workbook.active

sheet['A1'] = "Name"
sheet['B1'] = "Age"
sheet['C1'] = "City"
sheet['D1'] = "Country"

sheet['A2'] = "vj"
sheet['B2'] = 30
sheet['C2'] = "Mumbai"
sheet['D2'] = "India"

sheet['A3'] = "Divya"
sheet['B3'] = 28
sheet['C3'] = "Toronto"
sheet['D3'] = "Canada"

sheet['A4'] = "Atul"
sheet['B4'] = 25
sheet['C4'] = "Vancover"
sheet['D4'] = "Canada"


###----------Uncomment this line to create excel sheet-----
# workbook.save("data_excel.xls")



###How to use pandas
import pandas as pd

df = pd.read_excel('data_excel.xls')
print(df,'\n\n')

df_rows,df_columns = df.index(0)
print(df_rows,df_columns)

# df_filteration = df[(df['Age'] < 35) | (df['Country'] == "Canada")]

# print(df_filteration)

# df_loc = df.loc[2:,['Name']]
# print(df_loc)

# print('\n\n')

# df_iloc= df.iloc[1:,2:]
# print(df_iloc)



###########How to use numpy
import numpy as np

list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,9,10]

array = np.array(list1)
print(array)

print('\n\n')
array1 = np.array(list2)
print(array1)

print('\n\n')

array_reshape = array.reshape(2,3)
print(array_reshape)

print('\n\n')


array_broadcasting = array_reshape * 10
print(array_broadcasting)

print('\n\n')

array_mean = array.mean()
print(array_mean)

print('\n\n')

array_hz = np.hstack((array,array1))
print(array_hz)

print('\n\n')

array_vz = np.vstack((array,array1))
print(array_vz)




























    









































