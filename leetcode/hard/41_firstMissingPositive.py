from typing import List
import json
from collections import deque

class Solution:
    def firstMissingPositive_0(self, nums: List[int]) -> int:
        numbersInList = set()
        minNum = float('inf')
        maxNum = float('-inf')
        for num in nums:
            numbersInList.add(num)
            minNum = min(minNum, num)
            maxNum = max(maxNum, num)

        if minNum > 1 or maxNum < 0:
            return 1

        for i in range(1, maxNum + 2):
            if not i in numbersInList:
                return i

        return 0

    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums) + 2
        numbersInList = [-1]*n
        for num in nums:
            if num > 0 and num < n:
                numbersInList[num] = 1

        for i in range(1, n):
            if numbersInList[i] == -1:
                return i

        return 0

'''

1 2 3 4 5


'''

def test ():
    params = [
        {
            'input': [1,2,0],
            'output': 3,
        },
        {
            'input': [3,4,-1,1],
            'output': 2,
        },
        {
            'input': [7,8,9,11,12],
            'output': 1,
        },
        {
            'input': [3,2,-1,1],
            'output': 4,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.firstMissingPositive(param['input'])
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
