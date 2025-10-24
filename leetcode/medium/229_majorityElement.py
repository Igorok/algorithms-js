from typing import List
import json
from collections import deque, defaultdict
from functools import lru_cache


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        minLength = n / 3
        res = []
        left = 0
        for right in range(n):
            if nums[right] != nums[left]:
                length = right - left
                if length > minLength:
                    res.append(nums[left])
                left = right

        length = n - left
        if length > minLength:
            res.append(nums[left])

        return res;

def test():
    params = [
        {
            "input": [3,2,3],
            "output": [3],
        },
        {
            "input": [1],
            "output": [1],
        },
        {
            "input": [1,2],
            "output": [1,2],
        },
    ]
    solution = Solution()

    for param in params:
        nums = param["input"]
        result = solution.majorityElement(nums)
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
