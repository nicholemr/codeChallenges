class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'<Node> data: {self.data}'


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.first = None
        self.last = None
        self.min = None

    def __repr__(self):
        return f'<MinStack> first: {self.first} last: {self.last}'

    def push(self, x: int) -> None:

        if not self.first:
            self.first = self.last = Node(x)
            self.min = x
        else:
            newnode = Node(x)
            self.last.next = newnode
            self.last = newnode
            if x < self.min:
                self.min = x

    def pop(self) -> None:
        if self.first == self.last:
            self.first = self.last = self.min = None
            print('MinStack is empty')
        else:
            current = self.first
            newmin = current.data
            while current.next.next:
                current = current.next
                if current.data < newmin:
                    newmin = current.data
            current.next = None
            self.last = current
            self.min = newmin

    def top(self) -> int:
        print(self.last)
        return self.last.data

    def getMin(self) -> int:
        print(self.min)
        return self.min

    def printStack(self):
        current = self.first
        while current:
            print(current)
            current = current.next
        print(self)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.printStack()
obj.pop()
obj.printStack()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.printStack()

# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
