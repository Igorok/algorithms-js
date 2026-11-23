import heapq
import json
from collections import defaultdict, deque
from functools import cache
from typing import List

'''
0  1  2 3 4 5  6 7 8
1,-1,-1,1,1,1,-1-1,1


'''

class Solution:
    def getMaxLen(self, nums: list[int]) -> int:
        N = len(nums)
        memo = {
            'start': -1,
            'neg': -1,
            'left': -1,
            'right': -1,
        }

        res = 0
        acc = 1
        for i in range(N):
            num = nums[i]
            if num != 0:
                num = num // abs(num)

            acc = acc*num

            if acc == 0:
                acc = 1
                for k in memo:
                    memo[k] = -1
                continue

            if memo['start'] == -1:
                memo['start'] = i

            if acc < 0:
                if memo['neg'] == -1:
                    memo['neg'] = i
                    continue

                res = max(res, i - memo['neg'])
            else:
                if memo['neg'] == -1 and memo['left'] == -1:
                    memo['left'] = i
                elif memo['neg'] == -1 and memo['right'] == -1:
                    memo['right'] = i

                start = memo['start']
                res = max(res, i - start + 1)


        return res


def test():
    params = [
        {
            "input": [1,-2,-3,4],
            "output": 4,
        },
        {
            "input": [0,1,-2,-3,-4],
            "output": 3,
        },
        {
            "input": [-1,-2,-3,0,1],
            "output": 2,
        },
        {
            "input": [-1,2],
            "output": 1,
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.getMaxLen(nums)
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
