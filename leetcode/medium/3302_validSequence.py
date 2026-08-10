from typing import List
from json import dumps
from collections import deque
import heapq


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        return 0



def test ():
    params = [
        {
            'input': [
                "vbcca", "abc"
            ],
            'output':  [0,1,2],
        },
        {
            'input': [
                "bacdc", "abc"
            ],
            'output':  [1,2,4],
        },
        {
            'input': [
                "aaaaaa", "aaabc"
            ],
            'output':  [],
        },
        {
            'input': [
                "abc", "ab"
            ],
            'output':  [0,1],
        },
    ]
    solution = Solution()

    for param in params:
        word1, word2 = param['input']
        result = solution.validSequence(word1, word2)

        print(
            'SUCCESS' if result == param['output'] else 'ERROR',
            'input', param['input'],
            'output', param['output'],
            'result', result,
            '\n',
        )


if __name__ == '__main__':
    test()
