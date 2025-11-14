from typing import List
import json
from collections import deque, defaultdict
import heapq
from functools import lru_cache

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rightSum = [[0, 0] for i in range(n+1)]
        for i in range(n-1, -1, -1):
            num = nums[i]
            rightSum[i][0] = rightSum[i+1][0]
            rightSum[i][1] = rightSum[i+1][1]
            rightSum[i][num] += 1

        val = rightSum[0][0]
        res = [n]

        leftSum = [[0, 0] for i in range(n+1)]
        for i in range(n):
            r = leftSum[i-1][0] + rightSum[i][1]
            if r == val:
                res.append(i)
            elif r > val:
                val = r
                res = [i]

            num = nums[i]
            leftSum[i][0] = leftSum[i-1][0]
            leftSum[i][1] = leftSum[i-1][1]
            leftSum[i][num] += 1

        return res




def test ():
    params = [
        {
            'input': [0,0,1,0],
            'output': [2, 4],
        },
        {
            'input': [0,0,0],
            'output': [3],
        },
        {
            'input': [1,1],
            'output': [0],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.maxScoreIndices(nums)
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
