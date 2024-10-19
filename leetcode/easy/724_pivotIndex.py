from typing import List
from json import dumps

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pos = [None]*len(nums)
        pos[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            pos[i] = pos[i+1] + nums[i]

        pref = [None]*len(nums)
        pref[0] = nums[0]
        if pos[i] == pref[i]:
            return i
        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] + nums[i]
            if pos[i] == pref[i]:
                return i


        return -1


def test ():
    params = [
        {
            'input': [1,7,3,6,5,6],
            'output': 3,
        },
        {
            'input': [1,2,3],
            'output': -1,
        },
        {
            'input': [2,1,-1],
            'output': 0,
        },
        {
            'input': [-1,-1,0,0,-1,-1],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.pivotIndex(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
