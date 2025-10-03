from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        return 0


def test ():
    params = [
        {
            'input': 'bccb',
            'output': 6,
        },
        {
            'input': 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba',
            'output': 104860361,
        },
    ]
    solution = Solution()

    for param in params:
        result = solution.countPalindromicSubsequences(param['input'])
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
