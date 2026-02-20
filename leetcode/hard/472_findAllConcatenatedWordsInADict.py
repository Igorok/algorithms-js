from typing import List
from collections import deque, defaultdict
from functools import cache
import re

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # words.sort(key = lambda x: (len(x), x))

        root = {}
        for word in words:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[';'] = None

        # print('words', words)

        # @cache
        def check(word, id):
            nonlocal root

            if id == len(word):
                return 0

            res = float('-inf')
            node = root
            for i in range(id, len(word)):
                char = word[i]
                if char not in node:
                    break
                node = node[char]
                if ';' in node:
                    r = 1 + check(word, i+1)
                    res = max(res, r)
            return res

        res = []
        for word in words:
            r = check(word, 0)
            if r > 1:
                res.append(word)

        return res
'''

cats
cat
sdog
catsdog

'''

def test ():
    params = [
        {
            'input': ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"],
            'output': ["catsdogcats","dogcatsdog","ratcatdogcat"],
        },
        {
            'input': ["cat","dog","catdog"],
            'output': ["catdog"],
        },
    ]
    solution = Solution()

    for param in params:
        words = param['input']
        result = solution.findAllConcatenatedWordsInADict(words)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            # 'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
