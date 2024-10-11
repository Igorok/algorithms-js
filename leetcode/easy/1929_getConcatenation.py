from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None]*(n*2)

        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans


def test ():
    params = [
        {
            'input': [1,2,1],
            'output': [1,2,1,1,2,1],
        },
        {
            'input': [1,3,2,1],
            'output': [1,3,2,1,1,3,2,1],
        },

    ]
    solution = Solution()

    for param in params:
        result = solution.getConcatenation(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
