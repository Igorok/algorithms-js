from typing import List
import json
from collections import deque, defaultdict
import heapq
import math
from functools import cache

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: (len(x), x))

        used = set()
        res = ''

        for word in words:
            if len(word) == 1:
                used.add(word)
            else:
                subsrt = word[:len(word) - 1]
                if subsrt in used:
                    used.add(word)
                else:
                    continue

            if len(word) > len(res) or (len(word) == len(res) and word < res):
                res = word

        return res

def test ():
    params = [
        {
            'input': ["w","wo","wor","worl","world"],
            'output': 'world',
        },
        {
            'input': ["a","banana","app","appl","ap","apply","apple"],
            'output': 'apple',
        },
        {
            'input': ["ts","e","x","pbhj","opto","xhigy","erikz","pbh","opt","erikzb","eri","erik","xlye","xhig","optoj","optoje","xly","pb","xhi","x","o"],
            'output': 'e',
        },
    ]
    solution = Solution()

    for param in params:
        words = param['input']
        result = solution.longestWord(words)
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
