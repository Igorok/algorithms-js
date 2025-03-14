from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def minZeroArray_0(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0

        qLen = len(queries)
        nLen = len(nums)

        for i in range(qLen):
            start, end, val = queries[i]
            for j in range(start, end+1):
                nums[j] = max(0, nums[j] - val)

            if sum(nums) == 0:
                return i + 1

        return -1

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0:
            return 0

        qLen = len(queries)
        nLen = len(nums)

        def checkZeroSum(id):
            nonlocal qLen, nLen, nums, queries

            sweepedLine = [0]*nLen

            for i in range(id+1):
                s, e, v = queries[i]
                sweepedLine[s] += v
                if e+1 < nLen:
                    sweepedLine[e+1] -= v

            count = 0
            for i in range(nLen):
                count += sweepedLine[i]
                if count < nums[i]:
                    return False

            return True

        if not checkZeroSum(qLen-1):
            return -1

        s = 0
        e = qLen - 1
        res = e

        while s <= e:
            m = (s + e) // 2
            if checkZeroSum(m):
                res = m
                e = m - 1
            else:
                s = m + 1

        return res+1

'''
[2,0,2], [[0,2,1],[0,2,1],[1,1,3]]

0 0 0
-1 0 0 +1
-2 0 0 +2
-2 -3 +3 +2

2   0  2
-2 -3 +3

-2
-5
-2



---
[4,3,2,1], [[1,3,2],[0,2,1]]

4 3 2 1
4 4 4 4

[1,3,2] - 4 1 0 0
[0,2,1] - 3 0 0 0


[1,3,2]
[0,2,1]





'''



def test ():
    params = [
        {
            'input': [[2,0,2], [[0,2,1],[0,2,1],[1,1,3]]],
            'output': 2,
        },
        {
            'input': [[4,3,2,1], [[1,3,2],[0,2,1]]],
            'output': -1,
        },
        {
            'input': [[0], [[0,0,2],[0,0,4],[0,0,4],[0,0,3],[0,0,5]]],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        nums, queries = param['input']
        result = solution.minZeroArray(nums, queries)
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
