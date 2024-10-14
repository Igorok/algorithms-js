from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r = 0
        subsets = []
        for i in range(1, len(nums)):



        return r


def test ():
    params = [
        {
            'input': [1,3],
            'output': 6,
        },
        {
            'input': [5,1,6],
            'output': 28,
        },
        {
            'input': [3,4,5,6,7,8],
            'output': 480,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.subsetXORSum(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
