class Node:
    def __init__(self, data):
        self.data, self.prev, self.next = data, None, None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head: 
            new_node.next, self.head.prev = self.head, new_node
        self.head = new_node

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next: temp = temp.next
        temp.next, new_node = Node(data), temp.next
        temp.next.prev = temp

    def insert_at_position(self, data, pos):
        if pos == 1: return self.insert_at_beginning(data)
        temp, new_node = self.head, Node(data)
        for _ in range(pos - 2):
            if not temp: return print("Position out of range!")
            temp = temp.next
        if not temp: return print("Position out of range!")
        new_node.next, new_node.prev, temp.next = temp.next, temp, new_node
        if new_node.next: new_node.next.prev = new_node

    def delete_from_beginning(self):
        if self.head: 
            self.head = self.head.next
            if self.head: self.head.prev = None

    def delete_from_end(self):
        if not self.head or not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next: temp = temp.next
        temp.prev.next = None

    def delete_node(self, key):
        temp = self.head
        while temp and temp.data != key: temp = temp.next
        if not temp: return print("Key not found!")
        if temp.prev: temp.prev.next = temp.next
        if temp.next: temp.next.prev = temp.prev
        if temp == self.head: self.head = temp.next

    def display(self, reverse=False):
        temp = self.head
        if not temp: return print("List is empty!")
        if reverse:
            while temp.next: temp = temp.next
            while temp: print(temp.data, end=" <-> "); temp = temp.prev
        else:
            while temp: print(temp.data, end=" <-> "); temp = temp.next
        print("None")

# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    dll.insert_at_position(15, 3)

    print("Doubly Linked List (Forward):")
    dll.display()

    print("Doubly Linked List (Reverse):")
    dll.display(reverse=True)

    dll.delete_from_beginning()
    print("After deleting from beginning:")
    dll.display()

    dll.delete_from_end()
    print("After deleting from end:")
    dll.display()

    dll.delete_node(20)
    print("After deleting node with value 20:")
    dll.display()
