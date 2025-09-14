from typing import List
import json
from collections import deque, defaultdict
import heapq
import math

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        middle = math.floor(n / 2)
        res = 0

        for num in nums:
            res += abs(num - nums[middle])

        return res

'''
1
2
9
10

0 1 2 3 4 5 6 7 8 9 10 11
* *
* * *
* * * * * * * * * *
* * * * * * * * * * *

0 1 2 3 4 5 6 7 8 9 10 11
* * + + + + +
* * * + + + +
* * * * * * * - - -
* * * * * * * - - - -

(1 + 2 + 9 + 10) / 4

0 1 2 3 4 5 6 7 8 9 10
+ +
+ + +
+ + + + + + + + + + +
+ + + + + + + + + + +
+ + + + + + + + + + +

(1 + 2+ 10 + 10+ 10)/5
7

7-1 + 7-2 + 10-7 + 10-7 + 10-7 = 20
10-1 + 10-2 = 17


'''

def test ():
    params = [
        {
            'input': [1,2,3],
            'output': 2,
        },
        {
            'input': [1,10,2,9],
            'output': 16,
        },
        {
            'input': [1,2,10,10,10],
            'output': 17,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.minMoves2(nums)
        correct = result == param['output']

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
