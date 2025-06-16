# Input: [1,2,3,4,5], Target = 9 , Output: [1,3]

#Here, we have used prefix sum and it has time complexity of O(n)
def subarray_sum(nums, target):
    sum_index = {0: -1}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum+=num
        if current_sum-target in sum_index:
            return [sum_index[current_sum-target]+1, i]
        sum_index[current_sum]=i
    return []

# This is a brute force technique with time complexity of O(n^2) because of nested loop
# def subarray_sum(nums, target):
#     for i in range(0, len(nums), 1):
#         sum = 0
#         result = []
#         for j in range(i, len(nums), 1):
#             sum = sum+nums[j]
#             if(sum == target):
#                 result.append(i)
#                 result.append(j)

#                 return result
#     return []


nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [1, 2, 3, 4, 5]
target = 9
print(subarray_sum(nums, target))

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )