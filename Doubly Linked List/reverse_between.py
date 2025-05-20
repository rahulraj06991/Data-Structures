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

    # def print_dll(self):
    #     temp = self.head
    #     while temp is not None:
    #         print(temp.value)
    #         temp = temp.next

    def print_dll(self):
        if(self.head is None):
            print("emty list")
        else:
            temp = self.head
            values = []
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        print(" <-> ".join(values))

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
    
    def reverseBetween(self, x , y):
        if self.length <= 1 or x == y:
            return 
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prev = dummy
        for _ in range(x):
            prev = prev.next
        curr = prev.next
        print(prev.value, curr.value)
        for _ in range(y-x):
            nodeToMove = curr.next
            curr.next = nodeToMove.next
            if nodeToMove.next:
                nodeToMove.next.prev = curr
            nodeToMove.next = prev.next
            prev.next.prev = nodeToMove
            prev.next = nodeToMove
            nodeToMove.prev = prev
            prev.next = nodeToMove
        self.head = dummy.next
        self.head.prev = None

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

my_doubly_linked_list.print_dll()

my_doubly_linked_list.reverseBetween(1,3)

my_doubly_linked_list.print_dll()