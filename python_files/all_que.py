# print("hiiiiii")

# import openpyxl

# workbook = openpyxl.Workbook()
# sheet = workbook.active

# sheet['A1'] = 'Name'
# sheet['B1'] = 'Age'
# sheet['C1'] = 'Country'
# sheet['D1'] = 'City'

# sheet['A2'] = 'vj'
# sheet['B2'] = 32
# sheet['C2'] = 'India'
# sheet['D2'] = 'Mumbai'

# sheet['A3'] = 'Atul'
# sheet['B3'] = 25
# sheet['C3'] = 'Canada'
# sheet['D3'] = 'Toronto'

# sheet['A4'] = 'Deepak'
# sheet['B4'] = 30
# sheet['C4'] = 'Nepal'
# sheet['D4'] = 'Pushiphant'

# workbook.save("current.xlsx")

# import pandas as pd

# df = pd.read_excel("current.xlsx")

# filter_data = df[(df['Country']=='India') | (df['Age'] < 30)]

# print(df,'\n\n\n')
# # print(filter_data,'=====filter_data')

# loc_data =df.loc[:,['Name','Country']]
# print(loc_data,'\n\n')

# subset = df.iloc[1:3, 0:2]  # Access rows 1 and 2, columns 0 and 1
# print(subset)

# import numpy as np

# array_1d = np.array([1,2,3])
# array_2d = np.array([10,20,30])

# new_array = array_1d + array_2d
# print(array_1d,'\n')

# array_vstack= np.vstack((array_1d,array_2d))
# print(array_vstack,'\n')

# array_hstack = np.hstack((array_1d,array_2d))
# print(array_hstack,'\n')

# array_broadcasting = array_1d*100
# print(array_broadcasting) 



# def reverse_list(input_list):
#     i=0
#     j=len(input_list)-1
  
#     while i < j:
#         input_list[i],input_list[j] = input_list[j],input_list[i]
#         i=i+1
#         j=j-1
#     return input_list

# input_list = [1,2,3,4,5]
# obj = reverse_list(input_list)
# print(obj)

# def max_min_list(lst):
#     max_ele = lst[0]
#     min_ele =lst[0]

#     for ele in lst:
#         if ele > max_ele:
#             max_ele = ele
#         else:
#             min_ele = ele
#     return max_ele,min_ele


# lst = [3,10,45,26,4]
# obj = max_min_list(lst)
# print(obj)


# def remove_duplicates(lst):
#     i=0
#     while i < len(lst):
#         if lst.count(lst[i]) > 1:
#             lst.remove(lst[i])
#         else:
#             i=i+1
#     return lst

# lst = [1,1,2,2,2,3,3,4]
# obj = remove_duplicates(lst)

# print(obj)


# def sort_list(lst):
#     swap = True
#     n = len(lst)
#     while swap:
#         swap = False
#         for i in range(1,n):
#             if lst[i-1] > lst[i]:
#                 lst[i-1],lst[i] = lst[i],lst[i-1]
#                 swap = True
#     return lst

# lst = [3,1,4,2,5,6]
# obj = sort_list(lst)

# print(obj )


# def two_sum(lst,target):
#     i=0
#     while i < len(lst)-1:
#         j=i+1
#         if lst[i]+lst[j] == target:
#             return i,j
#         else:
#             j=j+1
#         i=i+1
#     return None


# lst = [2,7,11,9,6]
# target = 8
# obj = two_sum(lst,target)
# print(obj)


# def valid_pattern(str_input):
#     stack = []
#     mydict = {')' : '(',
#               ']' : '[',
#               '}' : '{'

#     }

#     for ele in str_input:
#         if ele in mydict.values():
#             stack.append(ele)

#         elif ele in mydict.keys():
#             if not stack or stack.pop() != mydict[ele]:
#                 return False
#         else:
#             return False
        
#     return not stack


# str_input = '{([{(}])}'
# obj = valid_pattern(str_input)
# print(obj)


# def star_pattern(input_data):
#     for i in range(input_data,0,-1):
#         print(" "*i,"*"*(2*(input_data-i)-1))

#     for i in range(0,input_data):
#         print(" "*i,"*"*(2*(input_data-i)-1))

# input_data = 5
# obj = star_pattern(input_data)


# def some_pattern(input_data):
#     for i in range(1,input_data+1):
#         for j in range(1,i+1):
#             print("*",end= " ")
#         print()

# def some_pattern(input_data):
#     i=0
#     while i < input_data+1:
#         print("*"*i,end=" ")
#         print()
#         i=i+1

# input_data = 5
# obj = some_pattern(input_data)



# def decorator_funct(func):
#     def inside_function(*args,**kwargs):
#         print("inside function",args[0],args[1])
#         return func(*args,**kwargs)
#     print("outside function")
#     return inside_function

# @decorator_funct
# def some_function(a,b):
#     print(a,b)
#     return a,b
    
# obj = some_function(10,20)

def sum_func(a,b):
    return a+b























































