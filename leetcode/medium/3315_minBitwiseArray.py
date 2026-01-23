import json
from collections import defaultdict, deque
from typing import List
# from functools import cache
import math


class Solution_0:
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


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num == 2:
                res.append(-1)
                continue

            i = 0
            while (num >> i) & 1:
                i += 1

            lastOneBit = 1 << (i - 1)
            flipped = num ^ lastOneBit
            res.append(flipped)

        return res


'''

11 1011
9  1001
10 1010

13 1101
13 1101
12 1100

15 | 16 = 31
31 11111
15 01111
16 10000


'''

def test():
    params = [
        {
            "input": [2,3,5,7],
            "output": [-1,1,4,3],
        },
        {
            "input": [11,13,31],
            "output": [9,12,15],
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
