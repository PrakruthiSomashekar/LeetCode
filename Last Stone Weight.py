
class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) != 1:
            stones = sorted(stones)
            max1 = stones.pop()
            max2 = stones.pop()
            stones.append(max1 - max2)
        return stones[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.lastStoneWeight([2,7,4,1,8,1]))