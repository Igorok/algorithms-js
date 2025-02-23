from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        def rec(_s):
            ls = len(_s)
            lp = len(part)
            if ls < lp:
                return _s

            for i in range(ls - lp + 1):
                if _s[i:i+lp] == part:
                    return rec(_s[:i] + _s[i+lp:])

            return _s

        return rec(s)


'''

abc
ababcc

'''


def test ():
    params = [
        {
            'input': ["daabcbaabcbc", "abc"],
            'output': 'dab',
        },
        {
            'input': ["axxxxyyyyb", "xy"],
            'output': 'ab',
        },
    ]
    solution = Solution()

    for param in params:
        s, part = param['input']
        result = solution.removeOccurrences(s, part)
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
