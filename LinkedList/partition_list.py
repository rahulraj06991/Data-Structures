#partitioning the linked list where elements smaller than x will be at left and greater than x will be at right
# sample input 3 -> 1 -> 4 -> 2 -> 5, x =3
#sample output 1 -> 2 -> 3 -> 4 -> 5
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length+=1
        return True
    
    def print_list(self):
        if(self.head is None):
            print("emty list")
        else:
            temp = self.head
            values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        print(" -> ".join(values))
    
    def partition_list(self, x):
        if self.head is None:
            return None
        dummy1 = Node(0)
        dummy2 = Node(0)
        left = dummy1
        right = dummy2
        curr = self.head
        while curr is not None:
            if curr.value < x:
                left.next = curr
                left= curr
            else:
                right.next = curr
                right = curr
            curr = curr.next
        left.next = dummy2.next
        right.next = None
        self.head = dummy1.next

my_linked_list = LinkedList(3)
my_linked_list.append(1)
my_linked_list.append(4)
my_linked_list.append(2)
my_linked_list.append(5)

my_linked_list.print_list()

my_linked_list.partition_list(3)

my_linked_list.print_list()