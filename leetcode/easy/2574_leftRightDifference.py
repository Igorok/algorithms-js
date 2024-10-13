from typing import List
from json import dumps


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [0] * length
        right = [0] * length

        for i in range(1, length):
            left[i] = nums[i-1]+left[i-1]

        for i in range(length - 2, -1, -1):
            right[i] = right[i+1] + nums[i+1]

        return [abs(left[i] - right[i]) for i in range(length)]


def test ():
    params = [
        {
            'input': [10,4,8,3],
            'output': [15,1,11,22],
        },
        {
            'input': [1],
            'output': [0],
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.leftRightDifference(param['input'])
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
