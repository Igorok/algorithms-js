from typing import List
from collections import defaultdict


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        leftEnd = -1

        left = 0
        for right in range(1, n):
            if nums[right] > nums[right-1]:
                if right - left + 1 == k*2:
                    return True
                if right - left + 1 == k and leftEnd != -1 and left - leftEnd == 1:
                    return True
            else:
                if right - left >= k:
                    leftEnd = right - 1
                left = right

        if n - left == k and leftEnd != -1 and left - leftEnd == 1:
            return True

        return False


def test ():
    params = [
        {
            'input': [[19,5], 1],
            'output': True,
        },
        {
            'input': [[2,5,7,8,9,2,3,4,3,1], 3],
            'output': True,
        },
        {
            'input': [[1,2,3,4,4,4,4,5,6,7], 5],
            'output': False,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.hasIncreasingSubarrays(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
