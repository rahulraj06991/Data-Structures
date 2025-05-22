class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def sort_stack(stack):
    #An additional stack
    additional_stack = Stack()
    # While original stack is not empty
    while not stack.is_empty():
        #popping out the top variable from original stack and store it in temp
        temp = stack.pop()
        #while additional stack is not empty and top element of additional stack is greater than temp 
        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            #move the top element from the additional stack to the original stack
            stack.push(additional_stack.pop())
        #add temp to the additional stack
        additional_stack.push(temp)
    #copy the sorted elements from additonal stack to original stack
    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())

my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(2)
my_stack.push(4)

sort_stack(my_stack)

my_stack.print_stack()