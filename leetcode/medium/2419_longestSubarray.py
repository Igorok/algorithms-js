from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = 0
        maxVal = 0
        maxLength = 0

        for n in nums:
            if n > maxVal:
                maxVal = n
                length = 1
                maxLength = 1
            elif n == maxVal:
                length += 1
            else:
                maxLength = max(maxLength, length)
                length = 0

        maxLength = max(maxLength, length)

        return maxLength


def test ():
    params = [
        {
            'input': [1,2,3,3,2,2],
            'output': 2,
        },
        {
            'input': [1,2,3,4],
            'output': 1,
        },
        {
            'input': [311155,311155,311155,311155,311155,311155,311155,311155,201191,311155],
            'output': 8,
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
