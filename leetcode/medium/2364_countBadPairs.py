from typing import List
from json import dumps
import heapq
from collections import deque


class Solution:
    def countBadPairs_0(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if j - i != nums[j] - nums[i]:
                    res += 1
        return res


    def countBadPairs_1(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        idValDiff = {}
        totalPairs = 0

        for i in range(n):
            totalPairs += i

            diff = nums[i] - i
            v = idValDiff.get(diff, 0)
            v += 1
            idValDiff[diff] = v

        validPairs = 0
        idValUsed = {}
        for i in range(n):
            diff = nums[i] - i
            u = idValUsed.get(diff, 0)
            u += 1
            idValUsed[diff] = u
            validPairs += (idValDiff[diff] - idValUsed[diff])

        return totalPairs - validPairs

    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        idValDiff = {}
        totalPairs = 0
        validPairs = 0
        for i in range(n):
            totalPairs += i

            diff = nums[i] - i
            v = idValDiff.get(diff, 0)
            validPairs += v
            v += 1
            idValDiff[diff] = v

        return totalPairs - validPairs

'''

[1,2,3,4,5]

1,2,3,4,5
0 1 2 3 4

pairs:
4 + 3 + 2 + 1 = 10

j - i == nums[j] - nums[i]
j - nums[j] == nums[i] - i

1,2,3,4,5
1 1 1 1 1



1,2,100,101,5

'''



def test ():
    params = [
        {
            'input': [4,1,3,3],
            'output': 5,
        },
        {
            'input': [1,2,3,4,5],
            'output': 0,
        },
        {
            'input': [1,2,100,101,5],
            'output': 6,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.countBadPairs(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
