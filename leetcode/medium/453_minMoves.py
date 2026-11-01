import heapq
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache
from typing import List



class Solution_0:
    def minMoves(self, nums: list[int]) -> int:
        N = len(nums)
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1

        data = sorted(cnt.keys())

        # print('data', data)
        # print('cnt', cnt)

        res = 0
        while len(data) != 1:
            res += 1
            num = data.pop()
            cnt[num-1] = cnt.get(num-1, 0) + 1

            if data[-1] != num - 1:
                data.append(num-1)

            if cnt[num] == 1:
                del cnt[num]
                continue

            data.append(num)
            cnt[num] -= 1

        return res


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1, 0, -1):
            res += nums[i] - nums[0]
        return res

'''
[1,2,3]
[2,3,3]
[3,3,4]
[4,4,4]
---
[1,2,3]
[1,2,2]
[1,2,1]
[1,1,1]


'''


def test():
    params = [
        {
            "input": [1,2,3],
            "output": 3,
        },
        {
            "input": [1,1,1],
            "output": 0,
        },
        {
            "input": [-1,1],
            "output": 2,
        },
        {
            "input": [1,100],
            "output": 99,
        },
        {
            "input": [1,100, 100],
            "output": 198,
        },
        {
            "input": [1,1000000000],
            "output": 999999999,
        },

    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.minMoves(nums)

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
