from typing import List
from json import dumps
import heapq

class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed = [0]*len(nums)
        robbed[0] = nums[0]
        robbed[1] = nums[1]

        res = max(robbed[0], robbed[1])

        for i in range(2, len(nums)):
            robbed[i] = nums[i]
            for j in range(i-2, -1, -1):
                robbed[i] = max(robbed[i], robbed[j] + nums[i])
                res = max(res, robbed[i])

        print('robbed', robbed)

        return res

def test ():
    params = [
        {
            'input': [1,2,3,1],
            'output': 4,
        },
        {
            'input': [2,7,9,3,1],
            'output': 12,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.rob(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
