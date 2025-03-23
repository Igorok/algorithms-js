from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        sequenceses = 0
        current = set()

        for num in rolls:
            current.add(num)
            if len(current) == k:
                sequenceses += 1
                current = set()


        return sequenceses + 1

'''
m*n



'''

def test ():
    params = [
        {
            'input': [[4,2,1,2,3,3,2,4,1], 4],
            'output': 3,
        },
        {
            'input': [[1,1,2,2], 2],
            'output': 2,
        },
        {
            'input': [[1,1,3,2,2,2,3,3], 4],
            'output': 1,
        },
        {
            'input': [[1,2,3,4,3,2,1], 4],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        rolls, k = param['input']
        result = solution.shortestSequence(rolls, k)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if correct else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
