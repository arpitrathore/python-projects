class Node:
    """[Class representing a linked list node]
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """[Class representing singly linked list]
    """
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, data):
        self.size += 1
        if not self.head:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def insert_last(self, data):
        self.size += 1
        if not self.head:
            self.head = Node(data)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            
            node = Node(data)
            current_node.next = node

    def remove(self, value) :
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            self.size -= 1
        else:
            current_node = self.head
            while current_node.next:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    self.size -= 1
                    break
                current_node = current_node.next

        
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("NULL")

    def display_size(self) :
        print(f"Size - {self.size}")




if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_first(1)
    ll.insert_first(3)
    ll.display_size()
    ll.display()

    ll.insert_first(5)
    ll.insert_last(7)
    ll.insert_last(9)
    ll.display_size()
    ll.display()

    ll.remove(1)
    print("\nAfter removing 1")
    ll.display_size()
    ll.display()

    ll.remove(5)
    print("\nAfter removing 5")
    ll.display_size()
    ll.display()

    ll.remove(9)
    print("\nAfter removing 9")
    ll.display_size()
    ll.display()

    ll.remove(51)
    print("\nAfter removing 51")
    ll.display_size()
    ll.display()

   