# def remove_duplicates(list1):
#     unique = set()
#     for element in list1:
#         unique.add(element)
#     return list(unique)
    

def remove_duplicates(list1):
    new_list = list(set(list1)) 
    return new_list


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)


