from typing import List
from collections import deque
from functools import cache
import re

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0]*N

        for i in range(N):
            if nums[i] == 0:
                res[i] = 0
            elif nums[i] > 0:
                id = (i + nums[i]) % N
                res[i] = nums[id]
            else:
                v = abs(nums[i])
                if i - v >= 0:
                    res[i] = nums[i-v]
                else:
                    v = abs(i - v) % N
                    res[i] = nums[(N-v) % N]

        return res




def test ():
    params = [
        {
            'input': [3,-2,1,1],
            'output': [1,1,1,3],
        },
        {
            'input': [-1,4,-1],
            'output': [-1,-1,4],
        },
        {
            'input': [-7,-5,8],
            'output': [8,8,-5],
        },
        {
            'input': [-10],
            'output': [-10],
        },
        {
            'input': [-10,-10],
            'output': [-10,-10],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.constructTransformedArray(nums)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
