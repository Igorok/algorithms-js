from typing import List
import json
from collections import deque, defaultdict
import math

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        aCode = ord('a')
        codesByWord = {}

        for word in words:
            code = 0
            for char in word:
                val = ord(char) - aCode
                code = code | (1 << val)
            codesByWord[word] = {
                'c': code,
                'l': len(word),
            }


        res = 0
        for i in range(n):
            for j in range(i+1, n):
                w1 = words[i]
                w2 = words[j]

                if (codesByWord[w1]['c'] & codesByWord[w2]['c']) == 0:
                    r = codesByWord[w1]['l'] * codesByWord[w2]['l']
                    res = max(res, r)

        return res

def test ():
    params = [
        {
            'input': ["abcw","baz","foo","bar","xtfn","abcdef"],
            'output': 16,
        },
        {
            'input': ["a","ab","abc","d","cd","bcd","abcd"],
            'output': 4,
        },
        {
            'input': ["a","aa","aaa","aaaa"],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        words = param['input']
        result = solution.maxProduct(words)
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
