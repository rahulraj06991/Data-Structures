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

#Tecnique 1 using counter
def is_balanced_parentheses(input):
    balance = 0
    for char in input:
        if char == "(":
            balance+=1
        if char == ")":
            balance-=1
            if balance < 0:
                return False
    return balance == 0

#Technique 2 using stack
# def is_balanced_parentheses(parentheses):
#     stack = Stack()
#     for p in parentheses:
#         if p == '(':
#             stack.push(p)
#         elif p == ')':
#             if stack.is_empty() or stack.pop() != '(':
#                 return False
#     return stack.is_empty()

    

print(is_balanced_parentheses(")("))
    
print(is_balanced_parentheses("(())"))

print(is_balanced_parentheses("))(("))