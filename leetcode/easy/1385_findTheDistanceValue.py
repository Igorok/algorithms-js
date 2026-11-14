import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()

        def getId(val):
            start = 0
            end = len(arr2) - 1

            while start <= end:
                m = (start + end) // 2
                if val - d > arr2[m]:
                    start = m + 1
                elif val + d < arr2[m]:
                    end = m - 1
                else:
                    return m

            return -1

        res = 0
        for n in arr1:
            res += 1 if getId(n) == -1 else 0


        return res

def test():
    params = [
        {
            "input": [[4,5,8], [10,9,1,8], 2],
            "output": 2,
        },
        {
            "input": [[1,4,2,3], [-4,-3,6,10,20,30], 3],
            "output": 2,
        },
        {
            "input": [[2,1,100,3], [-5,-2,10,-3,7], 6],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        arr1, arr2, d = param["input"]
        result = solution.findTheDistanceValue(arr1, arr2, d)
        correct = json.dumps(result) == json.dumps(param["output"])

        msg = "SUCCESS" if correct else "ERROR"
        msg += "\n"
        if not correct:
            msg += "input " + json.dumps(param["input"]) + "\n"
            msg += "output " + json.dumps(param["output"]) + "\n"
            msg += "result " + json.dumps(result) + "\n"

        print(msg)


if __name__ == "__main__":
    test()
