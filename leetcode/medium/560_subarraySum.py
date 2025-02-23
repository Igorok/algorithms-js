from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def subarraySum_0(self, nums: List[int], k: int) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            s = nums[i]
            if s == k:
                res += 1
            for j in range(i+1, n):
                s += nums[j]
                if s == k:
                    res += 1

        return res

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        s = 0
        res = 0
        for num in nums:
            s += num
            diff = s - k
            res += prefix[diff]
            prefix[s] += 1

        return res

'''
1 1 1 3
1 2 3 6

'''


def test ():
    params = [
        {
            'input': [[1,1,1,3], 3],
            'output': 2,
        },
        {
            'input': [[0,0,0,3,0], 3],
            'output': 8,
        },
        {
            'input': [[1,1,1], 2],
            'output': 2,
        },
        {
            'input': [[1,2,3], 3],
            'output': 2,
        },
        {
            'input': [[1,2,3,-1,4], 3],
            'output': 3,
        },
        {
            'input': [[1], 0],
            'output': 0,
        },

    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.subarraySum(nums, k)
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
