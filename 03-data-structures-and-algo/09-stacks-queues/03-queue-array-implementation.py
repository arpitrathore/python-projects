class Queue:
    def __init__(self):
        self._queue = []

    def enqueue(self, data):
        self._queue.append(data)
    
    def dequeue(self):
        data = self._queue[0]
        del(self._queue[0])
        return data

    def peek(self):
        return self._queue[0]

    def display(self):
        print(f"Queue -> {self._queue}")

    def display_size(self):
        print(f"Size - {len(self._queue)}")


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(3)
    queue.display()
    queue.display_size()
    print()
    

    queue.enqueue(5)
    queue.enqueue(7)
    # [1, 3, 5, 7]
    queue.display()
    queue.display_size()
    print()
    

    print(f"Peek element : {queue.peek()}")
    print()
    print(f"Dequeue element : {queue.dequeue()}")
    queue.display()
    queue.display_size()
    print(f"Peek element : {queue.peek()}")
    print()

    print(f"Dequeue element : {queue.dequeue()}")
    print(f"Dequeue element : {queue.dequeue()}")
    queue.display()
    queue.display_size()