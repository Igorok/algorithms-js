from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def sortVowels(self, s: str) -> str:
        n = len(s)
        vowelsSet = set(['a', 'e', 'i', 'o', 'u'])
        vowels = []

        res = [None] * n
        for i in range(n):
            if s[i].lower() in vowelsSet:
                vowels.append(s[i])
            else:
                res[i] = s[i]

        vowels.sort()
        vId = 0
        for i in range(n):
            if res[i] == None:
                res[i] = vowels[vId]
                vId += 1

        return ''.join(res)



def test ():
    params = [
        {
            'input': 'lEetcOde',
            'output': 'lEOtcede',
        },
        {
            'input': 'lYmpH',
            'output': 'lYmpH',
        },
    ]
    solution = Solution()

    for param in params:
        s = param['input']
        result = solution.sortVowels(s)
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
