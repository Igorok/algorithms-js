import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def getMaxLength(length, removed):
            maxLength = 1
            uniq = set(removed)

            for bar in removed:
                left = bar-1
                right = bar+1
                while left >= 1 and right <= length+2 and (left in uniq or right in uniq):
                    if left in uniq:
                        left -= 1
                    if right in uniq:
                        right += 1

                maxLength = max(maxLength, right-left)

            return maxLength


        maxHeight = getMaxLength(n, hBars)
        maxLength = getMaxLength(m, vBars)

        return min(maxHeight, maxLength) ** 2

'''
"input": [1, 5, [2], [2,3]],

3 - - - - - -
2 x x
1 2 3 4 5 6 7

'''



def test():
    params = [
        {
            "input": [2, 1, [2,3], [2]],
            "output": 4,
        },
        {
            "input": [1, 1, [2], [2]],
            "output": 4,
        },
        {
            "input": [2, 3, [2,3], [2,4]],
            "output": 4,
        },
        {
            "input": [1, 5, [2], [2,3]],
            "output": 4,
        },
        {
            "input": [3, 2, [3,2,4], [3,2]],
            "output": 9,
        },
    ]
    solution = Solution()

    for param in params:
        n, m, hBars, vBars = param["input"]
        result = solution.maximizeSquareHoleArea(n, m, hBars, vBars)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            # msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
