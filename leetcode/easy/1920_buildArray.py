from typing import List
from json import dumps

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [None]*len(nums)
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        return res


def test ():
    params = [
        {
            'input': [0,2,1,5,3,4],
            'output': [0,1,2,4,5,3],
        },
        {
            'input': [5,0,1,2,3,4],
            'output': [4,5,0,1,2,3],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.buildArray(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
