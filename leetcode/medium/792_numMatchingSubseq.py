from typing import List
import heapq
import math
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        N = len(s)
        chars = defaultdict(list)

        for i in range(N):
            chars[s[i]].append(i)

        def getCharId(char, val):
            if char not in chars:
                return -1

            left = 0
            right = len(chars[char]) - 1
            res = -1

            while left <= right:
                m = (left + right) // 2
                if chars[char][m] >= val:
                    res = chars[char][m]
                    right = m - 1
                else:
                    left = m + 1

            return res

        res = 0
        for word in words:
            left = 0

            for char in word:
                left = getCharId(char, left)
                if left == -1:
                    break
                left += 1

            if left != -1:
                res += 1

        return res


def test ():
    params = [
        {
            'input': [
                "abcde", ["a","bb","acd","ace"]
            ],
            'output': 3,
        },
        {
            'input': [
                "dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
            ],
            'output': 2,
        },
    ]
    solution = Solution()

    for param in params:
        s, words = param['input']
        result = solution.numMatchingSubseq(s, words)
        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
