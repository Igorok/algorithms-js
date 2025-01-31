from typing import List
import json
from collections import deque

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        charsLimit = [0]*26
        aOrd = ord('a')

        for char in letters:
            code = ord(char) - aOrd
            charsLimit[code] += 1

        def getScore(word, limit):
            r = 0
            for char in word:
                code = ord(char) - aOrd
                if limit[code] == 0 or score[code] == 0:
                    return 0
                limit[code] -= 1
                r += score[code]

            return r

        def rec(id, limit):
            if id == len(words):
                return 0

            r1 = rec(id + 1, limit.copy())
            r2 = getScore(words[id], limit) + rec(id + 1, limit)

            return max(r1, r2)

        return rec(0, charsLimit.copy())


def test ():
    params = [
        {
            'input': [
                ["dog","cat","dad","good"],
                ["a","a","c","d","d","d","g","o","o"],
                [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0],
            ],
            'output': 23,
        },
        {
            'input': [
                ["xxxz","ax","bx","cx"],
                ["z","a","b","c","x","x","x"],
                [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10],
            ],
            'output': 27,
        },
        {
            'input': [
                ["leetcode"],
                ["l","e","t","c","o","d"],
                [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0],
            ],
            'output': 0,
        },
    ]
    solution = Solution()

    for param in params:
        words, letters, score = param['input']
        result = solution.maxScoreWords(words, letters, score)
        correct = json.dumps(result) == json.dumps(param['output'])

        msg = 'SUCCESS' if json.dumps(result) == json.dumps(param['output']) else 'ERROR'
        msg += '\n'
        if not correct:
            msg += 'input ' + json.dumps(param['input']) + '\n'
            msg += 'output ' + json.dumps(param['output']) + '\n'
            msg += 'result ' + json.dumps(result) + '\n'

        print(msg)


if __name__ == '__main__':
    test()
