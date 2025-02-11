from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)



        return 0

def test ():
    params = [
        {
            'input': [2, [2,4,1]],
            'output': 2,
        },
        {
            'input': [2, [3,2,6,5,0,3]],
            'output': 7,
        },
    ]
    solution = Solution()

    for param in params:
        k, prices = param['input']
        result = solution.maxProfit(k, prices)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
