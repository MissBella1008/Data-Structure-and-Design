class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        self.head = new_node

    def delete(self, key):
        if self.head is None:
            return
        
        temp = self.head
        prev = None
        while temp.next != self.head:
            if temp.data == key:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
        
        if temp.data == key:
            if prev:
                prev.next = self.head
            else:
                self.head = None

    def display(self):
        nodes = []
        temp = self.head
        if self.head:
            while True:
                nodes.append(str(temp.data))
                temp = temp.next
                if temp == self.head:
                    break
        print(" -> ".join(nodes))

# Example Usage
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.prepend(0)
    cll.display()
    cll.delete(2)
    cll.display()
