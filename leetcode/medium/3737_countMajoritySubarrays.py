import heapq
import math
from collections import Counter, defaultdict
from functools import cache
from json import dumps
from operator import countOf
from typing import List


class Solution_0:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        res = 0

        for i in range(N):
            count = 0
            for j in range(i, N):
                if nums[j] == target:
                    count += 1
                if count > (j - i + 1) // 2:
                    res += 1

        return res


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # freq map to keep track of how many times each prefix sum has appeared
        freq = {0: 1}

        cur = 0
        smaller_count = 0
        ans = 0

        for num in nums:
            if num == target:
                # cur increases by 1
                smaller_count += freq.get(cur, 0)
                cur += 1
            else:
                # cur decreases by 1
                cur -= 1
                smaller_count -= freq.get(cur, 0)

            ans += smaller_count
            freq[cur] = freq.get(cur, 0) + 1

        return ans


"""
"input": [[1, 2, 2, 3], 2],
"output": 5,

1, 2, 2, 3, 2, 4
-1 1  1 -1  1 -1
-1 0  1  0  1  0

2, 5, 2, 1

3737. Count Subarrays With Majority Element I
3739. Count Subarrays With Majority Element II




"""


def test():
    params = [
        {
            "input": [[1, 2, 2, 3], 2],
            "output": 5,
        },
        {
            "input": [[1, 1, 1, 1], 1],
            "output": 10,
        },
        {
            "input": [[1, 2, 3], 4],
            "output": 0,
        },
        {
            "input": [[1, 2, 2, 3, 2, 4], 2],
            "output": 10,
        },
    ]
    solution = Solution()

    for param in params:
        nums, target = param["input"]
        result = solution.countMajoritySubarrays(nums, target)
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
