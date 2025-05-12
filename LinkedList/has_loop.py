#has loop question, where we need to identify a linked list is circular linked list
#Used Floyd's cycle finding algorithm (also known as "tortoise and the hare" algorithm), Slow and fast pointer 
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
    
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast.next is not None and fast is not None:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False
        
    