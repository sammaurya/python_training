
'''
Design a linked list that supports these ops:

1. Adds an element at the end.
2. Adds an element between the two elements.
3. Deletes an element from the given key.
4. Search an element from the given key.
5. Display the complete linked list.
6. Reverse the linked list.
'''

class Node:
    
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
        self.__next = next_node
    
class LinkedList:

    def __init__(self):
        self.__size = 0
        self.__first = None
        self.__last = None
    
    def add(self, data,front=False, element=None):
        node = Node(data)
        current_node = self.__first

        if self.__size == 0:
            self.__first = node
            self.__last = node
            self.__size += 1

        elif front or self.__first.data == element:
            node.next = self.__first
            self.__first = node
            self.__size += 1 

        elif not front and element == None:
            self.__last.next = node
            self.__last = node
            self.__size += 1 
        
        else:

            while current_node != None:
                previous_node = current_node
                current_node = current_node.next                
                if current_node.data == element:
                    node.next = current_node
                    previous_node.next = node
                    self.__size += 1 
                    return
                else:
                    # raise exception
                    pass
    
    def search(self, data):
        current_node = self.__first
        while current_node != None:
            if current_node.data == data:
                return True
            current_node = current_node.next
        
        return False

    def delete(self,data):
        current_node = self.__first
        previous_node = current_node
        while current_node.data != data and current_node != None:
            previous_node = current_node
            current_node = current_node.next
        
        if current_node.data == data:
            if current_node == self.__first:
                self.__first = current_node.next
                current_node.next = None

            else:
                if current_node == self.__last:
                    self.__last = previous_node
                previous_node.next = current_node.next
                current_node.next = None
            self.__size -= 1
        else:
            pass
            #raise exception

    def reverse(self):
        current_node = self.__first
        previous_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        
        self.__last = self.__first
        self.__first = previous_node

    def display(self):
        node_list = []
        current_node = self.__first
        
        while current_node != None:
            node_list.append(current_node.data)
            current_node = current_node.next
    
        print(node_list)

        return node_list
    
    def length(self):
        return self.__size


# Create LinkedList Object
linked_list = LinkedList()

# add 1 at the end of the linked list
linked_list.add(1)
# add 2 at the front of the linked list
linked_list.add(2,front=True)
# add 3 before element 1 in the linked list
linked_list.add(3,element=1)
# add 4 at the end of the linked list
linked_list.add(4)

# display and return list of elements in the linked list
linked_list.display()
# search element 4 return true here
print(linked_list.search(4))
# delete element 4
linked_list.delete(4)
# search element 4 return false here
print(linked_list.search(4))
# display linked list
linked_list.display()
# reverse the linked list
linked_list.reverse()
# display linked list
linked_list.display()
# returns length of the linked list
print(linked_list.length())
