import json
from collections import defaultdict, deque
from functools import cache
from typing import List


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        small = [chr(i) for i in range(ord("a"), ord("z") + 1)]
        big = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
        english = set(small + big)

        # print("english", english)

        chars = []
        symb = []
        N = len(s)
        for i in range(N):
            if s[i] in english:
                chars.append(s[i])
            else:
                symb.append(i)

        symb.reverse()
        res = [""] * N

        for i in range(N):
            if len(symb) and symb[-1] == i:
                res[i] = s[symb.pop()]
                continue
            res[i] = chars.pop()

        return "".join(res)


def test():
    params = [
        {
            "input": "ab-cd",
            "output": "dc-ba",
        },
        {
            "input": "a-bC-dEf-ghIj",
            "output": "j-Ih-gfE-dCba",
        },
        {
            "input": "Test1ng-Leet=code-Q!",
            "output": "Qedo1ct-eeLg=ntse-T!",
        },
    ]
    solution = Solution()

    for param in params:
        s = param["input"]
        result = solution.reverseOnlyLetters(s)
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
