class HashTable:
    def __init__(self, size = 7):
        # it creates a list as data_map which contains none.
        self.data_map = [None] * size
    
    # Here we will pass the key to determine the address where we store that key value pair 
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord is short form for ordinal, it returns the Ascii number of the letter
            # It is multiplied by 23, as 23 is prime number and we could plug any prime number in here.
            # Any number divided by 7 gives remainder between 0 to 6, which is our address space. 
            # That returned address will be the address to place the key value pair in the hash table
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys

    
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))

print(my_hash_table.keys())

my_hash_table.print_table()
    