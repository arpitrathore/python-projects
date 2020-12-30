class Stack:
    def __init__(self):
        self._stack = []

    def push(self, data):
        self._stack.append(data)
    
    def pop(self):
        data = self._stack[-1]
        del(self._stack[-1])
        return data

    def peek(self):
        return self._stack[-1]

    def display(self):
        print(f"Stack -> {self._stack}")

    def display_size(self):
        print(f"Size - {len(self._stack)}")


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(3)
    stack.display()
    stack.display_size()
    print()

    stack.push(5)
    stack.push(7)
    # [1, 3, 5, 7]
    stack.display()
    stack.display_size()
    print(f"Peek element : {stack.peek()}")
    print()

    print(f"Pop element : {stack.pop()}")
    stack.display()
    stack.display_size()
    print(f"Peek element : {stack.peek()}")
    print()

    print(f"Pop element : {stack.pop()}")
    print(f"Pop element : {stack.pop()}")
    stack.display()