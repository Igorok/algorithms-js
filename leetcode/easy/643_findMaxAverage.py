from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        val = 0
        for i in range(k):
            val += nums[i]
        res = val

        for i in range(k, len(nums)):
            val = val + nums[i] - nums[i - k]
            res = max(val, res)

        return res / k


def test ():
    params = [
        {
            'input': [[1,12,-5,-6,50,3], 4],
            'output': 12.75000,
        },
        {
            'input': [[5], 1],
            'output': 5.00000,
        },
        {
            'input': [[0,4,0,3,2], 1],
            'output': 4.00000,
        },
    ]
    solution = Solution()

    for param in params:
        nums, k = param['input']
        result = solution.findMaxAverage(nums, k)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
