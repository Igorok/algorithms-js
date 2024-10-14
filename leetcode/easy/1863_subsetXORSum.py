from typing import List
from json import dumps


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.subsets = []

        def rec(i, arr):
            if i == len(nums):
                if len(arr):
                    self.subsets.append(arr)
                return
            a1 = arr.copy()
            a1.append(nums[i])
            a2 = arr.copy()
            rec(i+1, a1)
            rec(i+1, a2)

        rec(0, [])

        print('self.subsets', self.subsets)

        def getXOR(arr):
            xor = 0
            for v in arr:
                xor = xor ^ v
            return xor

        s = 0
        for arr in self.subsets:
            xor = getXOR(arr)
            s += xor

        return s


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
