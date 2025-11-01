from typing import List
import json
from collections import deque, defaultdict
import heapq

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0

        for row in bank:
            cnt = row.count('1')
            res += prev * cnt
            if cnt != 0:
                prev = cnt

        return res



def test ():
    params = [
        {
            'input': ["011001","000000","010100","001000"],
            'output': 8,
        },
        {
            'input': ["000","111","000"],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        bank = param['input']
        result = solution.numberOfBeams(bank)
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
