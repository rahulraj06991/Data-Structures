# array = [5, 1, 7, 2, 9, 3], Target = 10 , output = [1,4]

# Two way of solving this problem.
# First, store array elements with their indices in a dictionary; then check for the complement in the keys while excluding the current index.
# Continue until a matching pair is found and return the indices.
def two_sum(arr, target):
    value_index_map = {val: i for i, val in enumerate(arr)}
    for i, val in enumerate(arr):
        complement = target - val
        if complement in value_index_map and value_index_map[complement] != i:
            return [i, value_index_map[complement]]
    return []    

# 2nd, declare a dictionary, then loop through the list and check if the complement is in the dictionary; if not, add the current number with its index. 
# Continue until a matching pair is found and return the indices.
# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i
#     return []

    
print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))  
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
print(two_sum([1, 3, 5, 7, 9], 10))  
print ( two_sum([1, 2, 3, 4, 5], 10) )
print ( two_sum([1, 2, 3, 4, 5], 7) )
print ( two_sum([1, 2, 3, 4, 5], 3) )
print ( two_sum([], 0) )

