import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        n = len(s)

        def isOk(word):
            m = len(word)
            i = 0
            j = 0
            while i < m and j < n:
                if s[j] == word[i]:
                    i += 1
                    j += 1
                else:
                    j += 1

            return i == m

        res = ''

        for word in dictionary:
            if isOk(word):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word

        return res


def test ():
    params = [
        {
            'input': ['abpcplea', ['ale','apple','monkey','plea']],
            'output': 'apple',
        },
        {
            'input': ['abpcplea', ['a','b','c']],
            'output': 'a',
        },
    ]
    solution = Solution()

    for param in params:
        s, dictionary = param['input']
        result = solution.findLongestWord(s, dictionary)
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
