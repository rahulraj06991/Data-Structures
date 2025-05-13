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

    #technique 1 
    def binary_to_decimal(self):
        curr = self.head
        num = 0
        while curr is not None:
            num =num*2
            if (curr.value == 1):   
                num +=1
            curr = curr.next
        return num
    
    #technique 2 alternative of option 1
    def binary_to_decimal(self):
        num = 0
        curr = self.head
        while curr:
            num = num * 2 + curr.value
            curr = curr.next
        return num

    #technique 3 with inbuilt function:
    def binary_to_decimal(self):
        if self.head is None:
            return 0
        curr = self.head
        binary_str = ""
        while curr:
            binary_str += str(curr.value)
            curr = curr.next
        return int(binary_str, 2)

    
    
my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(0)
my_linked_list.append(1)

print(my_linked_list.binary_to_decimal())