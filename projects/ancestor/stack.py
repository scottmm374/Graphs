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
