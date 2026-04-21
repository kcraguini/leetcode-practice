class MinStack:

    def __init__(self):
        self.minStack = []
        self.normalStack = []

    def push(self, val: int) -> None:
        self.normalStack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if self.minStack:
            self.minStack.pop()
        if self.normalStack:
            self.normalStack.pop()

    def top(self) -> int:
        return self.normalStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


ms = MinStack()
ms.push(1)
ms.push(2)
ms.push(0)
print(ms.getMin())
ms.pop()
print(ms.top())
print(ms.getMin())
