
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.q.pop(len(self.q)-1)

    def top(self):
        """
        :rtype: int
        """
        return self.q[len(self.q)-1]

    def getMin(self):
        """
        :rtype: int
        """
        p = sorted(self.q)
        return p[0]


if __name__ == '__main__':

    minStack = MinStack()
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())