#with using set
def has_unique_chars(str):
    char_set = set()
    for char in str:
        if char in char_set:
            return False
        char_set.add(char)
    return True

# without using set 
# def has_unique_chars(str):
#     flag = False
#     if str == '':
#         return True
#     freq = {}
#     for item in str:
#         if item in freq:
#             freq[item] += 1
#         else:
#             freq[item] = 1

#     for item in freq.items():
#         if item[1] > 1:
#             flag = False
#             return flag
#         else:
#             flag = True
#     return flag
        

print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False