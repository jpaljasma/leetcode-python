class MinStack:
    def __init__(self):
        self._d = []
        self._md = []

    def push(self, val: int) -> None:
        self._d.append(val)
        if not self._md:
            self._md.append(val)
        else:
            self._md.append(min(self._md[-1], val))

    def pop(self) -> None:
        self._d.pop()
        self._md.pop()

    def top(self) -> int:
        return None if 0 == len(self._d) else self._d[-1]

    def getMin(self) -> int:
        return None if 0 == len(self._md) else self._md[-1]


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(1)
    obj.push(3)
    obj.push(2)
    obj.pop()

    print(obj.top())
    print(obj.getMin())
