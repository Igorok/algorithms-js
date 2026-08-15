from typing import List
from json import dumps
from collections import deque
import heapq


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        N = len(nums)
        bits = [0]*33

        for num in nums:
            n = num
            i = 0
            while n > 0:
                r = n % 2
                if r != 0:
                    bits[i] += 1
                n = n // 2
                i += 1

        allZeros = True
        for cnt in bits:
            if cnt > 0:
                allZeros = False
            if cnt % 2 != 0:
                return N

        if allZeros:
            return 0

        return N-1



def test ():
    params = [
        {
            'input': [1,2,3],
            'output':  2,
        },
        {
            'input': [2,3,4],
            'output':  3,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.longestSubsequence(nums)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
