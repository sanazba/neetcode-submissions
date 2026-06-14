class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack =[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

#	1.	stack → نگهداری مقادیر اصلی
#	2.	minStack → نگهداری کمترین مقدار تا همان لحظه

#Line 9 	•	اگر minStack خالی نباشد:
#	•	مقدار جدید را با آخرین minimum مقایسه می‌کند
#	•	اگر خالی باشد:
#	•	خود مقدار جدید minimum است
