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
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True

    def pop(self):
        if self.length == 0:
            return None
        pre = self.head
        temp = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        #print(pre.value, temp.value)
        self.length-=1
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend (self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:    
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head  = self.head.next
        temp.next = None
        self.length-=1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        #Manual Approach
        # if index < 0 or index >= self.length:
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        # new_node = Node(value)
        # temp = self.head
        # pre = self.head
        # for _ in range(index):
        #     pre = temp
        #     temp = temp.next
        # #print(pre.value, temp.value)
        # pre.next = new_node
        # new_node.next = temp
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1 
        return True
    
    def remove(self, index):
        if index < 0 or index >=self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        #Manual Approach
        # temp = self.head
        # pre = self.head
        # for _ in range(index):
        #     pre = temp
        #     temp = temp.next
        # print(pre.value, temp.value)
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next= None
        self.length-=1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after 
        

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)

# my_linked_list.append(2)

# my_linked_list.append(3)

# my_linked_list.append(1)

#my_linked_list.print_list()

#my_linked_list.print_list()
    
# print(my_linked_list.pop().value)

#print(my_linked_list.pop_first())

#print(my_linked_list.get(2))

#print(my_linked_list.set(2,4))

#my_linked_list.set_value(2,4)

#print(my_linked_list.insert(4,9))

#my_linked_list.remove(1)

# my_linked_list.reverse()

my_linked_list.print_list()

