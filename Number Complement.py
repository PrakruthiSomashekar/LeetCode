# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

class Solution(object):
    def findComplement(self, num):
        binary = list(bin(num))
        binary.pop(0)
        binary.pop(0)
        for i in range(len(binary)):
            if binary[i] == '1':
                binary[i] = '0'
            else:
                binary[i] = '1'

        return int("".join(binary),2)

if __name__ == '__main__':
    solution = Solution()
    print(solution.findComplement(4))