def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst
# lst = [1,2,3,4,5,8,9]
# obj = reverse_list(lst)
# print(obj)


def find_max_min(lst):
    max_val = lst[0]
    min_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val
lst = [1,2,3,4,5,8,9,3,10,1,5]
# obj = find_max_min(lst)
# print(obj)

def remove_duplicates(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst


# lst = [1,2,3,4,5,8,9,3,10,1,5]
# obj = remove_duplicates(lst)
# print(obj)


# def count_frequecy(lst):
#     mydict = {}
#     for ele in lst:
#         mydict[ele] = lst.count(ele)

    

#     max_key = max(mydict, key=lambda k: mydict[k])
#     print(max_key)
#     max_value =max(mydict)
#     print(max_value)

#     return mydict

# lst = [1,2,1,3,3,4,6,6,6,1,1]



# obj = count_frequecy(lst)
# print(obj)

# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return None

# # Example usage:
# nums = [2, 7, 11, 15]
# target = 9
# result = two_sum(nums, target)
# print(result)  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)


# def two_sum(lst,target):
#     i=0
#     while i < len(lst)-1:
#         j=i+1
#         if lst[i] + lst[j] == target:
#             return i,j
#         else:
#             j=j+1

#         i=i+1
#     return None

# nums = [2, 7, 11, 15]
# target = 26
# result = two_sum(nums, target)
# print(result)
    

# def rotate_list(lst, k):    
#     return lst[k:] + lst[:k]

# lst = [1,2,3,4,6,9]
# k=2
# obj = rotate_list(lst,k)
# print(obj)


def count_rotations(arr):
    min_value = min(arr)
    min_index = arr.index(min_value)
    return min_index

# Test the function
arr = [4, 5, 6, 7, 1, 2, 3]
print(count_rotations(arr))  # Output: 4




























