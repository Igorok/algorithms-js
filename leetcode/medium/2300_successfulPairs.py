from typing import List
from json import dumps
import heapq

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potionArr = sorted(potions.copy())

        def search(val):
            nonlocal potionArr, success

            print(
                'val', val,
                'success', success,
                'potionArr', potionArr,
            )

            start = 0
            end = len(potionArr) - 1

            if potionArr[end] * val < success:
                return 0

            if potionArr[start] * val >= success:
                return len(potionArr)

            while start <= end:
                m = (start + end) // 2
                if success > potionArr[m] * val:
                    start = m + 1
                else:
                    end = m - 1

            print(
                'start', start,
                'end', end,
            )

            return len(potionArr) - start

        res = [
            search(n) for n in spells
        ]

        return res

'''

1 1 1 1 2 3

'''


def test ():
    params = [
        {
            'input': [[5,1,3], [1,2,3,4,5], 7],
            'output': [4,0,3],
        },
        {
            'input': [[3,1,2], [8,5,8], 16],
            'output': [2,0,2],
        },
        {
            'input': [[5,1,3], [1,2,3,4,5, 1,1,1,1,1,], 7],
            'output': [4,0,3],
        },
    ]
    solution = Solution()

    for param in params:
        spells, potions, success = param['input']
        result = solution.successfulPairs(spells, potions, success)
        print(
            'SUCCESS' if dumps(result) == dumps(param['output']) else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
