class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right


    def contains(self, value):
        temp = self.root
        #print(temp.value)
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
            




mytree = BinarySearchTree()
mytree.insert(4)
mytree.insert(1)
mytree.insert(3)
mytree.insert(2)
mytree.insert(5)
mytree.insert(7)

# print(mytree.root.value)
# print(mytree.root.left.value)
# print(mytree.root.right.value)

print(mytree.contains(5))
print(mytree.contains(7))
print(mytree.contains(9))