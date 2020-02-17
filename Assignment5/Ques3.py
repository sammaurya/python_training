
'''
Design a linked list that supports these ops:

1. Adds an element at the end.
2. Adds an element between the two elements.
3. Deletes an element from the given key.
4. Search an element from the given key.
5. Display the complete linked list.
6. Reverse the linked list.
'''

class linked_list:

    def __init__(self):
        self.list = []

    def insert(self, value):
        self.list.append(value)

    def insert_at(self, index, value):
        left_list = self.list[:index]
        right_list = self.list[index:]
        left_list.append(value)
        left_list.extend(right_list)
        self.list = left_list
    
    def delete(self, key):
        return self.list.remove(key)
    
    def search(self, key):
        if key in self.list:
            return self.list.index(key)
        
    def display(self):
        for value in self.list:
            print(value, end=", ")
        print()
    
    def reverse(self):
        self.list.reverse()


    
l = linked_list()
for value in range(10):
    l.insert(value)
l.display()
l.insert_at(4,10)
l.display()
print(l.search(10))
l.reverse()
l.display()
l.delete(10)
l.display()
    