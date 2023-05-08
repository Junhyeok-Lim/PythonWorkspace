class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        new_node = Node(data)

        if previous_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node_to_delete):

        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None

        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data


    def pop_left(self):
        data = self.head.data

        if self.head is self.tail:
            self.head = None
            self.tail = None
        
        else:
            self.head = self.head.next

        return data

    def delete_after(self, previous_node):
        data = previous_node.next.data

        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        
        else:
            previous_node.next = previous_node.next.next

    def insert_after(self, previous_node, data):
        new_node = Node(data)

        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = previous_node.next
            previous_node.next = new_node
        
        return data

    def find_node_at(self, index):
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else :
            self.tail.next = new_node
            self.tail = new_node
    
    def __str__(self):
        
        res_str = "|"
        iterator = self.head
        
        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next  

        return res_str

my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

node_2 = my_list.find_node_at(2)
my_list.insert_after(node_2, 6)

print(my_list)

# node_2 = my_list.find_node_at(2)
# my_list.delete_after(node_2)

# print(my_list)

# second_to_last_node = my_list.find_node_at(2)
# print(my_list.delete_after(second_to_last_node))

# print(my_list)