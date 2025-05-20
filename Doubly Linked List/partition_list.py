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
    
    def partitionList(self, x):
        if self.head is None:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        left = dummy1
        right = dummy2
        curr = self.head 
        while curr:
            if curr.value < x:
                left.next = curr
                curr.prev = left
                left = curr
            else:
                right.next = curr
                curr.prev = right
                right = curr
            curr = curr.next
        left.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = left
        right.next = None
        self.head = dummy1.next
        self.head.prev = None
        
my_doubly_linked_list = DoublyLinkedList(3)
my_doubly_linked_list.append(8)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(10)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(1)


print(my_doubly_linked_list.partitionList(5))

my_doubly_linked_list.print_dll()
