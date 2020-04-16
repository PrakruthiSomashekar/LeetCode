import collections

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.



class Solution(object):
    def minDominoRotations(self, A, B):
        count = 0
        freq1 = collections.Counter(A)
        freq2 = collections.Counter(B)
        isA = True
        num = -1

        for key in freq1:
            if freq2.get(key)!=None and ((freq1.get(key)+freq2.get(key)) >= len(A)):
                num = key
                break

        if num == -1:
            return num
        if freq2.get(num) > freq1.get(num):
            isA = False

        for i in range(len(A)):
            if A[i] != num and B[i] != num:
                return -1
            if isA:
                if A[i] != num and B[i] == num:
                    count += 1
            else:
                if B[i] != num and A[i] == num:
                    count += 1
        return count


if __name__ == '__main__':
    A = [2]
    B = [1]
    solution = Solution()
    print(solution.minDominoRotations(A,B))