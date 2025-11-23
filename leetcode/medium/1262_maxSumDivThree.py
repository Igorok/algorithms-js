from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache
import math

class Solution_0:
    def maxSumDivThree(self, nums: List[int]) -> int:
        rem1 = []
        rem2 = []

        res = 0

        for num in nums:
            rem = num % 3
            if rem == 0:
                res += num
            elif rem == 1:
                rem1.append(num)
            else:
                rem2.append(num)


        rem1.sort(key = lambda x: -x)
        rem2.sort(key = lambda x: -x)
        N1 = len(rem1)
        N2 = len(rem2)

        @lru_cache
        def dfs(id1, id2):
            res = 0

            if N1 - id1 > 0 and N2 - id2 > 0:
                res = max(res, rem1[id1] + rem2[id2] + dfs(id1+1, id2+1))
            if N1 - id1 > 2:
                res = max(res, rem1[id1] + rem1[id1+1] + rem1[id1+2] + dfs(id1+3, id2))
            if N2 - id2 > 2:
                res = max(res, rem2[id2] + rem2[id2+1] + rem2[id2+2] + dfs(id1, id2+3))

            return res

        return res + dfs(0,0)



class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        rem1 = []
        rem2 = []

        res = 0

        for num in nums:
            rem = num % 3
            if rem == 0:
                res += num
            elif rem == 1:
                rem1.append(num)
            else:
                rem2.append(num)


        rem1.sort(key = lambda x: -x)
        rem2.sort(key = lambda x: -x)
        N1 = len(rem1)
        N2 = len(rem2)

        if N1 + N2 == 0:
            return res

        rem = (N1 + 2*N2) % 3

        if rem == 0:
            return res + sum(rem1) + sum(rem2)

        if rem == 1:
            if N2 > 1 and rem1[-1] >= rem2[-1] + rem2[-2]:
                return res + sum(rem1) + sum(rem2[:N2-2])
            else:
                return res + sum(rem1[:N1-1]) + sum(rem2)

        # rem == 2
        if N2 == 0:
            return res + sum(rem1[:N1-2])

        if N1 == 0:
            return res + sum(rem2[:N2-1])

        if N1 > 1:
            if rem1[-1] + rem1[-2] >= rem2[-1]:
                return res + sum(rem1) + sum(rem2[:N2-1])
            else:
                return res + sum(rem1[:N1-2]) + sum(rem2)
        else:
            return res + sum(rem1) + sum(rem2[:N2-1])

        return res
'''

[2,6,2,2,7]

6
7
2 2 2



'''



def test ():
    params = [
        {
            'input': [2,6,2,2,7],
            'output': 15,
        },
        {
            'input': [3,1,2],
            'output': 6,
        },
        {
            'input': [3,6,5,1,8],
            'output': 18,
        },
        {
            'input': [4],
            'output': 0,
        },
        {
            'input': [1,2,3,4,4],
            'output': 12,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.maxSumDivThree(nums)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
