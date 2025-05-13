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

    #This function has two loops (nested loop) and has complexity of O(n^2)
    def remove_duplicates(self):
        current = self.head
        runner = self.head
        while current:
            runner = current
            while runner.next:
                if current.value == runner.next.value:
                    runner.next = runner.next.next
                    self.length-=1
                else:
                    runner = runner.next
                current = current.next
    
    #Solution to the problem using set and has complexity of O(n)
    def remove_duplicates(self):
        curr = self.head
        prev = None
        uniqueItem = set()
        while curr is not None:
            if curr.value in uniqueItem:
                prev.next = curr.next
                self.length-=1
            else:
                uniqueItem.add(curr.value)
                prev = curr
            curr = curr.next
