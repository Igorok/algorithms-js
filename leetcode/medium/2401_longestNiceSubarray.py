from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        res = 1
        start = 0
        acc = nums[start]
        for i in range(1, n):
            if acc & nums[i] == 0:
                acc |= nums[i]
                res = max(res, i - start + 1)
            else:
                while acc & nums[i] != 0:
                    acc ^= nums[start]
                    start += 1
                acc |= nums[i]


        return res


'''

1   000001
3   000011
8   001000
48  110000
10  001010


'''


def test ():
    params = [
        {
            'input': [1,3,8,48,10],
            'output': 3,
        },
        {
            'input': [3,1,5,11,13],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.longestNiceSubarray(nums)
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
