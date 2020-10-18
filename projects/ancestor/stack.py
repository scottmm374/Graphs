class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def __str__(self):
        return f'{self.stack}'

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        else:
            return None


class Queue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def __str__(self):
        return f'{self.queue}'

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1
        return value

    def dequeue(self):
        if self.size >= 1:
            value = self.queue.pop(0)
            self.size -= 1
            return value

        else:
            return None
