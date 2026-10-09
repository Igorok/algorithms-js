import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        N = len(s)
        left = 0
        memo = [0] * 26

        def checkCnt():
            charCount = max(memo)

            if charCount < k:
                return False

            if charCount > k:
                return True

            repeat = [v for v in memo if v == k]
            if len(repeat) > 1:
                return True

            code = ord(s[left]) - ord("a")
            if memo[code] != k:
                return True

            return False

        res = 0

        for right in range(N):
            code = ord(s[right]) - ord("a")
            memo[code] += 1

            while checkCnt():
                code = ord(s[left]) - ord("a")
                memo[code] -= 1
                left += 1

            if max(memo) == k:
                r = 1 * (left + 1)
                res += r

        return res


def test():
    params = [
        {
            "input": ["abacb", 2],
            "output": 4,
        },
        {
            "input": ["abcde", 1],
            "output": 15,
        },
        {
            "input": ["hxccgfp", 1],
            "output": 28,
        },
        {
            "input": ["ajsrhoebe", 2],
            "output": 7,
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param["input"]
        result = solution.numberOfSubstrings(s, k)
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
