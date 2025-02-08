from typing import List
from json import dumps
import heapq
from collections import deque

class Solution:
    def check_0(self, nums: List[int]) -> bool:
        n = len(nums)
        sortedNums = sorted(nums)
        idsByNums = { num: i for i, num in enumerate(sortedNums) }

        alarm = 0
        for i in range(n-1):
            id = idsByNums[nums[i]]
            if id + 1 == n or nums[i+1] != sortedNums[id + 1]:
                alarm += 1
                if alarm > 1:
                    return False
        return True

    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sortedNums = sorted(nums)

        for i in range(n-1):
            if nums[i] > nums[i+1]:
                left = nums[i+1:]
                right = nums[:i+1]
                return sortedNums == (left+right)

        return True



def test ():
    params = [
        {
            'input': [3,4,5,1,2],
            'output': True,
        },
        {
            'input': [2,1,3,4],
            'output': False,
        },
        {
            'input': [1,2,3],
            'output': True,
        },
        {
            'input': [1,1,1],
            'output': True,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.check(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
