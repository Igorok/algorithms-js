import heapq
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from typing import List


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            r = 0
            for char in word:
                weigh = weights[ord(char) - ord('a')]
                r = (r + weigh) % 26
            r = 25 - r
            res.append(chr(r + ord('a')))
        return ''.join(res)
        
        
def test():
    params = [
        {
            "input": [
                ["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]
            ],
            "output": "rij",
        },
        {
            "input": [
                ["a","b","c"], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ],
            "output": "yyy",
        },
        {
            "input": [
                ["abcd"], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]
            ],
            "output": "g",
        },
    ]
    solution = Solution()

    for param in params:
        words, weights = param["input"]
        result = solution.mapWordWeights(words, weights)
        print(
            "SUCCESS" if result == param["output"] else "ERROR",
            "input",
            param["input"],
            "output",
            param["output"],
            "result",
            result,
            "\n",
        )


if __name__ == "__main__":
    test()
