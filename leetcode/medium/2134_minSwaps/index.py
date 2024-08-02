from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numsLen = len(nums)
        windowSize = sum(nums)
        if windowSize == numsLen or windowSize == 0:
            return 0

        left = 0
        right = windowSize - 1
        maxWindowSum = currentSum = sum(nums[0:windowSize])

        for i in range(numsLen):
            currentSum = currentSum - nums[left] + nums[(right + 1) % numsLen]
            left = (left + 1) % numsLen
            right = (right + 1) % numsLen
            maxWindowSum = max(maxWindowSum, currentSum)

        return windowSize - maxWindowSum


def test ():
    params = [
        {
            'input': [0,1,0,1,1,0,0],
            'output': 1,
        },
        {
            'input': [0,1,1,1,0,0,1,1,0],
            'output': 2,
        },
        {
            'input': [1,1,0,0,1],
            'output': 0,
        },
        {
            'input': [0,0,1,0,1,0,0],
            'output': 1,
        },
        {
            'input': [0,1,0,0,0,0,1,0],
            'output': 1,
        },
        {
            'input': [0,1,1,1,0,0,1,1,0,0,0,1,1],
            'output': 2,
        },
        {
            'input': [0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,1,1],
            'output': 3,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.minSwaps(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
