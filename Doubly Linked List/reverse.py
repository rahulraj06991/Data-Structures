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


    def reverse(self):
        #swap head and tail
        temp = self.tail
        self.tail = self.head
        self.head = temp
        #print(temp.value)
        while temp:           
            before = temp.prev
            temp.prev = temp.next
            temp.next = before
            temp = before 
            # the above line can be 
            # temp = temp.next
        
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)


my_doubly_linked_list.reverse()

my_doubly_linked_list.print_dll()