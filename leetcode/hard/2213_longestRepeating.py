
from typing import List
import json
from collections import deque, defaultdict
from functools import cache

'''

Do you know leetcode issue - "2213. Longest Substring of One Repeating Character"
I can not understand description.

'''




class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        return []


def test ():
    params = [
        {
            'input': ["babacc", "bcb", [1,3,3]],
            'output': [3,3,4],
        },
        {
            'input': ["abyzz", "aa", [2,1]],
            'output': [2,3],
        },
    ]
    solution = Solution()

    for param in params:
        s, queryCharacters, queryIndices = param['input']
        result = solution.longestRepeating(s, queryCharacters, queryIndices)
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
