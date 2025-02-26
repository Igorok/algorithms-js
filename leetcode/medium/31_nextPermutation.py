from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        lastMaxId = 0
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                lastMaxId = i

        if lastMaxId == 0:
            start = 0
            end = length-1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return nums

        leftId = lastMaxId-1
        rightId = lastMaxId
        for i in range(lastMaxId+1, length):
            if nums[i] > nums[leftId] and nums[i] < nums[rightId]:
                rightId = i

        nums[leftId], nums[rightId] = nums[rightId], nums[leftId]
        sortedPart = sorted(nums[lastMaxId:])

        j = 0
        for i in range(lastMaxId, length):
            nums[i] = sortedPart[j]
            j += 1

        return nums



def test ():
    params = [
        {
            'input': [1,2,3],
            'output': [1,3,2],
        },
        {
            'input': [3,2,1],
            'output': [1,2,3],
        },
        {
            'input': [1,1,5],
            'output': [1,5,1],
        },
        {
            'input': [1,1,5,3,2,1],
            'output': [1,2,1,1,3,5],
        },
        {
            'input': [4,2,1,3,2],
            'output': [4,2,2,1,3],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.nextPermutation(param['input'])
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
