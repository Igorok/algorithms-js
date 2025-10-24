from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        remainders = {}
        for num in nums:
            r = num % value
            remainders[r] = remainders.get(r, 0 ) + 1

        n = len(nums)
        nonNegative = [0] * (n+1)
        for r in remainders:
            for i in range(remainders[r]):
                val = i * value + r
                if val >= n+1:
                    break
                nonNegative[val] = 1

        for i in range(n+1):
            if nonNegative[i] == 0:
                return i

        return 0

'''

[[1,-10,7,13,6,8], 5]

1,-10,7,13,6,8
1, 0, 2, 3,1,3


'''



def test():
    params = [
        {
            "input": [[1,-10,7,13,6,8], 5],
            "output": 4,
        },
        {
            "input": [[1,-10,7,13,6,8], 7],
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        nums, value = param["input"]
        result = solution.findSmallestInteger(nums, value)
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
