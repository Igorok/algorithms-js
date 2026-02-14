import sys
sys.setrecursionlimit(1500)
from typing import List
import json
from collections import deque, defaultdict
import heapq
import math



class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        chars = {}

        for word in words:
            root = chars
            for i in range(len(word)-1, -1, -1):
                if word[i] not in root:
                    root[word[i]] = {}
                root = root[word[i]]

        res = 0
        def dfs(root, acc):
            nonlocal res

            if not root:
                res += acc + 1

            for key in root:
                dfs(root[key], acc+1)


        dfs(chars, 0)


        return res


def test ():
    params = [
        {
            'input': ["time", "me", "bell"],
            'output': 10,
        },
        {
            'input': ["t"],
            'output': 2,
        },
        {
            'input': ["t"],
            'output': 2,
        },
        {
            'input': ["time","bell","mee","me"],
            'output': 14,
        },
    ]
    solution = Solution()

    for param in params:
        words = param['input']
        result = solution.minimumLengthEncoding(words)
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
