from typing import List
from json import dumps

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = -1
        length = 0

        start = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero == -1:
                    zero = i
                else:
                    length = max(length, i - start - 1)
                    start = zero + 1
                    zero = i
            if i == len(nums) - 1:
                length = max(length, i - start)

        return length


def test ():
    params = [
        {
            'input': [1,1,0,1],
            'output': 3,
        },
        {
            'input': [0,1,1,1,0,1,1,0,1],
            'output': 5,
        },
        {
            'input': [1,1,1],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.longestSubarray(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
