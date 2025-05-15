class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_dll(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    # Technique 1, it uses a list (an additional data structure) and it has two loop which has complexity of O(n) and has larger space complexity i.e. O(n)
    # def is_palindrome(self):
    #     temp = self.tail
    #     list1 = []
    #     for _ in range(self.length):
    #         list1.append(temp.value)
    #         temp = temp.prev
    #     temp2 = self.head
    #     list2  = []
    #     for _ in range(self.length):
    #         list2.append(temp2.value)
    #         temp2 = temp2.next
    #     print(list1, list2)
    #     if list1 == list2:
    #         return True
    #     return False

    # Technique 2, It uses two pointer and a loop it has a complexity of O(n) and has space complexity of O(1)
    def is_palindrome(self):
        left = self.head
        right = self.tail
        for _ in range(self.length // 2):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True
    
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)

print(my_doubly_linked_list.is_palindrome())