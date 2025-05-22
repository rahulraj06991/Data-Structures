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

#technique 1, iterating over the length of stack        
def reverse_string(input):
    output = ''
    stack = Stack()
    for char in input:
        stack.push(char)
    for i in range(len(stack.stack_list)-1, -1, -1):
        output+=stack.stack_list[i]
    return output

#technique 2, using pop method as stack follows LIFO
def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    for char in string:
        stack.push(char)
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string
 

print(reverse_string("hello"))
