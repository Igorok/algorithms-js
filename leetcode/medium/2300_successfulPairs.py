from typing import List
from json import dumps
import heapq

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        return []

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
