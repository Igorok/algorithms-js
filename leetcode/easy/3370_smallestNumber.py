from inspect import getgeneratorlocals
from typing import List
import json
from collections import deque, defaultdict
import heapq

nums = []
str = ''
for i in range(30):
    str += '1'
    num = int(str, 2)
    nums.append(int(str, 2))
    if num > 1000:
        break

print('nums', nums)

class Solution:
    def smallestNumber(self, n: int) -> int:
        nums = [1, 3, 7, 15, 31, 63, 127, 255, 511, 1023]

        start = 0
        end = len(nums) - 1
        res = -1

        while start <= end:
            middle = (start + end) // 2
            if nums[middle] < n:
                start = middle + 1
            else:
                res = middle
                end = middle - 1

        return nums[res]

def test ():
    params = [
        {
            'input': 5,
            'output': 7,
        },
        {
            'input': 10,
            'output': 15,
        },
        {
            'input': 3,
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        n = param['input']
        result = solution.smallestNumber(n)
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
