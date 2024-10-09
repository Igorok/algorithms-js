from typing import List
from json import dumps

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start = 0
        end = len(nums) - 1

        arr = sorted(nums)
        r = 0
        while start < end:
            if arr[start] + arr[end] == k:
                r += 1
                start += 1
                end -= 1
            elif arr[start] + arr[end] < k:
                start += 1
            else:
                end -= 1

        return r


def test ():
    params = [
        {
            'input': [[1,2,3,4], 5],
            'output': 2,
        },
        {
            'input': [[3,1,3,4,3], 6],
            'output': 1,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.maxOperations(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
