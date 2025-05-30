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

    def swap_nodes(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        #technique 1 ( reused reverse between code)
        # curr = self.head
        # while curr and curr.next:
        #         node_to_move = curr.next
        #         curr.next = node_to_move.next
        #         node_to_move.next = prev.next
        #         prev.next = node_to_move
        #         prev =  curr
        #         curr = curr.next
        #technique 2 
        first = self.head
        while first and first.next:
            second = first.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            first = first.next
        self.head = dummy.next

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.print_list()

my_linked_list.swap_nodes()

my_linked_list.print_list()