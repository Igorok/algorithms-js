import json
from collections import deque
from typing import List


class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        left = -1
        acc = 0
        res = 0

        for right in range(n):
            if s[right] == '0':
                if right == n-1:
                    res += acc
                continue

            if right - left > 1:
                res += acc
            acc += 1
            left = right


        return res




'''
1001101
0001111


'''

def test():
    params = [
        {
            "input": '1001101',
            "output": 4,
        },
        {
            "input": '00111',
            "output": 0,
        },
        {
            "input": '1001100',
            "output": 4,
        },
        {
            "input": '110',
            "output": 2,
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.maxOperations(s)
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
