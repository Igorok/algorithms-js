from typing import List
from collections import deque, defaultdict
from functools import cache
import re

class Solution:
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
