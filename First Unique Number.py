
class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.q = []
        self.map = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self):
        """
        :rtype: int
        """
        while len(self.q)>0 and self.map[self.q[0]]>1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:return self.q[0]

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        if value in self.map:
            self.map[value] += 1
        else:
            self.map[value] = 1
            self.q.append(value)

if __name__ == '__main__':
    solution = FirstUnique([4,1,2,3,3,7,1,7,7])
    print(solution.showFirstUnique())
    solution.add(1)
    print(solution.showFirstUnique())
    solution.add(4)
    print(solution.showFirstUnique())
    solution.add(2)
    print(solution.showFirstUnique())



