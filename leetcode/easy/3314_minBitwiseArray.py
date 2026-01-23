import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []


        for n in nums:
            found = -1
            for val in range(0, n):
                if val | (val + 1) == n:
                    found = val
                    break
            res.append(found)

        return res

'''

x | (x+1) = y

11
10
01

101
101

111
011
100


'''

def test():
    params = [
        {
            "input": [2,3,5,7],
            "output": [-1,1,4,3],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minBitwiseArray(nums)
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
