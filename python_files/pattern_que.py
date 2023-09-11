# def print_pattern(n):
#     for i in range(0,n+1):
#         print('* ' * i)

# print_pattern(5)

def number_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Test the function
number_pyramid(5)

# def fibonacci(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         next_num = fib_sequence[-1] + fib_sequence[-2]
#         fib_sequence.append(next_num)
#     return fib_sequence

# Test the function
# print(fibonacci(10))

# def prime_number(n):
#     if n == 1:
#         print("not prime")

#     if n > 2:
#         for i in range(2,n):
#             if n%i == 0:
#                 print("Not prime")
#                 break
#         else:
#             print("prime")

# obj = prime_number(97)
# print(obj)


# list1 = [1,2,3]
# mydict = {x:x**2 for x in range(1,5)}
# print(mydict)

# mylist = map(lambda x:x**2 ,list1) 
# print(list(mylist))

# def is_valid_parentheses(s):
#     stack = []
#     mapping = {')': '(', 
#                '}': '{', 
#                ']': '['}
    
#     for char in s:
#         if char in mapping.values():
#             stack.append(char)
#         elif char in mapping.keys():
#             if not stack or stack.pop() != mapping[char]:
#                 return False
#         else:
#             return False
    
#     return not stack

# # Test cases
# print(is_valid_parentheses("(({([{}])}))"))  # True
# print(is_valid_parentheses("({[}])"))    # False



# def upside_pyramid(n):

#     # for i in range(n,0,-1):
#     #     print(" "*i + "*" * (2*(n-i)-1))

#     for i in range(0,n):
#         print(" "*i + "*" * (2*(n-i)-1))

# obj = upside_pyramid(6)
    

    





