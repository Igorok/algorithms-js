from typing import List
import json
from collections import deque, defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def getCode(char):
            return ord(char) - ord('A')

        res = 1
        left = 0
        maxLength = 1
        chars = [0]*26
        chars[getCode(s[left])] = 1

        for right in range(1, len(s)):
            chars[getCode(s[right])] += 1
            maxLength = max(maxLength, chars[getCode(s[right])])
            length = right - left + 1

            while length - maxLength > k:
                chars[getCode(s[left])] -= 1
                left += 1
                length = right - left + 1
                maxLength = max(chars)

            res = max(res, length)

        return res

def test():
    params = [
        {
            "input": ["ABAB", 2],
            "output": 4,
        },
        {
            "input": ["AABABBA", 1],
            "output": 4,
        },
    ]
    solution = Solution()

    for param in params:
        s, k = param["input"]
        result = solution.characterReplacement(s, k)
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
