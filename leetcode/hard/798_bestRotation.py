from typing import List
from json import dumps
import heapq

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        return 0



'''

[1,3,0,2,4],


'''

def test ():
    params = [
        {
            'input': [2,3,1,4,0],
            'output': 3,
        },
        {
            'input': [1,3,0,2,4],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.trapRainWater(param['input'])
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )

if __name__ == '__main__':
    test()
