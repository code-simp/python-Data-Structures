class Queue(object):
    def __init__(self):
        self.items = []

    def enque(self,data):
        self.items.insert(0,data)

    def deque(self):
        if not self.items == []:
            temp = self.items[-1]
            self.items.remove(self.items[-1])
            return temp

    def show(self):
        result = ''
        for i in self.items:
            result += (' - ' + str(i))
        print(result)

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)