from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxCount = -1
        maxNum = -1

        for num in nums:
            count[num] += 1
            if count[num] > maxCount:
                maxNum = num
                maxCount = count[num]


        countNum = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == maxNum:
                countNum += 1

            if countNum * 2 > (i + 1):
                rightCount = maxCount - countNum
                rightLength = n - i - 1
                return i if rightCount * 2 > rightLength else -1

        return -1

'''

1 1 2 2 2 1 1 1


'''

def test ():
    params = [
        {
            'input': [1,2,2,2],
            'output': 2,
        },
        {
            'input': [2,1,3,1,1,1,7,1,2,1],
            'output': 4,
        },
        {
            'input': [3,3,3,3,7,2,2],
            'output': -1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param['input']
        result = solution.minimumIndex(nums)
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
