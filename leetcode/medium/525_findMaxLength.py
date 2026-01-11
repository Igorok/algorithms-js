from typing import List
import heapq
import math
from collections import defaultdict, deque

class Solution_0:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N):
            s = 0
            for j in range(i, N):
                s += nums[j]
                length = j+1-i
                if s*2 == length:
                    res = max(res, length)

        return 0 if res == 1 else res


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {
            0: -1,
        }
        sumOfNums = 0
        res = 0
        for i in range(N):
            n = nums[i]
            sumOfNums += 1 if n == 1 else -1
            if sumOfNums not in memo:
                memo[sumOfNums] = i
            else:
                res = max(res, i - memo[sumOfNums])

        return res

'''
0,1,1,1,1,1,0,0,0
0 1 2 3 4 5 5 5 5

0 0 0 1 1 1 1 1 0
0 0 0 1 2 3 4 5 5

 0  0  0  1  1  1  1  1  0
-1 -2 -3 -2 -1  0  1  2  1

 0  1  1  1  1  1  0  0  0
-1  0  1  2  3  4  3  2  1
'''

def test ():
    params = [
        {
            'input': [0,1],
            'output': 2,
        },
        {
            'input': [0,1,0],
            'output': 2,
        },
        {
            'input': [0,1,1,1,1,1,0,0,0],
            'output': 6,
        },
        {
            'input': [0,1,0,1,0,1],
            'output': 6,
        },
        {
            'input': [0],
            'output': 0,
        },
        {
            'input': [1],
            'output': 0,
        },
        {
            'input': [0,1,1],
            'output': 2,
        },
        {
            'input': [1,1,0],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.findMaxLength(nums)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
