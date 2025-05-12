class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        return True
    
def find_kth_node(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        #print(fast.value)
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
        # if(slow is not None): 
        #     print(slow.value)
        # else: 
        #     print ("None")
        # if(fast is not None):
        #     print(fast.value) 
        # else: 
        #     print ("None")
    return slow


my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.append(3)

my_linked_list.append(4)

print(find_kth_node(my_linked_list, 1).value)

