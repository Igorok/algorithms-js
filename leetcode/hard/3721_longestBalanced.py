from typing import List
from collections import deque, defaultdict
from functools import cache
import re

class Solution_0:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            if res >= N-i:
                break

            odd = 0
            even = 0
            values = set()

            for j in range(i, N):
                n = nums[j]
                if (n % 2) == 1:
                    if n not in values:
                        values.add(n)
                        even += 1
                else:
                    if n not in values:
                        values.add(n)
                        odd += 1

                if even == odd:
                    res = max(res, j-i+1)

        return res

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.minVal = [0] * (4*n)
        self.maxVal = [0] * (4*n)
        self.lazy = [0] * (4*n)

    def __push(self, id):
        if self.lazy[id] == 0:
            return

        self.lazy[2*id] += self.lazy[id]
        self.lazy[2*id + 1] += self.lazy[id]

        self.minVal[2*id] += self.lazy[id]
        self.minVal[2*id + 1] += self.lazy[id]

        self.maxVal[2*id] += self.lazy[id]
        self.maxVal[2*id + 1] += self.lazy[id]

        self.lazy[id] = 0


    def update(self, nodeId, nodeLeft, nodeRight, queryLeft, queryRight, val):
        if queryLeft > queryRight:
            return

        if nodeLeft == queryLeft and nodeRight == queryRight:
            self.lazy[nodeId] += val
            self.minVal[nodeId] += val
            self.maxVal[nodeId] += val
        else:
            self.__push(nodeId)
            middle = (nodeLeft + nodeRight) // 2

            self.update(2*nodeId, nodeLeft, middle, queryLeft, min(queryRight, middle), val)
            self.update(2*nodeId + 1, middle+1, nodeRight, max(queryLeft, middle+1), queryRight, val)

            self.minVal[nodeId] = min(self.minVal[nodeId*2], self.minVal[nodeId*2 + 1])
            self.maxVal[nodeId] = max(self.maxVal[nodeId*2], self.maxVal[nodeId*2 + 1])


    def findZero(self, nodeId, nodeLeft, nodeRight, left, right):
        if left > right or self.minVal[nodeId] > 0 or self.maxVal[nodeId] < 0:
            return -1

        if nodeLeft == nodeRight:
            return nodeLeft if self.minVal[nodeId] == 0 else -1

        self.__push(nodeId)

        middle = (nodeLeft + nodeRight) // 2
        res = self.findZero(2*nodeId, nodeLeft, middle, left, min(right, middle))
        if res != -1:
            return res

        return self.findZero(2*nodeId + 1, middle+1, nodeRight, max(left, middle+1), right)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        N = len(nums)
        st = SegmentTree(N)
        lastPos = {}
        res = 0

        for i in range(N):
            val = nums[i]

            prevId = lastPos.get(val, -1)
            left = prevId + 1
            right = i

            change = 1 if (val % 2) == 0 else -1
            st.update(1, 0, N-1, left, right, change)

            zeroId = st.findZero(1, 0, N-1, 0, right)
            if zeroId > -1:
                res = max(res, right - zeroId + 1)

            lastPos[val] = i

        return res

'''
1 2 3 2 5 2 2 2
2 1 3 5 2 4 2 4


'''

def test ():
    params = [
        {
            'input': [2,5,4,3],
            'output': 4,
        },
        {
            'input': [3,2,2,5,4],
            'output': 5,
        },
        {
            'input': [1,2,3,2],
            'output': 3,
        },
        {
            'input': [2, 1, 3, 5, 2, 4, 2, 4],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.longestBalanced(nums)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
