import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

"""
There is leetcode issue "3513. Number of Unique XOR Triplets I"

3 equal nums; res = 1 number
2 equal nums; res = 1 number
3 different number = ?

I have N numbers, last number is N = 100_000. Its binary representation length is 17
So i already have all bits combitation from 0 till 17. Can i make all bits combitation of length 17?
res = 2^17?
10000
01000
00011


"""


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 2:
            return N

        text = bin(N)[2:]
        cnt = 2 ** (len(text))

        return cnt


def test():
    params = [
        {
            "input": [1, 2],
            "output": 2,
        },
        {
            "input": [3, 1, 2],
            "output": 4,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.uniqueXorTriplets(nums)

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
