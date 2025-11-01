from typing import List
import json
from collections import deque, defaultdict


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stack = []

        def canPop(id):
            leftLength = len(stack)
            rightLength = n - id

            if stack and stack[-1] > nums[id] and leftLength - 1 + rightLength >= k:
                return True
            return False

        for i in range(n):
            while canPop(i):
                stack.pop()

            if len(stack) < k:
                stack.append(nums[i])

        return stack

'''
3 5 2 6 1


'''

def test ():
    params = [
        {
            'input': [[3,5,2,6], 2],
            'output': [2,6],
        },
        {
            'input': [[2,4,3,3,5,4,9,6], 4],
            'output': [2,3,3,4],
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.mostCompetitive(nums, k)
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
