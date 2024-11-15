from typing import List
from json import dumps
import heapq

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        binNums = [nums[0]]
        for i in range(1, len(nums)):
            binNums.append(binNums[-1] ^ nums[i])
        print(
            '\n maximumBit', maximumBit, bin(maximumBit),
            '\n binNums', binNums,
        )

        '''
        4 ^ 3 = 7
        100
        11
        111

        '''

        ones = (2 ** maximumBit) - 1
        res = []
        for n in reversed(binNums):
            xor = ones ^ n

            print(
                'ones', ones, bin(ones)[2:],
                'n', n, bin(n)[2:],
                'xor', xor, bin(xor)[2:],
            )

            res.append(xor)

        return res

def test ():
    params = [
        {
            'input': [[0,1,1,3], 2],
            'output': [0,3,2,3],
        },
        {
            'input': [[2,3,4,7], 3],
            'output': [5,2,6,5],
        },
    ]
    solution = Solution()

    for param in params:
        nums, maximumBit = param['input']
        result = solution.getMaximumXor(nums, maximumBit)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
